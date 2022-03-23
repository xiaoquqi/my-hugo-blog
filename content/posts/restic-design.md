---
title: Restic设计原理
slug: restic-design
date: 2022-03-23T07:40:36+08:00
draft: true
author: 老孙正经胡说
tags:
  - restic
  - 文件同步
categories:
  - restic
---

Restic(https://github.com/restic/restic)一款开源文件备份工具，存储文件前将文件切割成对象进行存储，可以支持多种存储后端，包括本地目录、SFTP、HTTP Server和多种云平台的对象存储。Restic支持快照等备份常用功能，同时兼顾数据存储的安全性。

本文主要讲解Restic设计原理，内容来源于Restic官方文档的Design篇(https://restic.readthedocs.io/en/latest/100_references.html#design)。

## 术语

这一节主要介绍文档中使用的专业术语。

存储库（Repository）：备份过程中生成的所有数据都以结构化形式发送并存储在存储库中，例如：存储在文件系统中，文件系统中可以创建多级目录。作为存储库，必须具备多种操作能力，例如列出内容。

Blob: Blob是将数据与识别信息（如数据的 SHA-256 哈希值及其长度）组合在一起。

包（Pack）: 一个Pack将多个Blobs进行组合，例如在一个文件中

快照（Snapshot）: 一个快照是文件和目录在某个备份时间点的状态。状态的含义是内容以及元数据（metadata）信息，例如：文件或目录及其内容的名称、修改时间。 

存储ID（Storage ID）：存储ID是存储库中存放内容的SHA-256。只有得到此ID才能从存储库中加载文件。

## 存储库格式

所有数据存放在restic存储库中。存储库可以存储不同类型的数据，可以根据ID获取。”Storage ID”是文件内容的SHA-256哈希值。存储库内所有文件仅仅写入一次，后续不再修改。这可以让多个客户端并发访问，甚至是写入到存储库中。仅仅只有删除操作将数据从存储库中移除。

在撰写本文时，仅仅实现的存储库后端是基于文件系统的目录和文件。可以在同一系统或者内置的SFTP客户端（或者其他的后端方式）访问存储库。两种访问方法的目录布局相同。存储库类型会在后续详细描述。

存储库由多个目录和一个名为 config 的文件组成。 对于存储库中的其他所有文件，文件的名称是存储 ID 的小写十六进制表示，即文件内容的 SHA-256 哈希。 通过简单地运行程序 sha256sum 并将其输出与文件名进行比较，轻松验证文件是否有意外修改，例如磁盘读取错误。 如果文件名的前缀在同一目录中是唯一的，则可以使用前缀代替完整的文件名。

除了存储在 `keys` 目录中的文件外，所有文件都在计数器模式 (CTR) 下使用 AES-256 进行加密。 加密数据的完整性由 Poly1305-AES 消息验证码（有时也称为“签名”）保护。

在每个加密文件的前 16 个字节中，存储了初始化向量 (IV)。 其后是加密数据并由 16 字节 MAC 结尾。 格式为：`IV || 密文 || MAC`。 完整的加密开销为 32 个字节。 对于每个文件，都会选择一个新的随机 IV。

文件 `config` 以这种方式加密，并包含如下 JSON 文档：

```python
{
  "version": 1,
  "id": "5956a3f67a6230d4a92cefb29529f10196c7d92582ec305fd71ff6d331d6271b",
  "chunker_polynomial": "25b468838dcb75"
}
```

解密后，restic 首先检查版本字段是否包含它可以理解的版本号，否则会中止。 此时，版本预计为 1。字段 `id` 包含一个由 32 个随机字节组成的唯一 ID，以十六进制编码。 无论是通过 SFTP 还是在本地访问它，这都会唯一标识存储库。 `chunker_polynomial` 字段包含一个参数，用于将大文件分割成更小的块（见下文）。

restic 存储库的基本布局如下所示：

```python
/tmp/restic-repo
├── config
├──data
│   ├── 21
│   │   └── 2159dd48f8a24f33c307b750592773f8b71ff8d11452132a7b2e2a6a01611be1
│   ├── 32
│   │   └── 32ea976bc30771cebad8285cd99120ac8786f9ffd42141d452458089985043a5
│   ├── 59
│   │   └── 59fe4bcde59bd6222eba87795e35a90d82cd2f138a27b6835032b7b58173a426
│   ├── 73
│   │   └── 73d04e6125cf3c28a299cc2f3cca3b78ceac396e4fcf9575e34536b26782413c
│   [...]
├── index
│   ├── c38f5fb68307c6a3e3aa945d556e325dc38f5fb68307c6a3e3aa945d556e325d
│   └── ca171b1b7394d90d330b265d90f506f9984043b342525f019788f97e745c71fd
├── keys
│   └── b02de829beeb3c01a63e6b25cbd421a98fef144f03b9a02e46eff9e2ca3f0bd7
├── locks
├── snapshots
│   └── 22a5af1bdc6e616f8a29579458c49627e01b32210d09adb288d1ecda7c5711ec
└── tmp
```

存储库可以使用restic init命令初始化，例如：

```python
$ restic -r /tmp/restic-repo init
```

## 包（Pack）格式

除 Key 和 Pack 文件外，存储库中的所有文件仅包含原始数据，存储为`IV || 密文 || 麦克`。 包文件可能包含一个或多个 Blob 数据。

一个包的结构如下：

```python
EncryptedBlob1 || ... || EncryptedBlobN || EncryptedHeader || Header_Length
```

Pack 文件的末尾是header，它描述了内容。header经过加密和身份验证。 `Header_Length` 是加密头的长度，使用四字节整数little-endian编码。将header放置在文件末尾，目的是为了在备份过程中，读取blob后立即将他们写入连续的流中。这降低了代码的复杂度，并且避免了在包完成后，在已知内容和header长度后重复写入文件的问题。

所有 blob（`EncryptedBlob1`、``EncryptedBlobN` 等）都经过独立鉴权和加密。存储库可以在无需解密Blob情况下，进行重组。此外，还可以进行高效的索引，因为只需要读取header，找出Pack中包含哪些Blob。因为header是经过鉴权的，因此可以检查header的真实性，而无需读取完整的Pack。

解密后，Pack 的头部由以下元素组成：

```python
Type_Blob1 ||Length(EncryptedBlob1) ||Hash(Plaintext_Blob1) ||
[...]
Type_BlobN ||Length(EncryptedBlobN) ||Hash(Plaintext_Blobn) ||
```

这足以计算Pack中所有 Blob 的偏移量。 长度是 Blob 的长度，它是 little-endian 格式的四字节整数。 type 字段是一个单字节字段，根据下表标记 blob 的内容：

| Type | Meaning |
| --- | --- |
| 0 | data |
| 1 | tree |

所有其他类型均无效，未来可能会添加更多类型。

为了重建索引或解析没有索引的Pack，首先必须读取最后四个字节才能找到header的长度。 之后，可以读取和解析header，这会产生所有已包含的 blob 的明文哈希、类型、偏移量和长度。

## 索引（indexing）

索引文件包含有关数据和树Blob树及其所在Pack的信息，并将此信息存储在存储库中。 当本地缓存索引不再可用时，可以下载索引文件并重建索引。 这些文件像数据和Blob树同样经过加密和鉴权，因此外部结构仍然是 IV || 密文 || Mac。 明文由如下 JSON 文档组成：

```
{
  "supersedes": [
    "ed54ae36197f4745ebc4b54d10e0f623eaaaedd03013eb7ae90df881b7781452"
  ],
  "packs": [
    {
      "id": "73d04e6125cf3c28a299cc2f3cca3b78ceac396e4fcf9575e34536b26782413c",
      "blobs": [
        {
          "id": "3ec79977ef0cf5de7b08cd12b874cd0f62bbaf7f07f3497a5b1bbcc8cb39b1ce",
          "type": "data",
          "offset": 0,
          "length": 25
        },{
          "id": "9ccb846e60d90d4eb915848add7aa7ea1e4bbabfc60e573db9f7bfb2789afbae",
          "type": "tree",
          "offset": 38,
          "length": 100
        },
        {
          "id": "d3dc577b4ffd38cc4b32122cabf8655a0223ed22edfd93b353dc0c3f2b0fdf66",
          "type": "data",
          "offset": 150,
          "length": 123
        }
      ]
    }, [...]
  ]
}

```

此 JSON 文档列出了Packs和其中包含的 blob。 在此示例中，Pack `73d04e61` 包含两个数据 Blob 和一个 Blob树，明文哈希随后列出。

字段 `supersedes` 列出了已被当前索引文件替换的索引文件的存储 ID。 这发生在重新打包索引文件时，例如删除旧快照并重新组合包时。

可能有任意数量的索引文件，其中包含关于不相交的Pack集合的信息。 选择在单一文件中描述的Packs数量，让文件大小保持在8MiB一下。

## 密钥（Keys），加密和MAC

所有存放在restic存储库中的数据使用计数器模式AES-256加密，鉴权使用Poly1305-AES。为了加密新数据，从密码安全的伪随机数生成器中读取前 16 个字节作为随机随机数。这既用作计数器模式的 IV，也用作 Poly1305 的随机数。该操作需要三个密钥：用于加密的 AES-256 的 32 字节、用于 Poly1305 的 16 字节的 AES 密钥和 16 字节的密钥。有关详细信息，请参阅 Dan Bernstein 的原始论文 [The Poly1305-AES 消息身份验证代码](http://cr.yp.to/mac/poly1305-20050329.pdf)。然后使用 AES-256 对数据进行加密，然后在密文上计算消息验证码 (MAC)，然后将所有内容存储为 IV || 密文 || MAC。

目录 `keys` 包含密钥文件。这些是简单的 JSON 格式文档，包含从用户密码派生存储库的主加密和消息身份验证密钥所需的所有数据。例如，可以使用 Python 模块 `json`（缩短以提高可读性）来优化打印存储库中的 JSON 文档：

```
$ python -mjson.tool /tmp/restic-repo/keys/b02de82*
{
    "hostname": "kasimir",
    "username": "fd0"
    "kdf": "scrypt",
    "N": 65536,
    "r": 8,
    "p": 1,
    "created": "2015-01-02T18:10:13.48307196+01:00",
    "data": "tGwYeKoM0C4j4/9DFrVEmMGAldvEn/+iKC3te/QE/6ox/V4qz58FUOgMa0Bb1cIJ6asrypCx/Ti/pRXCPHLDkIJbNYd2ybC+fLhFIJVLCvkMS+trdywsUkglUbTbi+7+Ldsul5jpAj9vTZ25ajDc+4FKtWEcCWL5ICAOoTAxnPgT+Lh8ByGQBH6KbdWabqamLzTRWxePFoYuxa7yXgmj9A==",
    "salt": "uW4fEI1+IOzj7ED9mVor+yTSJFd68DGlGOeLgJELYsTU5ikhG/83/+jGd4KKAaQdSrsfzrdOhAMftTSih5Ux6w==",
}

```

当打开restic存储库时，会提示用户输入存储库密码。然后将其与 `scrypt`、密钥派生函数 (KDF) 和提供的参数（`N`、`r`、`p` 和`salt`）一起派生 64 个密钥字节。前 32 个字节用于加密密钥（用于 AES-256），最后 32 个字节用作消息验证密钥（用于 Poly1305-AES）。这最后 32 个字节被分成一个 16 字节的 AES 密钥“k”，然后是 16 个字节的密钥“r”。然后将密钥` r` 屏蔽，与 Poly1305 一起使用（有关详细信息，请参阅论文）。

这些消息身份验证密钥（`k` 和 `r`）用于计算MAC，使用 JSON 中 `data`字段包含的字节（在删除 Base64 编码并且不包括最后 32 个字节之后）。如果密码不正确或密钥文件被篡改，则计算出的 MAC 将与数据的最后 16 个字节不匹配，restic 会报错退出。否则，将使用从 scrypt 派生的加密密钥解密数据。这将生成一个 JSON ，其中包含此存储库的主加密和消息鉴权密钥（以 Base64 编码）。 `restic cat masterkey` 命令可用于解密和格式化打印主密钥：

```
$ restic -r /tmp/restic-repo cat masterkey
{
    "mac": {
      "k": "evFWd9wWlndL9jc501268g==",
      "r": "E9eEDnSJZgqwTOkDtOp+Dw=="
    },
    "encrypt": "UQCqa0lKZ94PygPxMRqkePTZnHRYh1k1pX2k2lM2v3Q=",
}

```

存储库中的所有数据都使用这些主密钥进行加密和验证。 对于加密，使用计数器模式下的 AES-256 算法。 对于消息认证，如上所述使用 Poly1305-AES。

存储库可以有多个不同的密码，每个密码都有一个密钥文件。 这样，无需重新加密所有数据即可更改密码。

## 快照（Snapshots）

快照表示在特定时间点包含所有文件和子目录的目录。 对于所做的每个备份，都会创建一个新快照。 快照使用JSON文件描述，存储在存储库中“snapshots”目录下的加密文件。 文件名是存储 ID。 此字符串是唯一的，并在 restic 中用于唯一标识快照。

`restic cat snapshot` 命令可用于解密和格式化打印快照文件的内容：

```
$ restic -r /tmp/restic-repo cat snapshot 22a5af1b
enter passwordfor repository:
{
  "time": "2015-01-02T18:10:50.895208559+01:00",
  "tree": "2da81727b6585232894cfbb8f8bdab8d1eccd3d8f7c92bc934d62e62e618ffdf",
  "dir": "/tmp/testdata",
  "hostname": "kasimir",
  "username": "fd0",
  "uid": 1000,
  "gid": 100
}
```

在这里可以看出，这个快照代表了目录`/tmp/testdata`的内容。 最重要的字段是`tree`。

restic 存储库中的所有内容都根据其 SHA-256 哈希值进行引用。 在保存之前，每个文件都被分割成可变大小的数据块。 所有 Blob 的 SHA-256 哈希值都保存在有序列表中，代表文件的内容。

为了将这些明文哈希与 Pack 文件中的实际位置相关联，使用了索引。 如果索引不可用，则可以读取所有数据 Blob 的header。

## 树（Tree）和数据（Data）

快照通过JSON中SHA-256哈希引用树，代表其内容树和数据保存在目录“data”的子目录中的Pack文件中。

命令 `restic cat tree` 可用于检查上面引用的树：

```
$ restic -r /tmp/restic-repo cat tree b8138ab08a4722596ac89c917827358da4672eac68e3c03a8115b88dbf4bfb59
enter passwordfor repository:
{
  "nodes": [
    {
      "name": "testdata",
      "type": "dir",
      "mode": 493,
      "mtime": "2014-12-22T14:47:59.912418701+01:00",
      "atime": "2014-12-06T17:49:21.748468803+01:00",
      "ctime": "2014-12-22T14:47:59.912418701+01:00",
      "uid": 1000,
      "gid": 100,
      "user": "fd0",
      "inode": 409704562,
      "content": null,
      "subtree": "b26e315b0988ddcd1cee64c351d13a100fedbc9fdbb144a67d1b765ab280b4dc"
    }
  ]
}
```

树包包含一组节点（在“node”字段中），其中包含名称和时间戳等元数据。 当节点指向目录时，字段“subtree”包含另一个树对象的ID。

当使用命令“restic cat tree”时，需要存储哈希来显示树。 上面引用的树可以展开输出为：

```
$ restic -r /tmp/restic-repo cat tree 8b238c8811cc362693e91a857460c78d3acf7d9edb2f111048691976803cf16e
enter passwordfor repository:
{
  "nodes": [
    {
      "name": "testfile",
      "type": "file",
      "mode": 420,
      "mtime": "2014-12-06T17:50:23.34513538+01:00",
      "atime": "2014-12-06T17:50:23.338468713+01:00",
      "ctime": "2014-12-06T17:50:23.34513538+01:00",
      "uid": 1000,
      "gid": 100,
      "user": "fd0",
      "inode": 416863351,
      "size": 1234,
      "links": 1,
      "content": [
        "50f77b3b4291e8411a027b9f9b9e64658181cc676ce6ba9958b95f268cb1109d"
      ]
    },
    [...]
  ]
}
```

该树包含一个文件。 这一次，`subtree` 字段不存在，`content` 字段包含一个 SHA-256 哈希的列表。

命令 `restic cat data` 可用于提取和解密指定明文 ID 的数据，例如 对于上述数据：

```
$ restic -r /tmp/restic-repo cat blob 50f77b3b4291e8411a027b9f9b9e64658181cc676ce6ba9958b95f268cb1109d | sha256sum
enter passwordfor repository:
50f77b3b4291e8411a027b9f9b9e64658181cc676ce6ba9958b95f268cb1109d  -
```

从 sha256sum 的输出可以看出，哈希与上面树中包含的映射的明文哈希匹配，因此返回了正确的数据。

## 锁（Locks）

restic 存储库设计方式是允许并发访问，甚至并行写入。 但是，有些功能工作效率要求更高，甚至需要对存储库进行独占访问。 为了实现这些功能，需要restic进程在执行任何操作之前，在存储库上创建一个锁。

锁有两种类型：排他锁和非排他锁。 一个进程最多可以在存储库上拥有一个独占锁，并且在此期间不得有任何其他锁（独占和非独占）。 对于排它锁，可能并行存在多个。

锁是子目录`locks`中的文件，其文件名是内容的存储ID。 它的加密和鉴权方式与存储库中的其他文件相同，并包含以下 JSON 结构：

```
{
  "time": "2015-06-27T12:18:51.759239612+02:00",
  "exclusive": false,
  "hostname": "kasimir",
  "username": "fd0",
  "pid": 13607,
  "uid": 1000,
  "gid": 100
}
```

字段 `exclusive` 定义了锁的类型。 当要创建新锁时，restic 会检查存储库中的所有锁。 找到锁时，会测试锁是否超时，默认时间为大于30分钟以上。 如果锁是在同一台机器上创建的，即使对于没有达到超时时间的锁，它也会通过向它发送信号来测试进程是否还活着。 如果失败，restic 假定进程已死，并认为锁是无用的。

当要创建一个新锁并且没有检测到与其他冲突锁时，restic 创建一个新锁，等待并检查存储库中是否出现其他锁。 根据其他锁的类型和要创建的锁，restic 要么继续，要么失败。

## **备份和重复数据删除**

为了创建备份，restic 会扫描源目录中的所有文件、子目录和其他条目。 来自每个文件的数据被拆分为可变长度的 Blob，这些 Blob 以 64 字节的滑动窗口定义的偏移量进行切割。 该实现使用 Rabin 指纹来实现内容定义分块 (Content Defined Chunking, CDC)。 初始化存储库时，随机选择一个不可约多项式(不可约多项式，顾名思义即不能写成两个次数较低的多项式之乘积的多项式)并保存在文件 `config` 中，增加安全性，让水印攻击更加困难。

小于 512 KiB 的文件不会被拆分，Blob 的大小为 512 KiB 到 8 MiB。 实现的目标是Blob平均 1 MiB 大小。

对于修改过的文件，只有修改过的 Blob 必须保存在后续备份中。 即使在文件中的任意位置插入或删除字节，仍然可以继续工作。

# **威胁模型**

restic 的设计目标是能够将备份安全地存储在不完全受信任的位置，例如共享系统，其他人可以在其中访问文件（在系统管理员的情况下）甚至修改或删除它们。

一般假设：

- 创建备份的主机系统是受信任的。这是最基本的要求，对于创建可靠的备份至关重要。
- 用户使用的是正版restic
- 用户不与攻击者共享存储库密码。
- restic 备份程序并非是设计防止攻击者删除存储位置的文件。对此无能为力。如果需要保证这一点，一定要选择没有第三方可以访问的安全位置
- 如果密钥泄露，整个存储库将重新加密。使用当前的密钥管理设计，如果不重新加密整个存储库，就不可能安全地撤销泄露的密钥。
- 针对 restic 使用的加密原语（即 AES-256-CTR-Poly1305-AES 和 SHA-256），尚无法实现攻击。如果能够实现，会使 restic 提供的机密性或完整性保护变得无用。
- 算力方面进步还无法实现对 restic 加密保护的暴力攻击

restic 备份程序可以保证以下内容：

- 如果没有存储库的密码，就无法访问存储文件和元数据的未加密内容。密钥文件中除了用于信息描述目的的元数据之外的所有内容都经过加密和鉴权的。缓存中的内容也进行了加密，防止metadata泄露
- 对于存储在存储库中的所有数据的修复（坏 RAM、损坏的硬盘）可以被检测到
- 被篡改的数据将无法解密

考虑到上述假设和保证，以下是各种的攻击手段：

对备份存储位置具有读取权限的对手可以：

- 尝试对存储库副本进行暴力密码猜测攻击（推荐使用 30 个以上字符的长密码）。
- 通过文件访问模式推断哪些包可能包含树。
- 通过使用存储库对象的创建时间戳推断备份的大小。

具有网络访问权限的对手可以：

- 尝试 DoS 存储备份存储库的服务器或客户端和服务器之间的网络连接。
- 确定您创建备份的位置（即请求的来源位置）。
- 确定您存储备份的位置（即，哪个提供程序/目标系统）。
- 通过使用存储库对象的创建时间戳推断备份的大小。

以下是与违反上述某些假设后产生影响的示例。

破坏主机系统进行备份（通过恶意软件、物理访问等）：

- 使整个备份过程变得不可信（例如，拦截密码、复制文件、操纵数据）。
- 创建覆盖所有修改文件的快照（包含垃圾数据），并等到受信任的主机遗失所有正确的快照。
- 为每个时间戳稍有不同的快照创建一个垃圾快照，等到忘记运行后，一次性删除所有正确快照

在存储位置对您的文件具有写访问权限可以：

- 删除或操作您的备份，从而削弱您从受损存储位置恢复文件的能力。
- 确定哪些文件属于哪个快照（例如，基于存储文件的时间戳）。 当仅删除这些文件时，特定快照会消失，并且依赖于快照中的数据将无法完全恢复。Restic 并非设计来检测这种攻击。

破坏具有对备份存储库附加访问权限的主机系统可以：

- 主机收到攻击后，使新的备份不可信（由于对新备份具有完全控制权）。 攻击者无法删除或操作旧备份。 因此，恢复在主机入侵之前*创建的旧快照仍然是可能的。 *注意：**不**建议对仅追加快照运行自动忘记，当这些主机可能受到威胁时，因为使用虚假快照的攻击者可能会导致忘记删除正确的快照。*

拥有未重新加密的存储库的泄露密钥可以：

- 解密现有和未来的备份数据。 如果多台主机备份到同一个存储库，攻击者将可以访问每台主机的备份数据。