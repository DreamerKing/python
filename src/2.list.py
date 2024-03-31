"""
king = ['king', 20]
john = ['john', 32]
employee = [king, john]
print(employee)
print(employee[1])
print(employee[-2])

hello = "hello world"
print(hello[2], hello[-4], '你好'[1])

"""
# fourth = input('Year:\n')[-1]
# print(fourth)
"""

# 切片 :分隔 start:end:step 不包含end

tag = 'https://juejin.cn/post/6844904068888920071'
print(tag[8 : 17])

numbers = [0,1,2,3,4,5,6,7,8,9]
print(numbers[2:6])
print(numbers[6:6])
print(numbers[3: -2])
print(numbers[:-2])
print(numbers[5:]) # 序列前n个元素
print(numbers[-3:]) # 序列后n个元素
print(numbers[-3:0])
print(numbers[:]) # 复制序列

print(numbers[1:10:2])
print(numbers[::4])

# 步长为负的情况
print(numbers[8:3:-2]) # 步长可以为负值，表示从右向左提取元素
print(numbers[3:8:-2])
# print(numbers[2:6:0]) # 步长不能为0
print(numbers[:3:-2])
print(numbers[8::-3])

a = [1,2,3]
b = [4,5]
print(a + b)
# print(a + 'hello')
print(a + ['hello'])

print([23]*3)
print([None]*5)

permission = 'rw'
print('w' in permission)
print('x' in permission)

users = ['mlh', 'foo', 'bar']
input('Enter your user name: ') in users
subject = '$$$ get rich now!!! $$$'
print('$$$' in subject)

"""

numbers = [100, 123, 99, 89, 233]
print(len(numbers))
print(max(numbers))
print(min(numbers))

print(max(23, 1, 9, 99))
print(min(23, 2, 900, 6, 1, 334))