class Person:
    def __init__(self,name,gender):
        self.name = name
        self.gender = gender

# Outside of the class -> function
def greet(person):
    person.name = 'ankit'
    return person

p = Person('Fahad','male')
print(id(p))
x = greet(p)
print(id(x))