#args
#allows us to pass a variable number of non-keyword arguments to a function

def multiply(*args):
    product = 1
    for i in args:
        product = product*i
    return product

print(multiply(1,2,3,4,5,6,7,8,9,10,11,12,13))

#kwargs
#kwargs allows us to pass any number of keyword arguments
#keyword arguments mean that they can contain a key-value pair, like a python dictionary

def display(**kwargs):
    for (key,value) in kwargs.items():
        print(key, "->" , value)

display(Bangladesh='Dhaka',India='Delhi',Pakistan='Islamabad',Nepal='Kathmundu')

#Points to be remember
# 1.Order of the arguments matter(normal -> *args -> **kwargs)
# 2.The words args and kwargs are only a convention, you can use any name you want.