#isdisjoint/issubset/issuperset
s1 = {1,2,3,4}
s2 = {3,4,5,6}
print('s1 disjoint s2: ',s1.isdisjoint(s2))
s1 = {1,2,3,4}
s2 = {7,8,5,6}
print('s2 disjoint s1: ',s2.isdisjoint(s1))

s1 = {1,2,3,4,5}
s2 = {3,4,5}
print('s1 subset of s2: ',s1.issubset(s2))
print('s2 subset of s1: ',s2.issubset(s1))

s1 = {1,2,3,4,5}
s2 = {3,4,5}
print('s1 super set of s2: ',s1.issuperset(s2))
print('s2 super set of s1: ',s2.issuperset(s1))

#Copy
s1 = {1,2,3,4,5}
s2 = s1.copy()
print('s1: ',s1)
print('s2: ',s2)