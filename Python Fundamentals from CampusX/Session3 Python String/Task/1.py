#Take a sentence from the user. Count how many vowels (a, e, i, o, u) are in it

s = str(input("Write a sentence: "))

count = 0

for i in s:
    if i.lower() in "aeiou":
        count = count+1

print(count)
    