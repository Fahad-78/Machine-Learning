'''
We can't do this, becase string are immutable
s = 'hello'
s[0] = x
print(s)
'''

L = [1,2,3,4,5]
#Editing with indexing
L[-1] = 500
print(L)

#Editing with slicing
L[1:4] = [200,300,400]
print(L)