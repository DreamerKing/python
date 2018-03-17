#!/usr/bin/env python3
N = 10
sum = 0
count = 0
print("please input %d numbers:"% N)
while count < N:
    number = float(input())
    sum += number
    count += 1
average = sum / count
print("N={} Sum={:.2f} Average={:.2f}".format(count, sum, average))

