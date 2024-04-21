# 运行Python

## 解释器输入参数

解释器读取命令行参数，把脚本名与其他参数转化为字符串列表存到 sys 模块的 argv 变量里。执行 import sys，可以导入这个模块，并访问该列表。该列表最少有一个元素；未给定输入参数时，sys.argv[0] 是空字符串。给定脚本名是 '-' （标准输入）时，sys.argv[0] 是 '-'。使用 -c command 时，sys.argv[0] 是 '-c'。如果使用选项 -m module，sys.argv[0] 就是包含目录的模块全名。解释器不处理 -c command 或 -m module 之后的选项，而是直接留在 sys.argv 中由命令或模块来处理。

```bash
python -m http.server 8080
```

```bash
python hello.py

// #!/usr/bin/env python3
chmod +x hello.py
./hello.py
```

编码声明

```py
#!/usr/bin/env python
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

## 包管理工具

- pip

```bash
pip install package=1.5
pip install --upgrade package
pip install -U package
pip uninstall package
pip show package
```

- conda 管理和部署应用、环境和包的工具

## 从源码安装包

```bash
python setup.py install
```

## Jupyter

创建和共享实时代码

```bash
jupyter notebook
```

## 虚拟环境工具

- [virtualenv](https://virtualenv.pypa.io/en/latest/)
- [venv](https://docs.python.org/zh-cn/3/library/venv.html)

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
