#Static vs Dynamic Typing
#Static vs Dynamic Binding
#Stylish declaration technique

name = 'Fahad'
print(name)

a = 5
b = 2
print(a+b)

#Dynamic Typing (We don't tell the type of the variable)
a = 5
#Static Typing (We tell the type of the variable)
#int a1 = 5 #Python support dynamic typing

#Dynamic binding
a  = 5
print(a)
a = 'Fahad'
print(a)

#Stylish declaration technique
a = 1
b = 2
c = 3
print(a+b+c)

a,b,c = 1,2,3
print(a,b,c)

a=b=c=5
print(a,b,c)