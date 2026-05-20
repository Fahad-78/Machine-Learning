#len/sum/min/max/sorted
s = {1,2,3,4,5}
print(len(s))
print(sum(s))
print(min(s))
print(max(s))
print(sorted(s))
print(sorted(s,reverse=True))

print('1st half!')

#Union/update
s1 = {1,2,3,4,5}
s2 = {4,5,6,7,8}
print(s1.union(s2)) #s1|s2

s1.update(s2)
print(s1)
print(s2)

print('Middle portion!!')

#intersection/intersection_update
s1 = {1,2,3,4,5}
s2 = {4,5,6,7,8}
print(s1.intersection(s2))

s1.intersection_update(s2)
print(s1)
print(s2)

print('End of Intersection!!')

#diference/diference_update
s1 = {1,2,3,4,5}
s2 = {4,5,6,7,8}
print(s1.difference(s2))

s1.difference_update(s2)
print(s1)
print(s2)

print('End of difference!!')

#symetric_difference/symetric_difference_update
s1 = {1,2,3,4,5}
s2 = {4,5,6,7,8}
print(s1.symmetric_difference(s2))

s1.symmetric_difference_update(s2)
print(s1)
print(s2)