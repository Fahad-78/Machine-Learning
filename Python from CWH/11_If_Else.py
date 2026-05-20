a = int(input("Enter your age: "))
print("Your age is:", a)

#Conditional operators
# >, <, >=, <=, ==, !=
print(a>18)
print(a<18)
print(a>=18)
print(a<=18)
print(a==18)
print(a!=18)

if(a >= 18):
    print("You can drive.")
else:
    print("You can't drive.")

num = int(input("Enter number: "))
if(num < 0):
    print("Number is negative")
elif(num == 0):
    print("Number is zero.")
else:
    print("Number is positive.")

