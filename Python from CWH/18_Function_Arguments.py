def average(a=9, b=3): #Default Parameter Values
    print(f"The average is: {(a+b)/2}")

average()
average(1)
average(b=1) #Keyword Arguments

print("\n")

def average1(c, d): #Positional Arguments
    print(f"The average is: {(c+d)/2}")

average1(5, 5)

def average2(*number):
    #print(type(number)) #Touple
    sum = 0
    for i in number:
        sum = sum + i
    #print(f"Average is: {sum/len(number)}")
    return sum/len(number)

c = average2(5, 10, 15)
print(f"Average is: {c}")

def name(**name):
    print(type(name))
    print(f"Hello, {name["fname"], name["mname"], name["lname"]}") #dictionary

name(mname = "Buchanan", lname = "Barnes", fname = "James")