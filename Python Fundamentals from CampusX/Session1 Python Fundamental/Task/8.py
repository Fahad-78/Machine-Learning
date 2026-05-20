#Q8:- Given the first 2 terms of an Arithmetic Series.Find the Nth term of the series. Assume all inputs are provided by the user.

a1 = int(input("Enter first term: "))
a2 = int(input("Enter second term: "))
n = int(input("Enter nth term you want to find: "))

d = a2-a1

nth = (a1+((n-1)*d))

print("The",n,'th term of the sequence is: ', nth)