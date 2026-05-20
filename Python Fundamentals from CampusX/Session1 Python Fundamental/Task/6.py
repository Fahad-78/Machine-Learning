'''Q6:- Write a program that will tell the number of dogs and chicken are there when the user will provide the value of total heads and legs.

For example: Input: heads -> 4 legs -> 12
Output: dogs -> 2 chicken -> 2'''

h = int(input('Enter number of heads: '))
l = int(input('Enter number of legs: '))

d = int((l-(2*h))/2)
c = (h - d)

print('Dogs: ',d,'and Chickens: ',c)