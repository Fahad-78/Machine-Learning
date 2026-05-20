#Create a tuple of 5 city names. Unpack the first, middle, and last city into separate variables and print them.

t = ("Dhaka", "Cumilla", "Maymansingh", "Chittagong", "Rajshahi")

f , *m, l = t

print(f)
print(*m)
print(l)