#Unpack value
a,b,c = (1,2,3)
print(a)
print(b)
print(c)

# #Not possible because too many values for variables
# a,b = (1,2,3)
# print(a)
# print(b)

#Swap value without any third variable
a = 2
b = 3
a,b = b,a
print(a,end=',')
print(b)

#Using others for too many variable problem
a,b,*others = (1,2,3,4,5)
print(a,b)
print(others)

# Zip of tuple
a = (1,2,3,4,5)
b = (6,7,8,9,0)

print(zip(a,b))
print(list(zip(a,b)))
print(tuple(zip(a,b)))