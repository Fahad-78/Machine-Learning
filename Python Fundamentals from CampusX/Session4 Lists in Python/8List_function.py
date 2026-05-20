#len/min/max/sorted
L = [2,1,5,7,0]
print(len(L))
print(min(L))
print(max(L))
print(sorted(L))

#count
L = [1,2,1,3,4,1,5]
print(L.count(1))

#index
L = [1,2,1,3,4,1,5]
print(L.index(3))

#reverse
L = [2,1,5,7,0]
print(L.reverse()) #permanently reverses the list
print(L)

#sort (vs sorted)
L = [2,1,5,7,0]
print(L)
print(sorted(L)) #temporary
print(L)
L.sort() #permanent
print(L)

#copy -> shallow
L = [2,1,5,7,0]
print(id(L))
L1 = L.copy()
print(L1)
print(id(L1))