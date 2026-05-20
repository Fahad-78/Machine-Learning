# square the items of a list
L = list(map(lambda x:x**2,[1,2,3,4,5]))
print(L)

#odd/even labelling of list items
L = [1,2,3,4,5]
li = list(map(lambda x:'even' if x%2==0 else 'odd',L))
print(li)

# fatch names from a list of dict

users = [
    {
        'name':'Rahul',
        'age':45,
        'gender':'male'
    },
    {
        'name':'Fahad',
        'age':25,
        'gender':'male'
    },
    {
        'name':'Ritika',
        'age':50,
        'gender':'female'
    }
]

name = list(map(lambda users:users['name'],users))
print(name)