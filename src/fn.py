#!/usr/bin/env python
def print_params(first, *params, last):
  print(params)

print_params('hello',1, last=2)
print_params('hello', 2, last='world')
print_params(1,2,3,last=4)

def print_params2(first, **params):
  print(params)

print_params2(first='wxz', y=1, z=3)

"""
收集参数
"""
def print_params3(a,b,c=3, *d, **e):
  print(a, b, c)
  print('d => ', d)
  print('e => ', e)

print_params3(1,2,3,4,5,7,e=8, f=9)