---
title: Restic原理分析
slug: restic-analysis
date: 2022-04-22T18:23:33+08:00
draft: false
author: 老孙正经胡说
tags:
  - restic
  - 文件同步
categories:
  - restic
---

## 创建存储库

初始化存储库（本地）

```yaml
restic init --repo ./restic_repo
```

回车后，需要输入密码

```yaml
enter password for new repository:
enter password again:
created restic repository 56f6f17938 at ./restic_repo

Please note that knowledge of your password is required to access
the repository. Losing your password means that your data is
irrecoverably lost.
```

查看生成的目录结构

```yaml
.
├── config
├── data
│   ├── 00
│   ├── 01
│   ├── 02
......
│   ├── fd
│   ├── fe
│   └── ff
├── index
├── keys
│   └── a1147718095f6ecc356caaae676932f78159a8332bf6ea36aed5ff4763205042
├── locks
└── snapshots

261 directories, 2 files
```

### data目录结构

此时生成了restic存储库的结构，从目录结构上可以很清楚的和设计原理对应。在data目录下，根据十六进制从00一直生成到ff个目录，用于blob的存储。

### config文件

由于config采用加密方式存储，无法直接查看，需要使用restic命令查看具体内容。

```yaml
restic cat -r restic_repo config
```

输出结果为

```yaml
repository 56f6f179 opened successfully, password is correct
{
  "version": 1,
  "id": "56f6f17938d86e6a4718d8d5a31ea6503a8bf24606e022c4ac2c2aae75ed52e2",
  "chunker_polynomial": "25fe60909e1433"
}
```

根据restic设计原理，初始化后版本为1，id为存储库的唯一ID，`chunker_polynomial`字段包含一个参数，用于将大文件分割成更小的块。

### keys目录

而文件部分，在初始化的结构上只存在keys下的文件和config两个文件。其中config文件为加密存储，而keys文件是明文存储，可以直接查看。

```yaml
python -mjson.tool restic_repo/keys/a1147718095
```

格式化输出内容为：

```yaml
{
    "created": "2022-03-23T10:31:42.819697576+08:00",
    "username": "root",
    "hostname": "ray-dev",
    "kdf": "scrypt",
    "N": 8192,
    "r": 8,
    "p": 11,
    "salt": "aziDQSzuuAet1SPMaEcgSLphDb9UyLZ8D/mry7QBMbnL60LTU/sjwXXEctGQNIATe6XeAy+Lgojcej7CV959Gg==",
    "data": "YCG8jYsnxaj2YyF5jc82q7mWPF6YsNNbhISXrsZGab7bsMlFe/dBPbnCUzyigac73cMFdirzrb2n9was+0wcGiTc3TIdQ9op5sbgaqAaCRHzR28zDjq/6b8PCl39rDm0fhwSPT+TrvJ8d9EX7FcnxIltJ2Xio4dsnHmr+2KxIyXhAyPaad4KEDKiTZEhtdw+dorofFB1aDKiTYBysRW1RA=="
}
```

当打开restic存储库时，会提示用户输入存储库密码。然后将其与 `scrypt`、密钥派生函数 (KDF) 和提供的参数（`N`、`r`、`p` 和`salt`）一起派生64个密钥字节。前32个字节用于加密密钥（用于 AES-256），最后32个字节用作消息验证密钥（用于 Poly1305-AES）。这最后32个字节被分成一个16字节的AES密钥“k”，然后是16个字节的密钥“r”。然后将密钥`r`屏蔽，与 Poly1305 一起使用（有关详细信息，请参阅论文）。

这些消息身份验证密钥（`k` 和 `r`）用于计算MAC，使用 JSON 中 `data`字段包含的字节（在删除 Base64 编码并且不包括最后32个字节之后）。如果密码不正确或密钥文件被篡改，则计算出的 MAC将与数据的最后 16 个字节不匹配，restic 会报错退出。否则，将使用从scrypt派生的加密密钥解密数据。这将生成一个JSON，其中包含此存储库的主加密和消息鉴权密钥（以 Base64 编码）。

```yaml
restic cat masterkey -r restic_repo
```

查看信息

```yaml
repository 56f6f179 opened successfully, password is correct
{
  "mac": {
    "k": "DLMpuMFKlvonh3rpul5yMQ==",
    "r": "DU06C/h5Jg+UAzoLuBsRDA=="
  },
  "encrypt": "H6tU0t5Sbo5hjux3kj9BapWtEqIo63UyyBhcbwBnP+M="
}
```

