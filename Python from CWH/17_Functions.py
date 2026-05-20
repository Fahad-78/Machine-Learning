#Function for Geometric calculation
def calculateGmean(a, b):
    mean = (a*b)/(a+b)
    print(mean)

a = 9
b = 8
# gmean1 = (a*b)/(a+b)
# print(gmean1)
calculateGmean(a,b)

c = 8
d = 7
# gmean2 = (c*d)/(c+d)
# print(gmean2)
calculateGmean(c, d)

#Function for finding greater or equal
def calculateGreater(a, b):
    if a>b:
        print("First number is greater.")
    elif a==b:
        print("The numbers are equal.")
    else:
        print("Second number is Greater")

def isLesser(a, b):
    pass

e = 10
f = 12
# if e>f:
#     print("First number is greater.")
# elif e==f:
#     print("The numbers are equal.")
# else:
#     print("Second number is greater.")
calculateGreater(e,f)