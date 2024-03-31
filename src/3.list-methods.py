"""
lst = [1,2,3]
print(lst)
# 只能单个追加
lst.append(4)
print(lst)

# 清空列表
lst[:] = []
# lst.clear()
print(lst)

a = [1,2,3]
b = a
b[1:1] = [4,5,6]
print(a)

# 复制列表
l = [[1,2],2,3]
ll = l.copy()
ll.append(4)
ll[0][0] = 2
print(ll)
print(l)

lll = l[:]
print(lll);

# 统计元素出现频次
l4 = list(l)
l4.append(2)
print(l4)
print(l4.count(2))
"""

# 扩展列表
a = [1,2,3]
b = [2,3,4,5]
# a.extend(b)
# a = a + b
# a[len(a):] = b
# 拼接列表
# c = a + b
a[len(a):] = b
print(a)
print(b)
# print(c)

# 查找元素
knight = ['we', 'are', 'the', 'knight', 'who', 'say', 'hi']
print(knight.index('hi'))
index = knight.index('who')
print(knight[index], index)
# print(knight.index('hello'))

# 插入元素
numbers = [1,2,3,4,5,6]
numbers.insert(7,'hi')
# numbers.insert(1,'bar')
numbers[1:1] = ['bar']
print(numbers)

# 删除元素
x = [1,2,3]
y = x.pop() # 返回被删除的元素
z = x.pop(1)
print(x, y, z)

x = ['to', 'be', 'or', 'not', 'to', 'be']
# 删除第一次找到的元素,无返回值
y = x.remove('be')
# x.remove('are')
print(x, y)

x = [2, 1, 3, 6]
x2 = list(reversed(x))
print(x2)
# x.reverse()
# x.sort()
y = sorted(x)
print(x)
print(y)

x = ['aeejjdd', 'avjjd', 'kkdd', 'ss', 'jsksksksfse']
x.sort(key=len);
print(x)
x.sort(key=len, reverse=True)
print(x)


