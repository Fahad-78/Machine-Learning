def g(y):
    print(x)
    print(x+1)

x=5
g(x)
print(x,'\n')

"""Variables inside function are local variable and variable outside function are global variable.
We can use global variable from local variable but we can't use local variable from global variable.
So that those variable who are inside function we can't use them outside of the function."""

def f(y):
    x=1
    x+=1
    print(x)

x=5
f(x)
print(x,'\n')

"""✅ Reading a global variable inside a function — perfectly fine
   ❌ Modifying a global variable inside a function — causes an error"""
# def h(y):
#     x+=1
# x=5
# h(x)
# print(x,'\n')

#But we can change the global variable using global keyword
def h(y):
    global x
    x+=1
x=5
h(x)
print(x,'\n')

#Another example
def f(x):
    x = x+1
    print('in f(x): x=',x)
    return x
x = 3
z = f(x)
print('in main program scope: z=',z)
print('in main program scope: x=',x)