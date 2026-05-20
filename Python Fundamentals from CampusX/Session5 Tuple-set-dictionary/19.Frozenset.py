#Frozenset is just an immutable version of a python set object

f = frozenset([1,2,3,4,5])
print(f)

'''
Is all the functions of set works in frozenset?
ANS: yes, because is just an immutable version of set object
     But, remember that all the read functions will work only not the write operations
     Like, deleting, editing.
'''

#2D frozenset
fs = frozenset([1,2,3,frozenset([4,5])])
print(fs)