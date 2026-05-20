#Take a list with duplicate numbers e.g. [1,2,2,3,4,4,4,5]. Use a set to remove duplicates, then convert back to a sorted list.

li = [4,3,1,2,2,4,4,5]
s = set(li)
l = list(s)
print(sorted(l))