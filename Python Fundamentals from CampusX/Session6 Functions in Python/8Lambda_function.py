# x->x^2
a = lambda x:x**2
print(a(2))

#x,y->x+y
b = lambda x,y:x+y
print(b(2,3))

#check if a string has 'a'
a = lambda s:'a' in s
print(a('hello'))

#odd or even
b = lambda x:'even' if x%2==0 else 'odd'
print(b(6))