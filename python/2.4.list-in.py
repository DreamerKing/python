database = [
  ['albert', '1234'],
  ['dilbert', '4242'],
  ['smith', '7524'],
  ['jones', '9832']
]

username = input('User Name:')
pin = input('PIN:')

if [username, pin] in database:
  print('Access grandted!')