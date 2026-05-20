#Write a program that can check whether a given string is palindrom or not

s = input("Enter any string: ")

flag = True
for i in range(0, len(s)//2):
    if s[i] != s[len(s)-1-i]:
        flag = False
        break

if flag == False:
    print("Not palindrom")
else:
    print("Palindrom")