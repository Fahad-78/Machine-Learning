#Making an ATM machine
class Atm:

    __counter = 1

    #constractor (special function)
    def __init__(self):
        self.pin = ''
        self.balance = 0
        self.cid = Atm.__counter
        Atm.__counter = Atm.__counter+1    
        #self.menu()

    #Utility function
    @staticmethod
    def get_counter():
        return Atm.__counter

    
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
            self.check_balance()
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
        self.balance = user_balance
        print("Your new pin created successfully.")
        self.menu()

    def change_pin(self):
        prev_pin = int(input("Enter existing pin:"))
        if(self.pin == prev_pin):
            new_pin = int(input("Enter new pin:"))
            self.pin = new_pin
            print("Pin successfully changed.")
            self.menu()
        else:
            print("Existing pin invalid.")
            self.menu()
    def check_balance(self):
        user_pin = int(input("Enter your pin:"))
        if(self.pin == user_pin):
            print("Your balance is:",self.balance)
            self.menu()
        else:
            print("Invalid pin. Try again please.")
            self.menu()

    def withdraw(self):
        user_pin = int(input("Enter your pin:"))
        if self.pin == user_pin:
            amount = int(input("Enter amount: "))
            if amount<self.balance:
                new_amount = self.balance - amount
                self.balance = new_amount
                print("Withdraw successful.")
                self.menu()
            else:
                print("Invalid amount.")
                self.menu()

        else:
            print("Invalid pin. Try again please.")
            self.menu()

c1 = Atm()
c2 = Atm()
c3 = Atm()

print(c1.cid)
print(c2.cid)
print(c3.cid)

print(Atm._Atm__counter)
#print(Atm.__counter) will show error
#print(Atm.counter) will show error

#How to access static method
print(Atm.get_counter()) # We have to use class name instead of obj