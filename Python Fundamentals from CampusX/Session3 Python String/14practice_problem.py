#Write a program that can convert an integer to string.

num = int(input("Enter your number: "))

digit = '0123456789'
result = ''

while num != 0:
    result = digit[num % 10]+result
    num = num//10

print(result)
print(type(result))