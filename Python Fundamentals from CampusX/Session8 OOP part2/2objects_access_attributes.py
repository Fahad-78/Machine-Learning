class person:
    def __init__(self,user_name, user_country):
        self.name = user_name
        self.country = user_country

    def greet(self):
        if self.country=='Bangladesh':
            print("Assalamualaikum", self.name)
        else:
            print('Hello', self.name)


n1 = input("Enter your name: ")
c1 = input("Enter your country: ")
p1 = person(n1,c1)

#How to access atributes
print(p1.name)
print(p1.country)

#How to access methods
p1.greet()

#What if I try to access non-existent attributes
    #p1.gender
#output: I will get an error

p1.gender = 'male'
print(p1.gender)