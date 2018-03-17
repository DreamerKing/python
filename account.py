#!/usr/bin/env python3
amount = float(input("Enter amount: "))
rate = float(input("Enter rate: "))
period = int(input("Enter period: "))
value = 0
year = 1
while year <= period:
    value = amount + (rate * period)
    print("Year {} Rs.  {:.2f}".format(year, value)) # 注意{}中没有空格
    amount = value
    year = year + 1
