#We can delete whole tuple not any portion of tuple
t3 = (1,2,3,4,5)
print(t3)
del t3 #Tuple deleted
print(t3)

t5 = (1,2,3, (4,5))
del t5[-1] #We can delete a portion of a tuple
print(t5)