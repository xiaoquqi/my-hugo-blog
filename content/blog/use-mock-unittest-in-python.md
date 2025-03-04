---
title: 使用Mock思想进行单元测试Python篇
date: 2022-12-03T08:09:28+08:00
slug: "use-mock-unittest-in-python"
author: 老孙正经胡说
tags:
  - Linux
  - Python
  - test
categories:
  - Python
draft: false
---

## 为什么使用Mock进行单元测试？

从功能开发完成的定义来看，至少包括：代码本身、文档及单元测试。而往往在实际开发中，由于需求的不停的变化，导致文档及单元测试是开发过程中直接被忽略的内容。反观优秀的开源项目，在全球几千人合作开发的大项目中，仍然能保持代码的高质量，这其中文档和单元测试是必不可少的环节之一。

不同于完整性测试或者冒烟测试，单元测试是为了证明你代码逻辑的正确性，所以必须由开发人员亲自完成，类似在证明“你爸是你爸”。单元测试能够屏蔽80%以上的低级错误，以及在协作开发过程中出现修改公共逻辑造成的潜在风险。一个伴随着单元测试出现的指标叫做覆盖率，即单元测试覆盖的代码行数，简单来说单元测试有没有覆盖代码执行过程中的每一行。每一个项目的代码覆盖率要求不同，需要寻找一个平衡点，过高的覆盖率会导致研发成本升高，过低的覆盖率又没有起到单元测试的目的。

另外一个在单元测试经常出现的困扰点是环境依赖的问题，比如我们代码实现中需要调用外部某一系统的接口，那么我们在做单元测试时，是不是真的要搭建一套系统来满足我们测试的需要呢？显然是不可能的。这就和我们今天主题相关了，使用Mock思想进行单元测试。简而言之，不具备的条件使用Mock来进行模拟。还是接口调用的例子，我们在进行单元测试的时候，重点要测试时我们的逻辑，并不是那个接口的实现，我们关注的只是那个接口的正常或异常的返回，所以当我们的程序调用那个接口时，我们只需要Mock那个接口的返回即可，这样就可以专注于我们自身的逻辑测试了。

## 示例一：测试文件删除

