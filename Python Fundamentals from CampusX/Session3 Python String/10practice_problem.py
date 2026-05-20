#Write a program which can remove a particular character from a string

s = input("Enter the string: ")
t = input("What would you want to remove: ")

result = ''

for i in s:
    if i != t:
        result = result + i

print(result)