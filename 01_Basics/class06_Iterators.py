"""
Iterators (i
Iteration: Is a general term of taking each item of something one after another, anytime we use for loop, implicit , explicit
to over a group of items, is called iteration

Iterable: Its an object that has iter method which returns iterator, An Iterable is an object that we can get an iterator from

Iterator: Its an object that has next method, whenever we use for loop, map list comprehension the next method is called automatically to get each item from the iterator
thus going through the process of iteration.
s = "Hello"  # Iterable sequence
for i in s:  # performing iteration
    print(i) # iterator

s = "abc"
it = iter(s) # its iterable sequence
print(next(it)) # a
print(next(it)) # b
print(next(it)) # c
print(next(it)) # stop iteration exception

Generators in Python:
===================
Generator is a simply function which returns an object on which you can call next method such that for every call it returns some value
until it raises stop iteration exception, signaling that all values have been generated. Such an object is called iterators.

Normal functions have single return value, but there's an alternative called yield using  yield anywhere in the function makes it
generator
def foo(n):
    return n*n
    return n
print(foo(8))

def gen(n):
    yield n * n
    yield n + n
    yield n + 10

g = gen(10)
print(next(g))
print(next(g))
print(next(g))
print(next(g))

"""

