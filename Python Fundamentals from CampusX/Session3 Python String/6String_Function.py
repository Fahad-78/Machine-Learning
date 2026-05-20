#Common Function
a = len('Hello world')
print(a)

b = max('hello world')
print(b)

c = min('Hello world')
print(c)

d = sorted('Hello world')
print(d)
print('\n')

#Capitalize/Title/Upper/Lower/Swapcase
s = 'hello world'
a = s.capitalize()
print(a)

s = 'my personality'
b = s.title()
print(b)

s = 'hello world'
c = s.upper()
print(c)

s = 'HELLO WORLD'
d = s.lower()
print(d)

s = 'Hello World'
e = s.swapcase()
print(e)
print('\n')

#Count/Find/Index
a = 'my name is fahad.'
b = a.count('i')
print(b)

c = a.find('f')
print(c)

d = a.index('is')
print(d)

#endswith/startswith
e = 'My name is Fahad'
a = e.endswith('d')
print(a)

b = e.startswith('My')
print(b)

#Format
name = 'Fahad'
gender = 'male'
a = 'My name is {} and I am a {}.'.format(name, gender)
print(a)

#isalnum / isalpha / isdigit / isidentifier
name = 'nitis123'
a = name.isalnum()
print(a)

b = name.isalpha()
print(b)

c = name.isdigit()
print(c)

d = name.isidentifier()
print(d)

#Split / Join
sentence = 'Hi my name is Fahad'
a = sentence.split()
print(a)

an = ' '
b = an.join(['Hi', 'my', 'name', 'is', 'Fahad'])
print(b)

#Replace
name = 'Hi my name is Fahad'
print(name.replace('Fahad','Arafat'))

#Strip
jh = 'nitish                      '
print(jh.strip())