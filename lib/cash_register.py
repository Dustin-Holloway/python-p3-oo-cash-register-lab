#!/usr/bin/env python3
import ipdb
class CashRegister:
    def __init__(self, discount=0, total=0.0, items=None, price_list=None):
        self.total = total
        self.discount = discount
        self.items = []
        self.price_list = []
 
    def add_item(self, title, price, quantity=1):
          self.total += (price * quantity)
          for  i in range(quantity):
            self.items.append(title)
            self.price_list.append(price * quantity)

    def apply_discount(self):
          if self.discount == 0 or None:
            print("There is no discount to apply.")
          else:
            self.total *= (1 - self.discount/100)
            print(f"After the discount, the total comes to ${int(self.total)}.")

    def void_last_transaction(self):

      last_price = self.price_list.pop()
      self.items.pop()
      self.total -= last_price

      if len(self.items) == 0:
        self.total = None

            
        


        

        
        
  
# my_register = CashRegister(20, 1000)
# my_register.add_item("pizza", 2.45)
# my_register.apply_discount()
# my_register.void_last_transaction()