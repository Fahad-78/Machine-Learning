#Write a program to count the number of a words in a string without split()

s = input("Enter your string: ")

L = []
temp = ''
for i in s:
    if i != ' ':
        temp = temp+i
    else:
        L.append(temp)
        temp = ''
L.append(temp)
print(L)