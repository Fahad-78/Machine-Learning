#Q5:- Write a program to find the simple interest when the value of principle,rate of interest and time period is provided by the user.

p = float(input("Enter the value of principle: "))
n = int(input('Enter time in years: '))
r = float(input('Enter the rate of interesrt in percentage: '))

i = p*n*r

print('The simple interest is: ', i)