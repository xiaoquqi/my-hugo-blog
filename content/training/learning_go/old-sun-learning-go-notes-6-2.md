---
title: 6.2 如何理解Go语言中的接口
date: 2022-11-23T08:25:56+08:00
slug: "old-sun-learning-go-notes-6-2"
author: 老孙正经胡说
tags:
  - Linux
  - Go
categories:
  - Go
draft: false
weight: 36
---

## Go语言中的接口

- 接口有点像是定义，描述了必须具备的方法集合。通过观察接口的代码样例中，Go语言中的接口并不是非常复杂，但是为代码重用提供了高效的实现方式。
- 不同于Java中显式的接口定义，Go中的接口是隐式定义，另外Java中的接口可以定义属性，而Go中的接口则只包含了方法的定义

```java
// Interface
interface Animal {
  public String name = "animal";
  public void animalSound(); // interface method (does not have a body)
  public void sleep(); // interface method (does not have a body)
}

// Pig "implements" the Animal interface
class Pig implements Animal {
  public void animalSound() {
    // The body of animalSound() is provided here
    System.out.println("The pig says: wee wee");
  }
  public void sleep() {
    // The body of sleep() is provided here
    System.out.println("Zzz");
  }
}

class Main {
  public static void main(String[] args) {
    Pig myPig = new Pig();  // Create a Pig object
    myPig.animalSound();
    myPig.sleep();
  }
}
```

如果修改为Go语言实现，则为

```go
type Animal interface {
    animalSound();
    sleep();
}

type Pig struct {
    name string
}

func (p Pig) animalSound() {
    fmt.Println("The pig says: wee wee")
}

func (p Pig) sleep() {
    fmt.Println("Zzz")
}

func main() {
    p := Pig{"pig"}
    p.animalSound()
    p.sleep()
}
```

## 与类、继承之间的关系

- stuct和inteface构建了Go语言中的面向对象
   - struct相当于其他语言的类，但是并不完全等同，所以不要完全套用传统类的思想来进行开发。在结构体的学习中，我们知道Go语言中并没有像其他语言提供类(Class)的定义方式，而是通过结构体及函数的Reciever间接的使用。本质上，Go中的类就是属性和方法的组合。
   - interface相当于实现了动态语言中的多态(Duck Typing)
      - Duck Typing是动态类型中常用的一种多态方式，为了便于理解，这里重温了Python Duck Typing的实现方法。
      - 多态的引入提高了代码的灵活度，有些变量类型可以在编译或运行时决定
- Go语言里并没有设计诸如虚函数、纯虚函数、继承、多重继承的概念，但是仍然通过struct和interface实现类似继承和多态的特性，使代码能够可重用且优雅，降低传统面向对象语言开发的复杂程度。

## Python中的Duck Typing

> “当看到一只鸟走起来像鸭子、游泳起来像鸭子、叫起来也像鸭子，那么这只鸟就可以被称为鸭子。”
> 鸭子类型（英语：duck typing）在程序设计中是动态类型的一种风格。在这种风格中，一个对象有效的语义，不是由继承自特定的类或实现特定的接口，而是由"当前方法和属性的集合"决定。这个概念的名字来源于由詹姆斯·惠特科姆·莱利提出的鸭子测试。
> 简单来说，不关注鸭子，而关注是否会呱呱叫。
> 在常规类型中，我们能否在一个特定场景中使用某个对象取决于这个对象的类型，而在鸭子类型中，则取决于这个对象是否具有某种属性或者方法——即只要具备特定的属性或方法，能通过鸭子测试，就可以使用。

这不禁让我让我想到两句谚语：狗拿耗子多管闲事和黑猫白猫能抓到耗子就是好猫。显然，这里要表达的意思和Duck Typing类似：只要够能抓住耗子，狗也可以是只猫。

不同于强类型语言，在实际使用Duck Typing时，只需要对象拥有这个方法即可调用，而不需要关心这些对象是否为同一类或继承类，比如Python内置的len()方法，本质上是在类中实现了__len__方法。

```python
class DuckTypingDemo:

    def __len__(self):
        return 4096

duck_typing = DuckTypingDemo()
print("DuckTypingDemo len =", len(duck_typing))
# DuckTypingDemo len = 4096

my_str = "hello, world"
print("String len =", len(my_str))
# String len = 12

my_list = [1, 2, 3, 4, 5, 6]
print("List len =", len(my_list))
# List len = 6

my_dict = {"one" : 1, "two" : 2}
print("Dict len =", len(my_dict))
# Dict len = 2

try:
    my_int = 6
    print("int class =", my_int.__class__.__name__)
    print("int len =", len(my_int))
except Exception as e:
    print("Failed Reason:", e)
# int class = int
# Failed Reason: object of type 'int' has no len()
```

当我们为自定义类DuckTypingDemo定义了__len__方法时，就可以调用len方法，同理在内置函数中，对于string, list和dict也可以通过len获取相应类型的长度。

而对于没有定义__len__的int类型来说，就无法使用len方法获取其长度了。当然我们可以通过继承int，实现其__len__后，就可以使用len()方法了。

```python
class IntWithLen(int):

    def __len__(self):
        return 1024

i = IntWithLen()
print("Int with length:", len(i))
# Int with length: 1024
```

## 命名规范

- 根据惯例，接口名称后缀一般为er，像Reader, Writer, Formatter等
- 避免混淆，例如：Read、Write、Close、Flush、String
- 如果你定义的内容确实与这些类型相同，需要使用相同的名称和签名，例如字符转换方法是String而不是ToString