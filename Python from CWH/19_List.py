l = [3, 5, 6]
print(l, type(l))
print(l[0], l[1], l[2], sep = ", ")

lst2 = ["Red", "Green", "Blue"]
print(lst2)

details = ["Abhijeet", 18, "FYBScIT", 9.8]
print(details)

#Positive Indexing:
colors = ["Red", "Green", "Blue", "Yellow", "Green"]
#          [0]      [1]     [2]      [3]      [4]
print(colors[2], colors[4], colors[0], sep = ", ")

#Negative Indexing:
colors = ["Red", "Green", "Blue", "Yellow", "Green"]
#          [-5]    [-4]    [-3]     [-2]      [-1]
print(colors[-1], colors[-3], colors[-5], sep = ", ")
print(colors[len(colors)-2])
print(colors[len(colors)-4])

colors = ["Red", "Green", "Blue", "Yellow", "Green"]
if "Yellow" in colors:
    print("Yellow is present.")
else:
    print("Yellow is absent.")

colors = ["Red", "Green", "Blue", "Yellow", "Green"]
if "Orange" in colors:
    print("Orange is present.")
else:
    print("Orange is absent.")

#printing elements within a particular range:
animals = ["cat", "dog", "bat", "mouse", "pig", "horse", "donkey", "goat", "cow"]
print(animals[3:7])	#using positive indexes
print(animals[-7:-2])	#using negative indexes'

#printing all element from a given index till the end
animals = ["cat", "dog", "bat", "mouse", "pig", "horse", "donkey", "goat", "cow"]
print(animals[4:])	#using positive indexes
print(animals[-4:])	#using negative indexes

#printing all elements from start to a given index
animals = ["cat", "dog", "bat", "mouse", "pig", "horse", "donkey", "goat", "cow"]
print(animals[:6])	#using positive indexes
print(animals[:-3])	#using negative indexes

#Printing alternate values
animals = ["cat", "dog", "bat", "mouse", "pig", "horse", "donkey", "goat", "cow"]
print(animals[::2])		#using positive indexes
print(animals[-8:-1:2])	#using negative indexes

#printing every 3rd consecutive value withing a given range
animals = ["cat", "dog", "bat", "mouse", "pig", "horse", "donkey", "goat", "cow"]
print(animals[1:8:3])