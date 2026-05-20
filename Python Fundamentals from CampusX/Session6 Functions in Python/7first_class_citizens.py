# type and id
def square(num):
    return num**2

print(type(square))
print(id(square))

#reassign
x = square
print(x)
print(id(x))
print(x(3))

#deleting a function
'''
del square

'''
#storing
L = [1,2,3,4,square]
print(L)
print(L[-1](3),'\n')

#returning a function
def f():
    def x(a,b):
        return a+b
    return x

val = f()(3,4)
print(val,'\n')

# function as arguments
def func_a():
    print("Inside function a")

def func_b(z):
    print('inside function b')
    return z()

print(func_b(func_a),'\n')