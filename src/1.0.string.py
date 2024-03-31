print("Hello, Python")
print("Let's go!")
print('Let\'s go!')

# 字符串拼接 只适用字符串字面量
print("Let's say: "'"Hello Python!"' " again!")
x = "Hi! "
y = 'boy and girl.'
# 这里不能使用空格拼接
z = x + y
print(z)
print("hello \nworld")
print(str("hello \nworld!"));
print(repr("hello \nworld!"));
multstr = '''|
hello
" '
haha
!
'''
multstr2 = """
这样可以吗？"\n可以的吧！
"""
print(multstr, multstr2)

multstr3 = "hi!\
girl \
"
print(multstr3)

print \
  (1 + \
2 +   \
  3)

path = "C:\nowhere\js"
print(path)
path = "C:\\nowhere\js"
print(path)
print(r'C:\nowhere\js')
print(r'C:\nowhere\js\'')
print(r"C:\Program Files\foo\bar" '\\')

print("\u00C6")
print('\U0001f60A')
print("This is cat: \N{Cat}")
print("hello world".encode("ASCII"))
print("hell world".encode('utf-8'))
print("hell world".encode('UTF-32'))
print(b'\xff\xfe\x00\x00h\x00\x00\x00e\x00\x00\x00l\x00\x00\x00l\x00\x00\x00 \x00\x00\x00w\x00\x00\x00o\x00\x00\x00r\x00\x00\x00l\x00\x00\x00d\x00\x00\x00'.decode("utf-32"))
print(bytes("Hello world", encoding='utf-32'))
print(str(b'\xff\xfe\x00\x00H\x00\x00\x00e\x00\x00\x00l\x00\x00\x00l\x00\x00\x00o\x00\x00\x00 \x00\x00\x00w\x00\x00\x00o\x00\x00\x00r\x00\x00\x00l\x00\x00\x00d\x00\x00\x00', encoding='utf-32'))

x = bytearray(b'hello!')
x[1] = ord(b'b')
print(str(x, encoding='utf-8'))
