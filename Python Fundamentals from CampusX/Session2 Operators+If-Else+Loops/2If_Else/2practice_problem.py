#Find the min of 3 given numbers

num1 = int(input('Enter 1st number: '))
num2 = int(input('Enter 2nd number: '))
num3 = int(input('Enter 3rd number: '))

if num1<num2 and num1<num3:
    print('1st number is the minimum')
elif num2<num1 and num2<num3:
    print('2nd number is the minimum')
elif num3<num1 and num3<num2:
    print('3rd number is the minimum')
else:
    print('Something is wrong. Maybe 2 or 3 numbers are equal.')
