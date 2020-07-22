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
==================
1)enumerate (iterable, start=0)
2)
"""






