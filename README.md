# Python

## 基本概念

简单易用
提供了大量高级的数据结构
支持模块化,提供了大量内置模块
解释型语言，不需要编译和链接，可以节省大量开发时间
支撑C/C++扩展

- 高级数据类型允许在单一语句中表述复杂操作；
- 使用缩进，而不是括号实现代码块分组；
- 无需预声明变量或参数。

## Python语言风格

- 使用`4`个空格来缩进
- 永远不要混用空格和制表符
- 在函数之间空一行
- 在类之间空两行
- 字典，列表，元组以及参数列表中，在 `,` 后添加一个空格。对于字典，`:` 后面也添加一个空格
- 在赋值运算符和比较运算符周围要有空格（参数列表中除外），但是括号里侧不加空格

## 解释器

```bash
python --version
python -c command [arg] ...
python -m module [arg] ...
-i // 交互式运行
```

```bash
ipython
jupyter notebook
_ # 表示结果
# 查看函数签名
function?
```

## Anaconda

[Anaconda](https://www.anaconda.com/download)
[Miniconda](https://docs.anaconda.com/free/miniconda/index.html)

```bash
curl https://repo.anaconda.com/miniconda/Miniconda3-latest-MacOSX-arm64.sh -o ~/miniconda3/miniconda.sh
bash ~/miniconda3/miniconda.sh -b -u -p ~/miniconda3
rm -rf ~/miniconda3/miniconda.sh
~/miniconda3/bin/conda init bash
~/miniconda3/bin/conda init zsh
pip install ipython scipy numpy pandas matplotlib jupyter
which python
which pip
which conda

pip list

py -m pip --version
py -m pip install --user -U pip
py -m pip install -U virtualenv
```

## Python环境管理

```bash
# 关闭环境
conda deactivate
# 激活环境
conda activate
```

```bash
cd $ML_PATH
# 创建环境
python3 -m virtualenv ml-action
# 激活环境
source ml-action/bin/activate
```