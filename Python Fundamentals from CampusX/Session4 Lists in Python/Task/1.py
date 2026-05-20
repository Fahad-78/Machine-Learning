#Create a list of 5 numbers. Find the sum, average, min, and max without using built-in functions — use loops only.

l = [1,2,3,4,5]

sum = 0

for i in l:
    sum+=i
print("Sum: ",sum)
print("Average: ",sum/5)

minimum = l[0]
for i in l:
    if i<minimum:
        minimum = i
print("Min: ",minimum)

maximum = l[0]
for i in l:
    if i>maximum:
        maximum = i
print("Maximum: ",maximum)