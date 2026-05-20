#Append()
l = [1, 2, 3, 4, 6]
print(l)
l.append(7) #It means it add 7 in the last
print(l)

#Sort()
colors = ["voilet", "indigo", "blue", "green"]
colors.sort()
print(colors)

num = [4,2,5,3,6,1,2,1,2,8,9,7]
num.sort()
print(num)

colors = ["voilet", "indigo", "blue", "green"]
colors.sort(reverse=True) #Reverse parameter for descending order
print(colors)

num = [4,2,5,3,6,1,2,1,2,8,9,7]
num.sort(reverse=True) #Reverse parameter for descending order
print(num)

#reverse()
colors = ["voilet", "indigo", "blue", "green"]
colors.reverse() #This method reverses the order of the list.
print(colors)

num = [4,2,5,3,6,1,2,1,2,8,9,7]
num.reverse() #This method reverses the order of the list.
print(num)

#index()
colors = ["voilet", "green", "indigo", "blue", "green"]
print(colors.index("green"))

num = [4,2,5,3,6,1,2,1,3,2,8,9,7]
print(num.index(3))

#count()
colors = ["voilet", "green", "indigo", "blue", "green"]
print(colors.count("green"))

num = [4,2,5,3,6,1,2,1,3,2,8,9,7]
print(num.count(2))

#copy()
colors = ["voilet", "green", "indigo", "blue"]
newlist = colors.copy()
print(colors)
print(newlist)

#insert()
colors = ["voilet", "indigo", "blue"]
#           [0]        [1]      [2]

colors.insert(1, "green")   #inserts item at index 1
# updated list: colors = ["voilet", "green", "indigo", "blue"]
#       indexs              [0]       [1]       [2]      [3]

print(colors)

#extend()
colors = ["voilet", "indigo", "blue"]
rainbow = ["green", "yellow", "orange", "red"]
colors.extend(rainbow) #colors will be extended by rainbow
print(colors)

#Concatenating two lists:
colors = ["voilet", "indigo", "blue", "green"]
colors2 = ["yellow", "orange", "red"]
print(colors + colors2)