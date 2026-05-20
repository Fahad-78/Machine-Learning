#Count the frequency of a particular character is a provided string
#Eg 'hello how are you' is the string, the frequency of h in this string is 2.

s = input('Enter your string: ')
term = input("What would you like to search for: ")

count = 0
for i in s:
    if i == term:
        count += 1
    

print('Frequency is: ', count)