本文中的一些示例来自：[https://www.toptal.com/python/an-introduction-to-mocking-in-python](https://www.toptal.com/python/an-introduction-to-mocking-in-python)
我们从例子来看一下如果利用Mock思想进行单元测试。先看看代码实现部分：

```python
#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os

def rm(filename):
    os.remove(filename)
```

按照传统的思想进行测试，一定会构建一个文件，然后调用函数进行删除后，判断文件是否存在。但是注意，这种测试方法其实不是在测试你的函数，而是在测试os.remove。这种思想并不是不可以，但是严重依赖于环境，如果我们现在测试对象是一个数据库或者上面提到的接口，我们构建单元测试的成本就非常高，甚至无法实现了。

我们还是来看一下基于这种思想的测试用例实现：

- 实现在setUp中，随机新建了一个文件
- 在test_rm中，调用我们的方法进行删除
- 最终在assert中判断文件是否存在，如果存在，则抛出Failed to remove this file

```python
#!/usr/bin/env python
# -*- coding: utf-8 -*-

from mymodule import rm

import os.path
import tempfile
import unittest

class RmTestCase(unittest.TestCase):

    tmpfilepath = os.path.join(tempfile.gettempdir(), "tmp-testfile")

    def setUp(self):
        with open(self.tmpfilepath, "wb") as f:
            f.write("Delete me!")
        
    def test_rm(self):
        # remove the file
        rm(self.tmpfilepath)
        # test that it was actually removed
        self.assertFalse(os.path.isfile(self.tmpfilepath), "Failed to remove the file.")
```

我们使用Mock思想来重新分析一下：在代码中，我们实现其实是接受一个变量后，将变量传给os.remove，从Mock思想来看，我们只需要证明我们参数正确的传给了os.remove，并且os.remove是用我们这个参数执行的，这其实才是我们真正的逻辑，来看一下基于Mock是想的测试用例：

- 使用Mock时，我们不再需要依赖外部环境
- 我们需要使用unittest中的mock.patch，即允许我们对某些模块的返回值进行模拟，比如这里我们对我们依赖的mymodule.os进行了Mock
- 在测试用例中，当调用rm时，rm会使用我们Mock好的库进行调用，并不会触发真正的删除
- 而在断言中，我们只需要证明os库被调用，且参数与我们传入一致即证明测试通过
- 当然对于各种异常情况，我们也可以通过mock进行模拟，来捕获相关的异常是否符合我们的预期，在后面的示例中我们会看到

```python
#!/usr/bin/env python
# -*- coding: utf-8 -*-

from mymodule import rm

import mock
import unittest

class RmTestCase(unittest.TestCase):
    
    @mock.patch('mymodule.os')
    def test_rm(self, mock_os):
        rm("any path")
        # test that rm called os.remove with the right parameters
        mock_os.remove.assert_called_with("any path")
```

这里需要注意的一点是我们mock的对象是mymodule.os并不是os，这与Python运行机制有关，在运行时mymodule会导入模块中的独立范围内，所以如果单纯mock os是无法实现上述测试的。

## 示例二：测试校验验证

在这个示例中，我们对源代码进行部分修改，增加对path存在的校验，我们在执行os.remove前，首先判断传入的参数是否为文件类型。

```python
#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import os.path

def rm(filename):
    if os.path.isfile(filename):
        os.remove(filename)
```

我们直接使用Mock方式进行测试，测试用例增加的部分：

- 增加对mymodule.os.path进行Mock，Mock的目的是控制其返回值
- 通过return_value来控制isfile的返回值为False
   - mock_path.isfile.return_value = False
   - 我们的测试的第一种情况是：当参数不是文件时，os.remove不会被调用
- 再次通过return_value来控制isfile的返回值为True
   - mock_path.isfile.return_value = True
   - 我们测试的第二种情况是：当参数是文件时，os.remove会被调用同时使用参数

```python
#!/usr/bin/env python
# -*- coding: utf-8 -*-

from mymodule import rm

import mock
import unittest

class RmTestCase(unittest.TestCase):
    
    @mock.patch('mymodule.os.path')
    @mock.patch('mymodule.os')
    def test_rm(self, mock_os, mock_path):
        # set up the mock
        mock_path.isfile.return_value = False
        
        rm("any path")
        
        # test that the remove call was NOT called.
        self.assertFalse(mock_os.remove.called, "Failed to not remove the file if not present.")
        
        # make the file 'exist'
        mock_path.isfile.return_value = True
        
        rm("any path")
        
        mock_os.remove.assert_called_with("any path")
```

## 示例三：对类进行测试

首先我们将现有代码改造成类的方式，我们增加了RemovalService类，将原有方法变为类的方法

```python
#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import os.path

class RemovalService(object):
    """A service for removing objects from the filesystem."""

    def rm(self, filename):
        if os.path.isfile(filename):
            os.remove(filename)
```

我们再次进行测试时，需要将类实例化后，在进行相关测试，这个测试与上面对单独函数的测试并没有太大差别

```python
#!/usr/bin/env python
# -*- coding: utf-8 -*-

from mymodule import RemovalService

import mock
import unittest

class RemovalServiceTestCase(unittest.TestCase):
    
    @mock.patch('mymodule.os.path')
    @mock.patch('mymodule.os')
    def test_rm(self, mock_os, mock_path):
        # instantiate our service
        reference = RemovalService()
        
        # set up the mock
        mock_path.isfile.return_value = False
        
        reference.rm("any path")
        
        # test that the remove call was NOT called.
        self.assertFalse(mock_os.remove.called, "Failed to not remove the file if not present.")
        
        # make the file 'exist'
        mock_path.isfile.return_value = True
        
        reference.rm("any path")
        
        mock_os.remove.assert_called_with("any path")
```

我们再次对代码进行改造，实现两个类。

- 我们保留了刚才构建了RemovalService，同时新增了一个UploadService使用RemovalService的rm方法

```python
#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import os.path

class RemovalService(object):
    """A service for removing objects from the filesystem."""

    def rm(self, filename):
        if os.path.isfile(filename):
            os.remove(filename)
            

class UploadService(object):

    def __init__(self, removal_service):
        self.removal_service = removal_service
        
    def upload_complete(self, filename):
        self.removal_service.rm(filename)
```

根据刚刚我们强调的测试思想，此时再对UploadService进行测试时，我们无须再关注rm实现及测试，而是要关注upload_complete方法本身的测试，这里有两种Mock测试方法：

- 对RemovalService.rm进行Mock
- 在UploadService中完全Mock一个RemovalService

### Mock RemovalService.rm

在这种测试方式下，测试方法类似我们之前的测试，只要保证我们的UploadService中是否被正确调用及参数传递是否正确即可。

```python
#!/usr/bin/env python
# -*- coding: utf-8 -*-

from mymodule import RemovalService, UploadService

import mock
import unittest

class RemovalServiceTestCase(unittest.TestCase):
    
    @mock.patch('mymodule.os.path')
    @mock.patch('mymodule.os')
    def test_rm(self, mock_os, mock_path):
        # instantiate our service
        reference = RemovalService()
        
        # set up the mock
        mock_path.isfile.return_value = False
        
        reference.rm("any path")
        
        # test that the remove call was NOT called.
        self.assertFalse(mock_os.remove.called, "Failed to not remove the file if not present.")
        
        # make the file 'exist'
        mock_path.isfile.return_value = True
        
        reference.rm("any path")
        
        mock_os.remove.assert_called_with("any path")
      
      
class UploadServiceTestCase(unittest.TestCase):

    @mock.patch.object(RemovalService, 'rm')
    def test_upload_complete(self, mock_rm):
        # build our dependencies
        removal_service = RemovalService()
        reference = UploadService(removal_service)
        
        # call upload_complete, which should, in turn, call `rm`:
        reference.upload_complete("my uploaded file")
        
        # check that it called the rm method of any RemovalService
        mock_rm.assert_called_with("my uploaded file")
        
        # check that it called the rm method of _our_ removal_service
        removal_service.rm.assert_called_with("my uploaded file")
```

### Mock UploadService

在本示例中，我们直接对UploadService进行自动Mock：

- 使用mock.create_autospec(RemovalService)
- 测试的case仍然是对调用参数及调用过程进行检验

```python
#!/usr/bin/env python
# -*- coding: utf-8 -*-

from mymodule import RemovalService, UploadService

import mock
import unittest

class RemovalServiceTestCase(unittest.TestCase):
    
    @mock.patch('mymodule.os.path')
    @mock.patch('mymodule.os')
    def test_rm(self, mock_os, mock_path):
        # instantiate our service
        reference = RemovalService()
        
        # set up the mock
        mock_path.isfile.return_value = False
        
        reference.rm("any path")
        
        # test that the remove call was NOT called.
        self.assertFalse(mock_os.remove.called, "Failed to not remove the file if not present.")
        
        # make the file 'exist'
        mock_path.isfile.return_value = True
        
        reference.rm("any path")
        
        mock_os.remove.assert_called_with("any path")
      
      
class UploadServiceTestCase(unittest.TestCase):

    def test_upload_complete(self):
        # build our dependencies
        mock_removal_service = mock.create_autospec(RemovalService)
        reference = UploadService(mock_removal_service)
        
        # call upload_complete, which should, in turn, call `rm`:
        reference.upload_complete("my uploaded file")
        
        # test that it called the rm method
        mock_removal_service.rm.assert_called_with("my uploaded file")
```

mock.create_autospec 方法为所提供的类创建一个功能等效的实例。如果在使用过程中，例如：传递参数错误发生，则会导致异常。这在代码重构时，会帮助我们检查到相关调整可能导致的异常。

## Mock常用方法

### Mock Patch顺序

Mock的顺序与使用顺序相反，例如下面的例子中：

```python
    @mock.patch('mymodule.sys')
    @mock.patch('mymodule.os')
    @mock.patch('mymodule.os.path')
    def test_something(self, mock_os_path, mock_os, mock_sys):
        pass
```

我们看到在函数参数中，顺序与mock的顺序相反，这与Python自身机制有关

```python
patch_sys(patch_os(patch_os_path(test_something)))
```

### Mock和MagicMock

Mock和MagicMock都可以模拟对象所有属性和方法，并且灵活设定存储和返回的内容。

```python
from unittest.mock import MagicMock

thing = ProductionClass()
thing.method = MagicMock(return_value=3)
thing.method(3, 4, 5, key='value')

thing.method.assert_called_with(3, 4, 5, key='value')
```

使用mock side_effect模拟异常

```python
mock = Mock(side_effect=KeyError('foo'))
mock()
Traceback (most recent call last):
 ...
KeyError: 'foo'
```

```python
values = {'a': 1, 'b': 2, 'c': 3}
def side_effect(arg):
    return values[arg]

mock.side_effect = side_effect
mock('a'), mock('b'), mock('c')
(1, 2, 3)
mock.side_effect = [5, 4, 3, 2, 1]
mock(), mock(), mock()
(5, 4, 3)
```

## Mock API请求

使用各种SDK调用不同平台的API接口，是基于云开发的时候常用的形态。此时，Mock测试对于这种形态的调用是绝佳的测试方案，特别是一些异常情况，非常容易模拟。
该示例是调用Facebook API发送消息的接口实例：

- 在本示例中，我们封装了一个类
- post_message可以发送一条动态，我们需要对此进行测试

```python
import facebook

class SimpleFacebook(object):
    
    def __init__(self, oauth_token):
        self.graph = facebook.GraphAPI(oauth_token)

    def post_message(self, message):
        """Posts a message to the Facebook wall."""
        self.graph.put_object("me", "feed", message=message)
```

来看一下这个测试用例：

- 通过mock.patch.object对facbook.GraphAPI中的put_object进行Mock
- 用simple_facebook构建一个Mock Token，用于类的初始化
- 最后对Mock后进行调用及传参的校验

```python
import facebook
import simple_facebook
import mock
import unittest

class SimpleFacebookTestCase(unittest.TestCase):
    
    @mock.patch.object(facebook.GraphAPI, 'put_object', autospec=True)
    def test_post_message(self, mock_put_object):
        sf = simple_facebook.SimpleFacebook("fake oauth token")
        sf.post_message("Hello World!")

        # verify
        mock_put_object.assert_called_with(message="Hello World!")
```

## 参考链接

- Python unittest: [https://docs.python.org/3/library/unittest.mock.html#unittest.mock.Mock.assert_called_with](https://docs.python.org/3/library/unittest.mock.html#unittest.mock.Mock.assert_called_with)