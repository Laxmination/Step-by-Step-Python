''' 
Create a class called Order which stores item and its price.
Use dunder function __gt__()to convey that:
  order1 > order2 if the price of order1 > price of order2
'''

class Order:
    def __init__(self, item, price):
        self.item = item
        self.price = price

    def __gt__(self, order2):
        return self.price > order2.price
    

order1 = Order("Chips", 30)
order2 = Order("Coffee", 25)

print(order1 >order2) 