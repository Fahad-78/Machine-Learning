#Making an ATM machine
class Atm:

    #constractor (special function)
    def __init__(self):
        self.pin = ''
        self.__balance = 0
        self.menu()

    def get_balance(self):
        return self.__balance

    def set_balance(self, new_value):
        if type(new_value) == int:
            self.__balance = new_value
        else:
            print('Use any number please')

    def menu(self):
        user_input = input("""
        Hi how can I help you?

        press 1 to create pin
        press 2 to change pin
        press 3 to check balance
        press 4 to withdraw
        Anything else to exit
        """)

        if user_input == '1':
            #create pin
            self.create_pin()
        elif user_input == '2':
            #change pin
            self.change_pin()
        elif user_input == '3':
            #check balance
            self.check__balance()
        elif user_input == '4':
            #withdraw balance
            self.withdraw()
        else:
            #exit
            exit()

    def create_pin(self):
        user_pin = int(input("Enter pin: "))
        self.pin = user_pin

        user_balance = int(input("Enter your current balance for verify:"))
        self.__balance = user_balance
        print("Your new pin created successfully.")
        #self.menu()

    def change_pin(self):
        prev_pin = int(input("Enter existing pin:"))
        if(self.pin == prev_pin):
            new_pin = int(input("Enter new pin:"))
            self.pin = new_pin
            print("Pin successfully changed.")
            #self.menu()
        else:
            print("Existing pin invalid.")
            #self.menu()
    def check_balance(self):
        user_pin = int(input("Enter your pin:"))
        if(self.pin == user_pin):
            print("Your balance is:",self.__balance)
            #self.menu()
        else:
            print("Invalid pin. Try again please.")
            #self.menu()

    def withdraw(self):
        user_pin = int(input("Enter your pin:"))
        if self.pin == user_pin:
            amount = int(input("Enter amount: "))
            if amount<self.__balance:
                new_amount = self.__balance - amount
                self.__balance = new_amount
                print("Withdraw successful.")
                #self.menu()
            else:
                print("Invalid amount.")
                #self.menu()

        else:
            print("Invalid pin. Try again please.")
            #self.menu()

obj = Atm()
obj._Atm__balance = 'hehehehe' #Nothing is truly hidden in python, because python is made for adults not kids
obj.withdraw()

# We can change or see the balance even if it is set to private variable by this two functions
obj.set_balance(15000)
obj.get_balance()