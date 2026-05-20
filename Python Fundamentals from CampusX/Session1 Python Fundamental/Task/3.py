#Q3:- Take 2 numbers as input from the user.Write a program to swap the numbers without using any special python syntax.

a = int(input('Enter first number: '))
b = int(input('Enter second number: '))

a,b = b,a
print('a: ', a)
print('b: ', b)