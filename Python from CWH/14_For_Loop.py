name = "Fahad"
for i in name:
    print(i, end=", ")
    if(i == "a"):
        print("This is something special!", end=" ")
print("\n")
colors = ["Red", "Green", "Blue", "Black", "Yellow", "White"]
for x in colors:
    print(x)
    for j in x:
        print(j, end=",")
    print("\n")

for k in range(6):
    print(k, end=",")
print("\n")
for k in range(1, 11):
    print(k, end=",")
print("\n")
for k in range(1, 12, 3):  
    #Every time the loop runs, it adds 3 to the previous number.
    print(k, end=",")