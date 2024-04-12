print("{foo} {} {} {bar}".format(1,2, bar=3, foo=4))
print("{foo} {1} {1} {bar}".format(1,2, bar=3, foo=4))

print("{name[1]}".format(name = (23, "King")))

import math
print("The mode is {mod.__name__} has value {mod.pi}".format(mod = math))

print("{pi!s} {pi!r} {pi!a}".format(pi = "\nking👏"))

num = 2400000
print(f"The number: {num:f} {num} {num:b} {num:g} {num:e} {num:.2E} {num:G}")

num = -0x23B

print(f"Number: {num:d} {num:n} {num:o} {num:x} {num:F}")

name = "King"
print(f"{num:10}")
print(f"{name:10}")
num = 232000.238
print(f"{num:<20}")
print(f"{num:^20}")
print(f"{num:>20.2f}")
print(f"{num:^20,.2f}")
print(f"{num:,.2f}")

num = +43.23
num2 = -90.327

print(f"{num:+10}")
print(f"{num:10}")
print(f"{num2:10}")
print(f"{num2:-10}")
print(f"{num: 10}")
print(f"{num2: 10}")
print(f"{num:&<10}")
print(f"{num2:&>10}")
print(f"{num2:&^10}")
print(f"{num2:&=10}")
print(f"{num2:=10}")


str1 = "long long string"
print(f'{str1:.3}') # 字符截取

num = -23
print(f"{num:10b}")
print(f"{num:#10b}")
print(f"{num:*=#10x}")
print(f"{num:*>#10x}")

