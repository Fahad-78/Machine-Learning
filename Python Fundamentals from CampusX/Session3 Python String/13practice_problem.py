#Write a python program to convert a string to tittle case without using the tittle()

s = input("Enter string: ")

L = []
for i in s.split():
    L.append(i[0].upper() + i[1:].lower())

print(" ".join(L))