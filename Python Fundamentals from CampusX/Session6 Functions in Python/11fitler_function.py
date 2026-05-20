# numbers greater than s
L = [3,4,5,6,7]
l = list(filter(lambda x:x>5,L))
print(l,'\n')

#fetch fruits starting with 'a'
fruits = ['apple','guava','cherry']
f = list(filter(lambda x:x.startswith('a'),fruits))
print(f)