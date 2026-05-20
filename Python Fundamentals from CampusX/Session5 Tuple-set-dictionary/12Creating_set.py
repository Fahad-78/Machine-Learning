#empty set
s = set()
print(s)
print(type(s))

#1D and 2D set
s1 = {1,2,3,4,5}
print(s1)
# s2 = {1,2,3,{4,5}} #Not possible. Because set is mutable and inside set we can't keep any mutable object
# print(s2)

#Homo and hetro
s3 = {1,4,5.6,True} #True = 1 so, duplicate can't print
print(s3)
s4 = {1,5,7.8,False} #Set is unordered, its order decide by hash
print(s4)
s5 = {1,2,3.4,(1,2,3,4)} #We can add tuple inside set because tuple is immutable
print(s5)

#Using type conversion
s6 = [1,2,3,4]
print(type(s6))
ss = set(s6)
print(ss)
print(type(ss))

#Duplicates not allowed
s7 = {1,2,3,3,4,5,5,6}
print(s7)

# #Set can't have mutable items
# s8 = {1,2,3,4,[6, 7,8,9]}
# print(s8)

#Proving that set is unordered
s11 = {1,2,3}
s22 = {3,2,1}
print(s11 == s22)