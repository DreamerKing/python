import fileinput

for line in fileinput.input(inplace=True):
  line = line.rstrip()
  num = fileinput.lineno()
  print(f'{line:<50} # {num:2d}')