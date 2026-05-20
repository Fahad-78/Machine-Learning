#del
L = [1,2,3,4,5]
print(L)
del L
#print(L)

#indexing
L1 = [1,2,3,4,5]
del L1[-1]
print(L1)

#slicing
L2 = [1,2,3,4,5]
del L2[1:3]
print(L2)

#Remove
L = [1,2,3,4,5]
L.remove(5)
print(L)

#pop
L = [1,2,3,4,5]
L.pop(0)
print(L)
L.pop()
print(L)

#clear
L = [1,2,3,4,5]
L.clear()
print(L)