存储库中的所有数据都使用这些主密钥进行加密和验证。 对于加密，使用计数器模式下的 AES-256 算法。 对于消息认证，如上所述使用 Poly1305-AES。

存储库可以有多个不同的密码，每个密码都有一个密钥文件。 这样，无需重新加密所有数据即可更改密码。

## 小文件备份

为了测试方便，我们创建一个文本类型文件，该文件只包含一个字符，例如0。

```yaml
cat demo.txt
```

内容如下：

```yaml
0
```

查看文件的大小：

```yaml
stat demo.txt
```

输出为：

```yaml
File: ‘demo.txt’
  Size: 2         	Blocks: 8          IO Block: 4096   regular file
Device: 803h/2051d	Inode: 878940853   Links: 1
Access: (0644/-rw-r--r--)  Uid: (    0/    root)   Gid: (    0/    root)
Access: 2022-03-23 14:39:15.857514408 +0800
Modify: 2022-03-23 14:39:13.157444776 +0800
Change: 2022-03-23 14:39:13.157444776 +0800
 Birth: -
```

此时我们的目录结构为

```python
source_dir
└── demo.txt

0 directories, 1 file
```

我们使用restic进行备份

```yaml
restic -r restic_repo --verbose backup source_dir/demo.txt
```

输入正确的密码后备份成功

```yaml
repository 56f6f179 opened successfully, password is correct
lock repository
load index files
no parent snapshot found, will read all files
start scan on [source_dir/demo.txt]
start backup on [source_dir/demo.txt]
scan finished in 0.204s: 1 files, 2 B

Files:           1 new,     0 changed,     0 unmodified
Dirs:            1 new,     0 changed,     0 unmodified
Data Blobs:      1 new
Tree Blobs:      2 new
Added to the repo: 750 B

processed 1 files, 2 B in 0:00
snapshot 6ca52f2f saved
```

此时，我们回到restic存储库中来检查一下文件增加的情况，为了方便查看，我用git将初始化的信息进行了commit，这样就能看到本次备份后的文件变化情况。

```yaml
23 data/62/62f89d280ebdf875ef6f0d12e4d90d0e807a48506e60064ecb4d58a2c733177a
23 data/b3/b3346e2e87eee7a8d1a17052ce1d1d09784c072b949205f3c632dd503b867096
549 index/701f1ff24a647a51ebfadfaf973721075b62819408f3ac647e7a757e147de059
251 snapshots/6ca52f2f0978fbcfa16fdade23b2f20ba4f5a4a71882bb63cc0d4bec2970161a
```

我们来分析一下文件的变化情况，我们发现在data目录下增加了两个文件，而index和snapshots下分别增加了一个文件。

### 包（Packs）

很明显restic在存储文件时是根据文件名称前两位决定将文件存放在哪个目录下，比如62f89d280ebdf875ef6f0d12e4d90d0e807a48506e60064ecb4d58a2c733177a就存放在data/62下面。

在data目录下增加的两个文件就是restic的包，我们通过list命令可以查询存储库中包的列表

```python
restic -r restic_repo list packs
```

返回所有包的信息，与目录中的内容对应

```python
62f89d280ebdf875ef6f0d12e4d90d0e807a48506e60064ecb4d58a2c733177a
b3346e2e87eee7a8d1a17052ce1d1d09784c072b949205f3c632dd503b867096
```

虽然在cat中提供了查看pack内容，但是由于加密的原因，无法查看其中的内容，与直接执行cat返回内容一致

### 索引

查看index情况，和snapshots一样使用目录下的id进行查询

```python
restic -r restic_repo cat index 701f1ff24a647a51ebfadfaf973721075b62819408f3ac647e7a757e147de059 | python -mjson.tool
```

通过返回数据，我们可以看到packs与blobs的对应关系，通过返回，我们可以得知pack 62f89d280ebdf875ef6f0d12e4d90d0e807a48506e60064ecb4d58a2c733177a中包含的是实际数据，而另外一个pack包含的则是tree，即目录结构，虽然原理文档对于offset和length的计算有介绍，但是单从描述的方式上还不足以理解，需要对源码进行分析。

