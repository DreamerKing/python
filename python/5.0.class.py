class Man:
  def __init__(this, name):
    this.name = name
    print('initialzed!')

  def hello(this):
    print('Hello', this.name)


m = Man('King')
m.hello()
