"""Reference variable
    ->Reference variable hold the objects
    ->We can create objects without refernce variable as well
    ->An object can have multiple reference variable
    ->Assigning a new reference variable to an existing object does not create a new object
    """

class person:
    def __init__(self):
        self.name = 'nitish'
        self.gender = 'male'

p = person()
q = p

#Multiple reference
print(p)
print(q)

#change attribute value with the help of 2nd object
print(p.name)
print(q.name)
q.name = 'Fahad'
print(p.name)
print(q.name)