```python
{
    "packs": [
        {
            "id": "62f89d280ebdf875ef6f0d12e4d90d0e807a48506e60064ecb4d58a2c733177a",
            "blobs": [
                {
                    "id": "9a271f2a916b0b6ee6cecb2426f0b3206ef074578be55d9bc94f6f3fe3ab86aa",
                    "type": "data",
                    "offset": 0,
                    "length": 34
                }
            ]
        },
        {
            "id": "b3346e2e87eee7a8d1a17052ce1d1d09784c072b949205f3c632dd503b867096",
            "blobs": [
                {
                    "id": "5dbab6dedd6e621d742e9e2327e8e8da6198ed188321d68b6cc5ec1dc9ebafc2",
                    "type": "tree",
                    "offset": 405,
                    "length": 407
                },
                {
                    "id": "e8a97749d4bdd53506bd5979dec630d8606cc98e46ed6c07432242592382b322",
                    "type": "tree",
                    "offset": 0,
                    "length": 405
                }
            ]
        }
    ]
}
```

### Blob

我们进一步通过cat blob命令进行查询，我们先来查看数据类型

```python
restic -r restic_repo cat blob 9a271f2a916b0b6ee6cecb2426f0b3206ef074578be55d9bc94f6f3fe3ab86aa
```

返回的结果就是我们的实际内容

```python
0
```

我们再来查看tree类型

```python
restic -r restic_repo cat blob 5dbab6dedd6e621d742e9e2327e8e8da6198ed188321d68b6cc5ec1dc9ebafc2 | python -mjson.tool
```

此时，返回的是我们的第一级目录

```python
{
    "nodes": [
        {
            "name": "source_dir",
            "type": "dir",
            "mode": 2147484141,
            "mtime": "2022-03-23T14:39:13.157444776+08:00",
            "atime": "2022-03-23T14:39:13.157444776+08:00",
            "ctime": "2022-03-23T14:39:13.157444776+08:00",
            "uid": 0,
            "gid": 0,
            "user": "root",
            "group": "root",
            "inode": 878936120,
            "device_id": 2051,
            "content": null,
            "subtree": "e8a97749d4bdd53506bd5979dec630d8606cc98e46ed6c07432242592382b322"
        }
    ]
}
```

这里包含subtree，就是我们的子目录，我们进一步查询

```python
restic -r restic_repo cat blob e8a97749d4bdd53506bd5979dec630d8606cc98e46ed6c07432242592382b322 | python -mjson.tool
```

此时content的内容指向了数据blob 9a271f2a916b0b6ee6cecb2426f0b3206ef074578be55d9bc94f6f3fe3ab86aa，即我们的文件内容

```python
{
    "nodes": [
        {
            "name": "demo.txt",
            "type": "file",
            "mode": 420,
            "mtime": "2022-03-23T14:39:13.157444776+08:00",
            "atime": "2022-03-23T14:39:13.157444776+08:00",
            "ctime": "2022-03-23T14:39:13.157444776+08:00",
            "uid": 0,
            "gid": 0,
            "user": "root",
            "group": "root",
            "inode": 878940853,
            "device_id": 2051,
            "size": 2,
            "links": 1,
            "content": [
                "9a271f2a916b0b6ee6cecb2426f0b3206ef074578be55d9bc94f6f3fe3ab86aa"
            ]
        }
    ]
}
```

### 快照

再来查看一下snapshots的情况，直接使用snapshots下面的6ca52f2f0978fbcfa16fdade23b2f20ba4f5a4a71882bb63cc0d4bec2970161a进行查询

```python
restic -r restic_repo cat snapshot 6ca52f2f0978fbcfa16fdade23b2f20ba4f5a4a71882bb63cc0d4bec2970161a
```

从返回的数据看，snapshots指向了tree，而tree实质上就是最顶层的目录blob

```python
{
  "time": "2022-03-23T14:44:52.064414778+08:00",
  "tree": "5dbab6dedd6e621d742e9e2327e8e8da6198ed188321d68b6cc5ec1dc9ebafc2",
  "paths": [
    "/root/workspace/restic_test/source_dir/demo.txt"
  ],
  "hostname": "ray-dev",
  "username": "root"
}
```

从以上一个备份过程上，我们不难理解restic是如何进行的备份，那么我们再来测试一下，当达到restic对blob文件进行切割后，如何进行的存储。

## 大于8MB文件备份

根据原理文档描述，restic针对512 KB以下文件不切分，对于512KB到8MB的文件会保留原有大小，只有大于8MB才会切分，所以我们构建一个10MB文件，为了便于后续观察，我们按照递增方式从1向上增加，每一行为一个数字，即

