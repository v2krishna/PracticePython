"""
Functions Parameters
Types of Parameters
1) Positional Parameters: These are mandatory and they dont have default value. It raises error if missed to pass.
Example:
def foo(a,b):   return a+b  -->
foo(3,5) : 8
foo(3)  : exception missed to pass d
2) Keyworded Parameters: These are not mandatory and they have default value , default vaue can be overwritten
def foo(a,b=10):
    return a+b
foo(3,5) --> 8
foo(3)   --> 13
3) Arbitrary Positional(*args): Its a tuple of positional parameters of arbitrary length. * is used to unpack tuple
def demo(*a):
    return a
t = [10, 20, 30, 40]
demo(*t) --> (10, 20, 30, 40)
demo() --> return () --> empty tuple.

4) Arbitrary Keyworded Parameters (**kwargs): Its a dictionary of keyworded arguments of arbitrary length.
** is used to unpack dictionary.

def demo(**a):
    for k,v in a.items():
        print(k,v)

d = {'a': 10, 'b':20}
demo(**d)
    (a 10)
    (b 20)
demo(c= "hello", e="world")
     (c 'hello')
     (e 'world')
demo()
    {} -- returns empty dictionary

"""