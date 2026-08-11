'''
Inheritance
    ->What is inheritance
    ->Example
    ->What gets inherited?
'''
#Example of Inheritance
#Parent class
class User:
    def __init__(self):
        self.name = 'Fahad'

    def login(self):
        print('login')

#Child class
class Student(User):

    def enroll(self):
        print('enroll into the course')

u = User()
s = Student()

print(s.name)
s.login()
s.enroll()