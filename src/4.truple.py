t1 = 1,2,3
print(t1)
# 元组的切片依然是元组
print(t1[1:])
tt = t1
print(tt)

t2 = (1,)
n = (1)
print(t2, n)

t3 = 3,
print(t3)

# 不支持索引赋值
# t3[0] = 6
# print(t3)

t4 = t3*3
print(t4)

t5 = (2)
print(3*t5)

t6 = tuple([2,3,6])
print(t6)

t7 = tuple(t4)
print(t7, t4 == t7)