```python
1
2
3
4
5
...
100
101
102
```

使用如下命令生成

```python
for i in {1..1450000}; do echo $i; done > 10mb_file.txt
```

直接对文件进行备份

```python
restic -r restic_repo --verbose backup source_dir/10mb_file.txt
```

输出详情为

```python
repository 56f6f179 opened successfully, password is correct
lock repository
load index files
no parent snapshot found, will read all files
start scan on [source_dir/10mb_file.txt]
start backup on [source_dir/10mb_file.txt]
scan finished in 0.206s: 1 files, 10.003 MiB

Files:           1 new,     0 changed,     0 unmodified
Dirs:            1 new,     0 changed,     0 unmodified
Data Blobs:      6 new
Tree Blobs:      2 new
Added to the repo: 10.004 MiB

processed 1 files, 10.003 MiB in 0:00
snapshot 9b965346 saved
```

通过输出可以看到：restic发现了一个新的文件，同时生成了6个新的数据Blobs，其中Tree Blobs为2个。通过观察restic repo内的文件变化情况，没有文件被修改，新增了6个文件（无修改文件）：

```python
1.3K ****data/34/347f0dd64113d6fd4cc47dc085405fbff605e942a7a18f92c77aab0bd480e069
3.0M data/ab/ab69b131e8262286a726f65b12462657259961a58ca7adbac480321e9a091565
3.0M data/be/be1e14a1ec2b41ea3e7d02ab985ff99e764a8f5de6c13aaac6ba9180f5ce81cd
4.2M data/be/be4b589501ccd0c6da460659faf5db477b541e6fb46bf5909af5927b03f19ca8
1.3K index/d40932add8acb5cfdd1deae551d59a85deab190b55a578243860fbf71aeb08d0
255 snapshots/9b9653468c30e7943f5d068c2a0210069eab03ca56d8b787c2883be06be2b116
```

从输出的结果上来看，本次生成的文件中snapshots文件与第一次备份一致，因为仅仅指向blob，所以文件大小没有显著增加，而index文件则比之前大了一倍，从549直接增加到1.3K。

### 索引

我们仍然通过命令，查看一下索引内的变化情况

```python
restic -r restic_repo cat index d40932add8acb5cfdd1deae551d59a85deab190b55a578243860fbf71aeb08d0 | jq
```

从生成的结果来看，与备份的标准输出相对应，index文件中总共包含了6个Blobs，其中四个为数据型，两个为目录型，我们直接对数据型blobs进行分析，看看restic是如何对文件进行的拆分。

```python
{
  "packs": [
    {
      "id": "be1e14a1ec2b41ea3e7d02ab985ff99e764a8f5de6c13aaac6ba9180f5ce81cd",
      "blobs": [
        {
          "id": "df59490249716895dd8b67dfe4af369f21dde033b51489ab4ccb3af5d064e65f",
          "type": "data",
          "offset": 0,
          "length": 708813
        },
        {
          "id": "6e837f4efe3effa79c1db760a83dc4a4ed9e8feb0a03d0c3358612248fd6bfd6",
          "type": "data",
          "offset": 708813,
          "length": 2344049
        }
      ]
    },
    {
      "id": "ab69b131e8262286a726f65b12462657259961a58ca7adbac480321e9a091565",
      "blobs": [
        {
          "id": "7d2fc5c4b2b7d183c94460eb6418a4b3a8898d769951281708cf7cf430f99dcd",
          "type": "data",
          "offset": 0,
          "length": 1482607
        },
        {
          "id": "d20d76c1a8e128707d094207f63d3e54bdd34c2f7dbb9bef19bfba9b408232cc",
          "type": "data",
          "offset": 1482607,
          "length": 1616191
        }
      ]
    },
    {
      "id": "be4b589501ccd0c6da460659faf5db477b541e6fb46bf5909af5927b03f19ca8",
      "blobs": [
        {
          "id": "2df049910612d58b07727115601f8a2bf6412ebc036d087a233d26d677290415",
          "type": "data",
          "offset": 1837173,
          "length": 2500255
        },
        {
          "id": "5e137b93f71fca42a5710a5b7e16c75d75c0c4b63b8bc8aab8f334a34c65b4ae",
          "type": "data",
          "offset": 0,
          "length": 1837173
        }
      ]
    },
    {
      "id": "347f0dd64113d6fd4cc47dc085405fbff605e942a7a18f92c77aab0bd480e069",
      "blobs": [
        {
          "id": "005bdcba00bd7ad8f1aa1f7db1aaa8b8539f1839061c40709a519de1b25e4b89",
          "type": "tree",
          "offset": 0,
          "length": 752
        },
        {
          "id": "067835a81002764d000d0e2dd36ea942d9ef176586d80a03878c373777608958",
          "type": "tree",
          "offset": 752,
          "length": 404
        }
      ]
    }
  ]
}
```

