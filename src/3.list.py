l = list('hello')
print(l)
print(''.join(l))

x = [1,2,3]
# 修改列表元素
x[1] = 4
print(x)
# 不能给不存在的列表元素进行赋值
# x[3] = 9
# print(x)

# 删除列表中元素
names = ["Alice", "Beth", "Cecil", 'Dee', 'Earl']
# 会自动改变列表长度
del names[3]
print(names)

# 切片赋值
name = list('Perl')
print(name)
# 保留指定索引前的，替换指定索引之后的元素
name[2:] = list('ar')
print(name)

numbers = [1,5]
# 指定插入位置
numbers[1:1] = [2,3,4]
print(numbers)

numbers[1:4] = []
print(numbers)

numbers[1:] = [2,3,4,5]
print(numbers)
del numbers[1:4]
print(numbers)

numbers = [1,2,3,4,5,6,7,8,9]
del numbers[-1:2:-3]
print(numbers)

numbers = [1,3]
numbers = numbers*2
print(numbers)

