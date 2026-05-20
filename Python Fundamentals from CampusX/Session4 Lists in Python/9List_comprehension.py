'''List comprehension provides a concise way of creating list
newlist = [expression for item in iterable if condition == True]

advantage of List comprehension
->More time-efficient and space-efficient than loops
->Require fewer lines of code
->Transforms iterative statement into a formula
'''

# Add 1 to 10 numbers to a list
L = []
for i in range(1,11):
    L.append(i)

print(L)

L1 = [i for i in range(1,11)]
print(L1)

# scalar multiplication on a vector
v = [2,3,4]
s = -3

print([s*i for i in v])

# Add squares
L = [1,2,3,4,5]
print([i**2 for i in L])

# Print all the numbers divisible by 5 in the range of 1  to 50
print([i for i in range(1,51) if i%5 == 0])

#find languages which start with letter p
languages = ['java','python','php','c','javascript']
print([language for language in languages if language.startswith('p')])

# nested if with list comprehension
basket = ['apple','guava','cherry','banana']
my_fruits = ['apple','kiwi','graps','banana']
# add new list from my_fruits and items if the fruit exists in basket and also strats with 'a'
print([fruit for fruit in my_fruits if fruit in basket if fruit.startswith('a')])
# print a (3,3) matrix using list comprehension -> nested list comprehension
print([[i*j for i in range(1,4)] for j in range(1,4)])
# cartisian products -> List comprehension on 2 lists together
L1 = [1,2,3,4]
L2 = [5,6,7,8]
print([i*j for i in L1 for j in L2])