#Making an ATM machine
class Atm:

    #constractor (special function)
    def __init__(self):
        self.pin = ''
        self.balance = 0
        self.menu()

    def menu(self):
        user_input = input("""
        Hi how can I help you?
        1. press 1 to create pin
        2. press 2 to change pin
        3. press 3 to check balance
        4. press 4 to withdraw
        5. Anything else to exit
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

obj = Atm()
