# 运行Python

```bash
python hello.py

// #!/usr/bin/env python3
chmod +x hello.py
./hello.py
```

指定源码编码

```py
# -*- encoding name -*-
# name => utf-8(默认) latin-1
```

## 清屏

```py
import os
os.system('clear') // mac and linux
os.system('cls') // windos
os.system('reset') // linux
os.system("printf'\033c'") // linux

```

## 查看帮助信息

help([object])

## 数据结构

数据结构是以某种方式组合起来的数据元素集合,可其视容器，是可以包含其他对象的对象。
主要的容器有序列、映射和集合。

序列 通过位置索引访问序列中的元素，负索引表示序列末尾元素的位置
常用的序列有字符串、列表、元组,列表支持修改而元组不能修改。
内置函数返回的都是元组，几乎所有情况都可以使用列表代替元组，但将元组用作字典键时不能用列表代替，因为字典的键不允许修改。

通用序列操作

- 索引
- 切片
- 相加
- 相乘
- 迭代
- 成员检查
