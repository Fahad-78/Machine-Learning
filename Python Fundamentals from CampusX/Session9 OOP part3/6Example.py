class Parent:
    def __init__(self, num):
        self.__num = num

    def get_num(self):
        return self.__num

class Child(Parent):
    def __init__(self,val,num):
        self.val = val

    def get_val(self):
        return self.__val

son = Child(100, 10)
print("Parent: Num:",son.get_num())
print("Child: Val:",son.get_val())

#It shows an error in the output