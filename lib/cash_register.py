#!/usr/bin/env python3

class CashRegister:
    def __init__(self, discount=0):
        '''initialize attributes'''
        self.discount = discount
        self.total = 0
        self.items = []
        self.last_transaction = 0

    def add_item(self, title, price, quantity=1):
        '''add items'''
        self.items.extend([title] * quantity)
        self.total += (price * quantity)
        self.last_transaction = price * quantity

    def apply_discount(self):
        '''applies discount'''
        if self.discount > 0:
            self.total = int((self.total) * (100 - self.discount) / 100)
            print(f"After the discount, the total comes to ${self.total}.")
        else:
            print("There is no discount to apply.")

    # def apply_discount_success_message(self):
    #     '''prints success message'''
    #     if self.discount > 0:
    #         print(f"After the discount, the total comes to ${self.total:.2f}.")
    #     else:
    #         print("There is no discount to apply.")

    def void_last_transaction(self):
        '''voids the last transaction'''
        self.total -= self.last_transaction
        self.last_transaction = 0

