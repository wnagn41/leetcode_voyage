class Address:
  def __init__(mine, street, number):
    mine.street = street
    mine.number = number

  def myfunc(abc):
    print("My Address is " + abc.street)

p1 = Address("Albert Street", 20)
p1.myfunc()