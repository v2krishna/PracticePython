"""
Decorators: Are simply functions which extends the functionality of further functions.
Decorators can follow ,following 3 rules:
    1) Must be nested function
    2) Inner function have access of outer function's parameters
    3) Outer Function may return inner function

The inner function can be known as wrapper function and outer function is known as decorator

Types of Decorators
===================
I)user-defined decorators
    1) Function Decorators
    2) Class Decorators

II)built-in decorators
    classmethod
    staticmethod

=========================================================================
def outer(x):   # this will be our decorator
    def inner(a,b,c):   # this will be our wrapper function
        return a*x**2 +b*x+c
    return inner

y = outer(2)
print(y(1,3,5))
==========================================================================

def demo(n):
    def foo(num):
        return (n(num))
    return foo

def general(a):
    print("This is general function")
    return a

obj = demo(general)
print(obj(10))
==========================================================================
def outer(function):
    print("This is outer function")
    def inner(num):
        print("This is inner function:")
        return function(num)
    return inner
@outer
def fizz(a):
    print("This is fizz funciton")
    return a

#obj = outer(fizz)
print(fizz(10))

"""


