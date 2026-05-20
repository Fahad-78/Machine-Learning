#del
s = {1,2,3,4,5}
print(s)
#del s
#print(s)

#discard
s.discard(5)
print(s)
s.discard(50) #It will not show any error and any items from the set will not be delete

#remove
s.remove(4)
print(s)
#s.remove(50) #It will show error. This is the difarence between discard and remove otherwise this two are same

s.pop() #it remove any random items from the set
print(s)

s.clear() #It clear the whole set and give an empty set as an output
print(s)