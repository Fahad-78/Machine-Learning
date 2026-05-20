class Person:
    def __init__(self,name,gender):
        self.name = name
        self.gender = gender

# Outside of the class -> function
def greet(person):
    print("Hi, I am",person.name,"And I am a ",person.gender)
    p1 = Person('nitish','male')
    return p1

p = Person('Fahad','male')
x = greet(p)
print(x.name)
print(x.gender)