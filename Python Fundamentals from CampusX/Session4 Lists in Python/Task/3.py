#Create a 3×3 matrix as a nested list. Print the sum of each row on a separate line.

l = [
    [1,2,3],
    [4,5,6],
    [7,8,9]
]

for i in l:
    sum = 0
    for j in i:
        sum+=j
    print(sum)