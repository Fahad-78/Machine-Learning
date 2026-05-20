#Find the sum of a 3 digit number entered by the use

num = int(input('Enter a 3 digit number: '))

a = num%10
num = num//10

b = num%10
num = num//10

c = num%10
num = num//10

print('Sum of 3 digits are:', a+b+c)


