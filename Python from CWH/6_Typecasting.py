a = "1"
# a = 1
b = "2"
# b = 2
print(int(a) + int(b))

#Explicite Typecasting
string = "15"
number = 7
string_number = int(string) #throws an error if the string is not a valid integer
sum = number + string_number
print("The Sum of both the numbers is: ", sum)


#Implicit Typecasting
# Python automatically converts a to int
a1 = 7
print(type(a1))
 
# Python automatically converts b to float
b1 = 3.0
print(type(b1))
 
# Python automatically converts c to float as it is a float addition
c = a1 + b1
print(c)
print(type(c))