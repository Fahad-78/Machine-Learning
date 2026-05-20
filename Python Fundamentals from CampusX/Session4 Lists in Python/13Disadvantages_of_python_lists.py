'''
Disadvantages of python lists
-> Slow
-> Risky usage
-> eats up more memory
'''

a = [1,2,3]
b = a.copy() #If we don't use copy function then b also will be changed

print(a)
print(b)

a.append(4)
print(a)
print(b)

# Lists are mutable