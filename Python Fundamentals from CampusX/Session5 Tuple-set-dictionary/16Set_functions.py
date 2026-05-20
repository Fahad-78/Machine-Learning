s1 = {1,2,3,4,4,5,5}
s2 = {4,5,6,6,7,8,9}

#Union {Print all the items of sets but not duplicate just each single item}
print(s1|s2)

#intersection {print those items which are common between these sets}
print(s1&s2)

#Difference 
print(s1-s2) #{print those items which are not into s2}
print(s2-s1) #{Print those items which are not into s1}

#Symetric Difference {print those items which are uncommon betweek sets but not any item will come duplicate}
print(s1^s2)

#Membership test
print(1 in s1)
print(1 not in s1)

#Iterations
for i in s1:
    print(i,end=' ')