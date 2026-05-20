#Take a list of words and create a new list that contains only the words that start with the letter "a" — use list comprehension.

l1 = ["apple","banana","applied","amango","orange","graps"]
l2=[]
for i in l1:
    if i[0] == 'a':
        l2.append(i)
print(l2)