#Q7:- Write a program to find the sum of squares of first n natural numbers where n will be provided by the user.

n = int(input('Enter the number: '))

sum = (n*(n+1)*((2*n)+1)/6)

print('The sum of squares of first',n,'natural numbers: ', sum)