from item import Item
from phone import Phone
from keyboard import Keyboard

item1 = Item('MyItem', 750)

item1.send_email()
item1.apply_discount()
print(item1.price)

item2 = Phone('PhoneV30', 1000)

item2.send_email()
item2.apply_discount()
print(item2.price)

item3 = Keyboard('KeyboardV23', 500)

item3.send_email()
item3.apply_discount()
print(item3.price)
