tup = (1)
tup1 = (1, 4, 6, 7)
print(tup, type(tup),tup1, type(tup1))

tuple1 = (1,2,2,3,5,4,6)
tuple2 = ("Red", "Green", "Blue")
print(tuple1)
print( tuple2)

details = ("Abhijeet", 18, "FYBScIT", 9.8)
print(details)
     
#Positive Indexing     
country = ("Spain", "Italy", "India",)
#            [0]      [1]      [2]     
print(country[0], country[1], country[2], sep = ", ")


#Negative Indexing
country = ("Spain", "Italy", "India", "England", "Germany")
#            [0]      [1]      [2]       [3]        [4]
print(country[-1], country[-3], country[-4], sep=", ") # Similar to print(country[len(country) - 1])

#Check for item
country = ("Spain", "Italy", "India", "England", "Germany")
if "Germany" in country:
    print("Germany is present.")
else:
    print("Germany is absent.")

country = ("Spain", "Italy", "India", "England", "Germany")
if "Russia" in country:
    print("Russia is present.")
else:
    print("Russia is absent.")

#Printing elements within a particular range
animals = ("cat", "dog", "bat", "mouse", "pig", "horse", "donkey", "goat", "cow")
print(animals[3:7])     #using positive indexes
print(animals[-7:-2])   #using negative indexes

#Printing all element from a given index till the end
animals = ("cat", "dog", "bat", "mouse", "pig", "horse", "donkey", "goat", "cow")
print(animals[4:])      #using positive indexes
print(animals[-4:])     #using negative indexes

#printing all elements from start to a given index
animals = ("cat", "dog", "bat", "mouse", "pig", "horse", "donkey", "goat", "cow")
print(animals[:6])      #using positive indexes
print(animals[:-3])     #using negative indexes

#Print alternate values
animals = ("cat", "dog", "bat", "mouse", "pig", "horse", "donkey", "goat", "cow")
print(animals[::2])     #using positive indexes
print(animals[-8:-1:2]) #using negative indexes

#printing every 3rd consecutive withing given range
animals = ("cat", "dog", "bat", "mouse", "pig", "horse", "donkey", "goat", "cow")
print(animals[1:8:3])