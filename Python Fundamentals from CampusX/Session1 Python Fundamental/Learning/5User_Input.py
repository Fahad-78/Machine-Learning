#Take input from user and store them in variables
#Adddd the variables
#Print the result
fnum = input('Enter first number: ')
snum = input('Enter second number: ')

print('Before',type(fnum), type(snum))

sum = int(fnum) + int(snum)
print('Sum of two numbers:',sum)

print('After',type(fnum), type(snum), '\n')


#Another way of Type Conversion
fnum = int(input('Enter 1st number: '))
snum = int(input('Enter 2nd number: '))

print(type(fnum), type(snum))