### Blob

我们分别对每个Blob进行cat查询，可以清楚看到每一个文件切分的位置，这里不再赘述，这里只列出切割的位置(根据上面输出索引的顺序)，及Blob对应的id。

| Blob ID | 文件起始行 | 结尾 |
| --- | --- | --- |
| df59490249716895dd8b67dfe4af369f21dde033b51489ab4ccb3af5d064e65f | 824978 | 92# |
| 6e837f4efe3effa79c1db760a83dc4a4ed9e8feb0a03d0c3358612248fd6bfd6 | 1 | 35073# |
| 7d2fc5c4b2b7d183c94460eb6418a4b3a8898d769951281708cf7cf430f99dcd | 181
613182 | 824977# |
| d20d76c1a8e128707d094207f63d3e54bdd34c2f7dbb9bef19bfba9b408232cc | 6232
926233 | 1137472
1# |
| 2df049910612d58b07727115601f8a2bf6412ebc036d087a233d26d677290415 | 137473
1137474 | 1450000 |
| 5e137b93f71fca42a5710a5b7e16c75d75c0c4b63b8bc8aab8f334a34c65b4ae | 2
350733 | 613180
613# |

从输出结果来看，我们不难看到restic切割的痕迹和每个Blob的关系，那么restic又是如何管理其中的顺序呢？答案就是最后subtree的contents字段。

最后，我们来通过查看子树的信息来观察contents的排列。

```python
restic -r restic_repo cat blob 005bdcba00bd7ad8f1aa1f7db1aaa8b8539f1839061c40709a519de1b25e4b89 | jq
```

通过观察contents的排列顺序恰好是我们上述表格内正确的顺序，这样在还原备份时，restic就可以对文件进行重组。

```python
{
  "nodes": [
    {
      "name": "10mb_file.txt",
      "type": "file",
      "mode": 420,
      "mtime": "2022-03-24T07:00:32.751188252+08:00",
      "atime": "2022-03-24T07:00:32.751188252+08:00",
      "ctime": "2022-03-24T07:01:26.38858041+08:00",
      "uid": 0,
      "gid": 0,
      "user": "root",
      "group": "root",
      "inode": 1377358062,
      "device_id": 2051,
      "size": 10488896,
      "links": 1,
      "content": [
        "6e837f4efe3effa79c1db760a83dc4a4ed9e8feb0a03d0c3358612248fd6bfd6",
        "5e137b93f71fca42a5710a5b7e16c75d75c0c4b63b8bc8aab8f334a34c65b4ae",
        "7d2fc5c4b2b7d183c94460eb6418a4b3a8898d769951281708cf7cf430f99dcd",
        "df59490249716895dd8b67dfe4af369f21dde033b51489ab4ccb3af5d064e65f",
        "d20d76c1a8e128707d094207f63d3e54bdd34c2f7dbb9bef19bfba9b408232cc",
        "2df049910612d58b07727115601f8a2bf6412ebc036d087a233d26d677290415"
      ]
    }
  ]
}
```

## 小文件修改后备份

在本次备份前，先来尝试修改小文件，我们将原有小文件的内容从0变为1，进行备份。

```yaml
restic -r restic_repo --verbose backup source_dir/demo.txt
```

此时restic发现有一个文件进行了改变，增加了一个Data Blob，增加了746字节

```yaml
repository 56f6f179 opened successfully, password is correct
lock repository
load index files
using parent snapshot 6ca52f2f
start scan on [source_dir/demo.txt]
start backup on [source_dir/demo.txt]
scan finished in 0.219s: 1 files, 2 B

Files:           0 new,     1 changed,     0 unmodified
Dirs:            0 new,     1 changed,     0 unmodified
Data Blobs:      1 new
Tree Blobs:      2 new
Added to the repo: 746 B

processed 1 files, 2 B in 0:00
snapshot 4e2aa2b0 saved
```

我们看一下存储库内的实际变化情况，虽然只修改了一个字符，但是restic存储库增加了1901个字节。

