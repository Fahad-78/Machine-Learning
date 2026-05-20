"""
Types of arguments:
    1. Default argument
    2. Positional argument
    3. Keyword argument
"""

#Default argument
def speed(a=1,b=1):
    return a**b

print(speed(2,3))
"""Here we do is when the function recieved two parameters it works, if function didn't recieved a perameter or two parameter it
didn't shows any error. Thats why we declare a default value is parameters and its called default arguments"""

#Positional arguments
"""It's nothing new. If wee look at the code above we can see that when we give 2 and 3 in parameters
2 go to a and 3 go to b. So the first value is always go in the first parameter and the orders goes like this"""

#Keyword arguments
def speed(a=1,b=1):
    return a**b

print(speed(b=3,a=2))
'''Here the positional arguments didn't work because we declare the value with key. Means where is the b i don't care the 3 should go there in b and same for a'''
