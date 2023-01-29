---
title: 8.5 Go语言中数据库操作
date: 2023-01-05T20:01:50+08:00
slug: "old-sun-learning-go-notes-8-5"
author: 老孙正经胡说
tags:
  - Linux
  - Go
categories:
  - Go
draft: false
---

数据库是应用开发中必须要掌握的技巧，通常在数据库开发过程中，会有两种不同的方式：

- 直接使用SQL语句，这种方式下，直接编写SQL，简单直观，但是可维护性较差，同时对于数据库依赖性比较强
- 使用ORM方式，将数据库映射到对象上，方便操作，而且可以跨数据库使用，也是开发框架中最常用的使用方式；同时，采用Migration管理数据库Schema，形成版本控制

以下代码及部分解释由chatGPT生成

## 原生SQL方式

这段代码实现了一个 Go 程序，它使用了标准库中的 "database/sql" 包来连接 MySQL 数据库并查询表。

```go
package main

import (
    "database/sql"
    "fmt"

    _ "github.com/go-sql-driver/mysql"
)

func main() {
    db, err := sql.Open("mysql", "username:password@tcp(host:port)/dbname")
    if err != nil {
        panic(err.Error())
    }
    defer db.Close()

    rows, err := db.Query("SELECT * FROM table_name")
    if err != nil {
        panic(err.Error())
    }
    defer rows.Close()

    columns, err := rows.Columns()
    if err != nil {
        panic(err.Error())
    }

    values := make([]sql.RawBytes, len(columns))
    scanArgs := make([]interface{}, len(values))
    for i := range values {
        scanArgs[i] = &values[i]
    }

    for rows.Next() {
        err = rows.Scan(scanArgs...)
        if err != nil {
            panic(err.Error())
        }

        var value string
        for i, col := range values {
            if col == nil {
                value = "NULL"
            } else {
                value = string(col)
            }
            fmt.Println(columns[i], ": ", value)
        }
        fmt.Println("-----------------------------------")
    }
    if err = rows.Err(); err != nil {
        panic(err.Error())
    }
}
```

首先，通过调用 sql.Open() 函数并传入 "mysql" 作为驱动名称和一个连接字符串来打开数据库连接。如果打开连接失败，程序会 panic。

接下来，使用 db.Query() 函数执行 SQL 查询语句，并将结果保存到变量 rows 中。如果查询失败，程序会 panic。

之后，调用 rows.Columns() 函数获取表的列名，并在循环中调用 rows.Next() 函数来遍历查询结果。在每次循环中，调用 rows.Scan() 函数将当前行的数据读取到 values 数组中。然后，遍历 values 数组，并将每列的值输出到控制台。

最后，使用 rows.Err() 函数检查是否有任何错误，并在有错误时 panic。

注意：

- 需要先安装 github.com/go-sql-driver/mysql
- 连接字符串需要替换成自己的连接信息
- 查询语句需要替换成自己的表名

## ORM方式

ORM (Object-Relational Mapping) 是一种将关系数据库中的数据映射到对象上的技术。在 Go 语言中，可以使用第三方库 "gorm" 来实现 ORM 数据库访问，该库也是Go语言使用较为广泛的ORM库。

下面是一个简单的例子，它使用 gorm 库来连接 MySQL 数据库并查询表：

```go
package main

import (
    "fmt"

    "github.com/jinzhu/gorm"
    _ "github.com/jinzhu/gorm/dialects/mysql"
)

type Product struct {
    gorm.Model
    Code  string
    Price uint
}

func main() {
    db, err := gorm.Open("mysql", "username:password@tcp(host:port)/dbname?charset=utf8&parseTime=True&loc=Local")
    if err != nil {
        panic("failed to connect database")
    }
    defer db.Close()

    // Migrate the schema
    db.AutoMigrate(&Product{})

    // Create
    db.Create(&Product{Code: "L1212", Price: 1000})

    // Read
    var product Product
    db.First(&product, 1)                   // find product with id 1
    db.First(&product, "code = ?", "L1212") // find product with code L1212

    // Update - update product's price to 2000
    db.Model(&product).Update("Price", 2000)

    // Delete - delete product
    db.Delete(&product)
}
```

该示例定义了一个名为 Product 的结构体，其中包含了三个字段：Code、Price 和 gorm.Model。gorm.Model 是 GORM 提供的一个结构体，包含了一些预定义字段，如 ID、CreatedAt、UpdatedAt 等。

程序首先连接到 MySQL 数据库，然后使用 AutoMigrate 函数自动创建 Product 表，如果表已经存在，则修改表结构。

接下来使用 Create 函数向 Product 表中插入一条数据。使用 First 函数查询表中的第一条记录。

之后，使用 Model 函数更新该条记录的价格，最后使用 Delete 函数删除该条记录。

注意：
- 需要先安装 github.com/jinzhu/gorm
- 连接字符串需要替换成自己的连接信息