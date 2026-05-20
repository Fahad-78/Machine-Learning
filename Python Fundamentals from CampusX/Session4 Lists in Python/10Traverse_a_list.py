# 2 ways to traverse a list

# ->itemwise
L = [1,2,3,4]
for i in L:
    print(i, end = ' ')
print('\n')

# ->indexwise
L = [1,2,3,4]
for i in range(0,len(L)):
    print(i, end = ' ')

