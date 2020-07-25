"""
List Comprehension
==================
Its a concise way to declare a list where each element of list is an result of some expression.

Syntax of List Comprhension
1) [expression loop condition] when to filter the data
2) [exp condition loop]  if in exp itself we need to use condition

l = [n*n for n in range(1,21)]
print(l)
l = [n *n for n in range(1,21) if n%2!=0]
print(l)
l= [n*n if n%2!=0 else n**3 for n in range(1,21)]
print(l)

l = ["fizbuz" if i%3==0 and i %5==0 else "fiz" if i%3==0 else "buz" if i%5==0 else i for i in range(1,51)]
# [exp if cond else exp if cond ...  loop]
print(l)

===========================
#lambda Functions in Python
===========================
Its small anonymous function can be created with lambda keyword

Lambda function can be used whereever function objects are required.
They are syntactically restricted to a single expression, symentically they are just syntatic sugar for normal  function definition

When to lambda functions or normal functions
Lambda function can be used where ever function objects are required.

syntax:
======
lambda params:expession condition
l = lambda n: 'even' if n%2==0 else 'odd'
print(l(10))
print(l(11))

normal function
def demo (n):
    if n%2 ==0:
        print('even')
    else:
        print('odd')
demo(10)
demo(11)

obj = lambda n : 'fizbuz' if n%3==0 and n%5==0 else 'fiz' if n%3==0 else 'buz' if n%5==0 else n
print(obj(10))
print(obj(3))
print(obj(7))
print(obj(15))

    Built-in Functions:
========================
1)enumerate (iterable, start=0) it return an enumerate object such that it returns a list of tuples containing
 count (start = 0 ) and the values obtain from iteratring over iterable.
l = ['a','b','c','d']
e = enumerate(l)
print(list(e))
e1 = list(enumerate(l,1))
print(e1)
s = "Python Programming"
e2 = list(enumerate(s,1))
print(e2)

2)zip(*iterables) -- it make an iterator that aggregates elements from each of the iterables.
                     It returns iterator of tuples , where the i(th) tuple contains the i(th) element from each of the
                     argument sequences.
                     The Iterator stops when the shortest input iterable is exhausted with a single iterable argument.
                     It returns an iterator of one tuple.
                     With no arguments, it returns an empty iterator
l1 =[1,2,3]
l2 = [4,5,6]

z1 = list(zip(l1,l2))
print(z1)

s1 = "python"
s2="programming"
print(list(zip(s1,s2)))
print(list(zip(s1)))
print(list(zip('')))

3)map(fun,iterables) -- it returns an iterator that applies function to every item of iterable yielding the results
if additional iterables are passes function must take that many arguments and is applied to the items from all iterables
in parallel.
With multiple iterables, the iterator stops when the  shortest input is exhausted.
Map can be used to apply expression on iterables.

l1 = [1,2,3]
l2 = [4,5,6]

m1 = list(map(lambda x,y : x+y , l1,l2))
print(m1)

s1 ="python"
m2 = list(map(lambda x,y,z  :str(x)+str(y)+z , l1,l2,s1))
print(m2)

m3 = list(map(lambda x,y,z : str(x+y) +z, l1,l2,s1))
print(m3)

l3 = ['hello', 'world','welcome', 'to','python', 'programming']
m4 = list(map(lambda x: x.title(), l3))
print(m4)

m = list(map(lambda x: x+'ly' if x.endswith('ing') else x+'ing', l3))
print(m)

m5 = list(map(lambda x: 'fizbuz' if x%3 ==0 and x%5==0 else 'fiz' if x%3==0 else 'buz' if x%5==0 else x, range(1,51)))
print(m5)

m1 = list(map(len, [ [1], [2], [3] ]))
print(m1)

m2 = list(map(lambda x: x.split(' '), 'a b c'))
print(m2)

4)filter(fun,iterable)
======================
It construct an iterator from those elements of iterable for which function returns true
If function is None the identity function is assumed that is all elements of iterable that are false are removed.
l1 = ['Hi', 'bye', 1, 2, 3, '4', 'c']
f1 = list(filter(lambda x: type(x) == str , l1))
print(f1)

f2 = list(filter(lambda x: type(x)== int ,l1))
print(f2)

l3 = ['hello', 'world','welcome', 'to','python', 'programming']
f3 = list(filter(lambda x : len(x)>4, l3))
print(f3)

f4 = list(filter(lambda x : len(x)<=5, l3))
print(f4)

l4 = [-2, 1 , 3, -4 ,9 ,8 ,1 , -1, -3]
f5 = list(filter(lambda x : x >0 and x % 2 ==0, l4))
print(f5)

x1 = {'x': 1}
y2 = {'y': 2}
x3_y4 = {'x': 3, 'y': 4}

m4 = list(filter(lambda d: 'x' in d.keys(), [ x1, y2, x3_y4 ]))
print(m4)

print(list(filter(str.swapcase, [ 'a', '1', 'b', '2' ])))

5)functools.reduce(func,iterable,initializer)
==============================================
It applies function of two arguments cumulatively to the items of iterable from left to right, so as to reduce the function
to a single value.
If the optional initializer is present, its placed before the items of the iterable in the calculation and serves as default when iterable is empty.
If the initializer is not given and iterable contains only one item , the first item is returned.

import functools

c = functools.reduce(lambda x,y : x+y , range(1,11))
print(c)

c = functools.reduce(lambda x,y : x+y , range(1,11),100)
print(c)

c = functools.reduce(lambda x,y : x+y , range(1,2))
print(c)

c = functools.reduce(lambda x,y : x+y , '', 'None')
print(c)

=====================================================
cube = lambda x: x**3  # complete the lambda function

def fibonacci(n):
    # return a list of fibonacci numbers
    f = lambda x: x if x == 0 or x == 1 else f(x-2 )+f(x-1)
    l= list(map(f,range(n)))
    return l

if __name__ == '__main__':
    n = int(input("Enter n:"))
    print(list(map(cube, fibonacci(n))))
============================================================================================================================
write a lambda expression and map function to replace string with a given characters
given for string s , c1 and c2 , replace characters with c1 with c2 and c2 to c1

s = "grrksfoegrrks"
c1 ="e"
c2 = "r"

s1 = list(map(lambda s: s.replace(c1,c2) if c1 in s else s.replace(c2,c1), s))
s2 ="".join(s1)
print(s2)
============================================================================================================================
find the number occuring odd number of times using lambda exp and reduce function.
Given and list of positive integers

import functools
l =[1,2,3,2,3,1,2]
f = lambda inp : functools.reduce(lambda a,b : a^b, inp)
print(f(l))

print("testing symmetric difference")
print((((((1^2)^3)^2)^3)^1)^2)
============================================================================================================================
write a recursive Factorial using lambda function
f = lambda x : 1 if x== 0 or x == 1 else x*f(x-1)
print(f(5))
============================================================================================================================
s = "Test the String replacement"
print(s.replace("the","of"))
============================================================================================================================
Given list of float  values , write a function to sort the output resulted list
t = ['1.2', '.8', '19.8', '2.7', '99.8', '80.7'] # output['.8', '1.2', '2.7', '19.8', '80.7', '99.8']

t = ['1.2', '.8', '19.8', '2.7', '99.8', '80.7']

# a = list(map(lambda t: float(t), t))
# a.sort()
print(list(map(lambda a: str(a), sorted(list(map(lambda t: float(t), t))))))
============================================================================================================================
write a program to convert 3d list to 2d
Input = [[[3], [4]], [[5], [6]], [[7], [8]]]
ouput = [[3], [4], [5], [6], [7], [8]]
method#1
Input = [[[3], [4]], [[5], [6]], [[7], [8]]]
output = []
for elements in Input:
   for i in elements:
       print(i)
       output.append(i)
print(output)

Input = [[[3], [4]], [[5], [6]], [[7], [8]]]
output = [i for element in Input for i in element]
print(output)

=====================================================================
wrp to convert mixed datatype tuple list to string list
t = [('sts', 1, True), ('is', False), ('best', 2)]
#output  = [('sts', '1', 'True'), ('is', 'False'), ('best', '2')]

t = [('sts', 1, True), ('is', False), ('best', 2)]

for element in t:
    for ele in element:
        print(str(ele))
# o = [tuple(str(ele)) for elements in t for ele in elements]
o = [tuple(map(str,i)) for i in t]
print(o)

=====================================================================
wrp to convert string list to nested character list
t = ["a, b, c", "gfg, is, best", "1, 2, 3"]
output= [[‘a’, ‘b’, ‘c’], [‘gfg’, ‘is’, ‘best’], [‘1’, ‘2’, ‘3’]]
t = ["a, b, c", "gfg, is, best", "1, 2, 3"]
print(len(t))

o = [list(map(str, i.split(', '))) for i in t]
print(o)

=====================================================================
"""
