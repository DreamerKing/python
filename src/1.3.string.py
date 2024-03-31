import string
"""
# 字符串常量
print(string.digits)
print(string.ascii_letters)
print(string.ascii_uppercase)
print(string.ascii_letters)
print(repr(string.printable))
print(string.punctuation)
"""

"""
# 字符串填充对齐
print("Hello Python!".center(20))
print("Hello Python!".center(20, '*'))
print("Hello".rjust(20, '#'))
print("Hello Python!".zfill(20))
print("Hello".ljust(20, '#'))

print("This is jokes".find('is'))
print("This is jokes".find('is',3))
print("This is jokes".find('Ais'))

title = "$$$ is $$$$ has $$$$ dend"
print(title.find('$$$', 1))
print(title.find('$$$', 8, 12))
print(title.find('$$$', 9, 16))
print(title.find('$$$', 9))
print(title.rfind('$$$'))
print(title.index('is'))
print(title.index('is', 4, 10)) # index 没找到会报错
print(title.startswith("$$$"))
print(title.startswith("$$$", 16))
print(title.endswith('end'))
# 统计子串的出现频次
print(title.count('$$$'))
print(title.count('$$$', 1))
print(title.count('$$$', 1, 16))

"""
"""
# seq = [1,2,3,4,5,6]
# print('#'.join(seq))
seq = ['1', '2', '3']
print('*'.join(seq))

dirs = '', 'usr', 'bin', 'env'
print('/'.join(dirs))
print('C:' + '\\'.join(dirs))

s = '1+2+3+4'
print(s.split('+'))

path = '/usr/bin/env'
print(path.split('/'))
print(path.split('/', 2))
print(path.rsplit('/', 2))

sentence = 'This is word\n\
  hahshs \
end'
print(sentence.split())
print(sentence.splitlines())

print(path.partition('/'))
print(path.rpartition('/'))
print(sentence.partition(' '))
print(sentence.partition('\n'))
"""
str1 = "we are family, We live in the world"
print(str1.lower())
print(str1.upper())
print(str1.capitalize())
print(str1.casefold())
print(str1.swapcase())
print(str1.title())
print(string.capwords(str1))
print(string.capwords(str1, ' '))

str2 = 'we are brother'
print(str2.islower())
print(str2.isupper())
str2 = "We"
print(str2.istitle())
str2 = '23'
print(str2.isalnum())
print(str2.isdecimal())
print(str2.isdigit())
print(str2.isidentifier())
print(str2.isnumeric())
print(str2.isprintable())
print(str2.isspace())

str2 = 'haha hi '
# 转换表 字符码点映射 替换字符要与被替换字符具有一致的长度 第三个参数是要删除的字符
table = str.maketrans('hi','lo')
# table = str.maketrans('hi','lo', ' ')

print(table)
print(str2.translate(table))

print(str2.replace('ha', 'hilo'))
txt = "H\te\tl\tl\to"
print(txt.expandtabs())

# 删除首位空白或指定字符
text = '   The expandtabs() method sets the tab size to the specified number of whitespaces.  '
print(text.strip())
print(text.rstrip())

text = "*** strip * and *! one ****!"
print(text.strip('!*'))

print(ascii('hello'))


