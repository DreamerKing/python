website = 'http://github.com'
# 字符串是不可变，不能进行索引赋值和切片赋值
# website[-3:] = 'cn'

# 字符串格式化

value = ('Dreamer', 23)
show_str = "My name is %s, I'm %d years old"
print(show_str % value)

from string import Template
temp = Template("My name is $name, I'm $age years old")
print(temp.substitute(name = value[0], age= value[1]))

fstr = "{}, {} and {}".format("Dreamer", "King", "Jefi")
print(fstr)

fstr = "{1}, {0} and {1}".format("Dreamer", "King", "Jefi")
print(fstr)

print("{3} {0} {2} {1} {3} {0}".format("be", "not", "or","to"))

from math import pi, e
print("{name} is {:.2f}".format(pi, name="PI"))
print("{name} is {value:.2f}".format(value = pi, name="PI"))
print("{name} is {value}".format(value = pi, name = "PI"))
print("e is {:.3f} and pi is {:.5f}".format(e, pi))
print(f"Pi is {pi:.6f}")

# print("{'name'}".format())
# print("{name}".format())
print("{{name}}".format())