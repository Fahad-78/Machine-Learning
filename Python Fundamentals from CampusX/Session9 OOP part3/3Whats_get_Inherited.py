'''
What gets inherited?
    Contructor
    Non Private Attributes
    Non Private Methods
'''
class Phone:
    def __init__(self, price, brand, camera):
        print("Inside phone constructor")
        self.price = price
        self.brand = brand
        self.camera = camera

    def buy(self):
        print("Buying a phone")

class SmartPhone(Phone):
    pass

class Phone1:
    def __init__(self, price, brand, camera):
        print("Inside phone constructor")
        self.price = price
        self.brand = brand
        self.camera = camera

class SmartPhone1(Phone1):
    def __init__(self, os, ram):
            self.os = os
            self.ram = ram
            print("Inside smartphone constructor")

s = SmartPhone(20000, "Apple", 13)
s1 = SmartPhone1('Android', 16)