```yaml
107 data/30/30b15f86b4797676aa3b15b7b39094887fa5ebc23faeb0005a1de3db3cb5a99e
918 data/b8/b83c8903968a1754a4b935937c80588ca6415bc765b3ac67da3c1b5d99181545
549 index/35a11e5dfa5a4dd5a94ef7865993161e637c6e594b945b91a819c2cbbad5437f
327 snapshots/4e2aa2b01e6c253bff413e80c4838338342eb3cdf21adaee6399e0d196efef24
```

因为存储库的变化情况与上述相似，这里不再赘述。

## 大文件修改后备份

我们接下来看看如果是大文件变化，restic的同步情况，我们将我们构造的10MB文件的第一行进行从1修改为a。

```yaml
restic -r restic_repo --verbose backup source_dir/10mb_file.txt
```

输出内容，增加了一个1个新的数据blob，增加容量为2.236MB。

```yaml
repository 56f6f179 opened successfully, password is correct
lock repository
load index files
using parent snapshot 3568a27c
start scan on [source_dir/10mb_file.txt]
start backup on [source_dir/10mb_file.txt]
scan finished in 0.208s: 1 files, 10.003 MiB

Files:           0 new,     1 changed,     0 unmodified
Dirs:            0 new,     1 changed,     0 unmodified
Data Blobs:      1 new
Tree Blobs:      2 new
Added to the repo: 2.236 MiB

processed 1 files, 10.003 MiB in 0:00
snapshot 7505e3f0 saved
```

看一下存储库的实际变化情况，增加的总大小大约为2.3MB。

```yaml
2.3M data/b0/b0b147233fd6514fa14229231aa346bb321698e091fd5d2ca2aeb39590d96180
1.3K data/ed/edbf5390498ef9459e359eff4c03da82ee46c1f302a7ef6ec7410af25c825ae1
554 index/10001235dbd9f406ae7bd4030ad3feaf7dbdcddc32da05c125371a0780c578aa
332 snapshots/7505e3f009775ad74c00ca09aa57a854957d7f761a14e72ecd0d5fef9d7e9623
```

我们再将第100行，修改为aaa。我们看到在同一blob内，每次修改同步的大小是一样的。

```yaml
repository 56f6f179 opened successfully, password is correct
lock repository
load index files
using parent snapshot 7505e3f0
start scan on [source_dir/10mb_file.txt]
start backup on [source_dir/10mb_file.txt]
scan finished in 0.205s: 1 files, 10.003 MiB

Files:           0 new,     1 changed,     0 unmodified
Dirs:            0 new,     1 changed,     0 unmodified
Data Blobs:      1 new
Tree Blobs:      2 new
Added to the repo: 2.236 MiB

processed 1 files, 10.003 MiB in 0:00
snapshot 98f81417 saved
```

如果我们增加行数会发生什么呢？根据blob的分割记录，我们大概追加30000行到文件内，此时文件大小情况为

```yaml
File: ‘10mb_file.txt’
  Size: 10657790  	Blocks: 53248      IO Block: 4096   regular file
Device: 803h/2051d	Inode: 1377358062  Links: 1
Access: (0644/-rw-r--r--)  Uid: (    0/    root)   Gid: (    0/    root)
Access: 2022-03-24 15:05:36.102065592 +0800
Modify: 2022-03-24 15:11:54.259081906 +0800
Change: 2022-03-24 15:11:54.259081906 +0800
 Birth: -
```

本次同步后，可能是未达到边界值，所以同步的大小为2.5MB左右。

```yaml
repository 56f6f179 opened successfully, password is correct
lock repository
load index files
using parent snapshot 98f81417
start scan on [source_dir/10mb_file.txt]
start backup on [source_dir/10mb_file.txt]
scan finished in 0.214s: 1 files, 10.164 MiB

Files:           0 new,     1 changed,     0 unmodified
Dirs:            0 new,     1 changed,     0 unmodified
Data Blobs:      1 new
Tree Blobs:      2 new
Added to the repo: 2.547 MiB

processed 1 files, 10.164 MiB in 0:00
snapshot 84bb70fa saved
```

## 总结

通过以上使用测试，首先我们应该了解restic的目录管理逻辑

- index目录下的文件记录了每一次备份的完整组织结构，指向packs
- snapshots则直接指向了最顶层的blob
- data目录中的id是packs id，而packs中可能包含多个blob
- blob包含tree和data两种类型，blob记录了大量与文件有关的metadata信息