#List of object

class Person:
    def __init__(self,name,gender):
        self.name = name
        self.gender = gender

p1 = Person('nitish','male')
p2 = Person('ankit','male')
p3 = Person('Ankita','female')

L = [p1,p2,p3]
for i in L:
    print(i.name,i.gender)

print('\n')

L1 = (p1,p2,p3)
for i in L1:
    print(i.name,i.gender)

print('\n')

L2 = {'p1':p1,'p2':p2,'p3':p3}
for i in L2:
    print(L2[i].name,L2[i].gender)