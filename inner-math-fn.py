"""
Python中内置的数学函数
"""

# 取绝对值
print("%d\t%.2f" % (abs(-3), abs(-2.34)))

# 取数列中的最大值和最小值
print("%d\t%d" % (max(-2, 3, 1, 6), min(-2, 3, 1, 6)))

# 计算乘方
print("%d\t%.2f\t%.2f" % (pow(2, 5), pow(2.1, 1.3), (2.1 ** 1.3)))

# rand(x) 返回最接近x的整数,如果x与两个数接近程度相同则返回偶数的那个
print("%d\t%d" % (round(2.6), round(-3.6)))

# rand(x, n) 返回保留n位小数
test1, test2 = round(2.634, 2), round(-3.63326, 2)
print("%.2f\t%.2f\t%.2f" % (test1, test2, round(-3.63326, 2)))
