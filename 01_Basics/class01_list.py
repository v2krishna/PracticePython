"""
Operators in Python
   addition (+)
        a) Addition
        b)concatenation

   subtraction (-)
   multiplication (*)
        a) replication
        b) multiply
   division
     float division (/)
     integer division (//)
    modulo (%)
        gives the remainder
    power (**)
        gives the power of given number


keywords in python
['False', 'None', 'True', 'and', 'as', 'assert', 'async', 'await', 'break', 'class', 'continue', 'def', 'del', 'elif',
 'else', 'except', 'finally', 'for', 'from', 'global', 'if', 'import', 'in', 'is', 'lambda', 'nonlocal', 'not', 'or',
 'pass', 'raise', 'return', 'try', 'while', 'with', 'yield']
import keyword
print(keyword.kwlist)
range
    1) range(val1) --> starts from 0 to val1-1
    2) range(val1,val2) -- > starts from val1 to val2-1
    3) range(val1,val2, step) --> starts from val1 to val2-1 with step
    4) range(val1,val2, -step) --> starts from val2 to val1-1 with -step

for loop
    when we iterate on numbers or specific range then
    for i in range(val1,val2):
        print(i)

    when we iterate on specific sequence then
    seq = "string"
    for str in seq:
        print(str)

if loop // conditional executions
    if condition 1:
        "if body"
    elif condition 2:
        "elif body"
    else:
        "else body"

Truth Table of if .. elif
    inputs
    if         T       F    F
    elif       F       T    F
    else       F       F    T
while loop conditions
    while condition:
        "while body"
         we've to write condition to break the while loop \
         otherwise it will run infinite time
Functions in python
    loop  are used for local use
    functions are used for global use

    Block of code which are executed repeatedly at the time of function calling.
    are block of code which performs the similar kind of functionality within a single block.

    Types of Functions:
    1) Built-in Functions
    2) User-defined Functions
          a) Parameterized udf
                def demo(p1, p2):
                    print(p1, p2)
                demo('test', 'test2')

          b) Non-Parameterized udf
                 def demo():
                    print("Hello Welcome")

    3) recursive functions
            These functions calls themselves within a function body until certain conditions are matched.
            def sum_of_digits(num):
                if num == 0:
                    return num
                else:
                    return num%10 + sum_of_digits(num//10)
            # n = 1987, sum of all digits of this number. ie 1+9+8+7
                #numbers are not hashable or neither iterable

            print(sum_of_digits(1987))

# n = 153
# 1+ 125+27  ==153
# find within 1 to 500

def sum_of_cube_of_num(num):
    if num == 0:
        return 0
    else:
        return (num%10) ** 3 + sum_of_cube_of_num(num//10)

for i in range(1,501):
    a = sum_of_cube_of_num(i)
    if i == a:
        print(i)
    4) anonymous functions /lambda functions

Data Structures
    Mutable Data Structures         Immutable Data Structures
    List                            String
    Dictionary                      Tuple
                                    Sets
                                        Set ( mutable seq)
                                        Frozen Set (immutable seq)
List
    It is ordered collection of mutable data type, lists are iterable , hashable and contains any kind of data type
    Basic Operations on List
        1) Empty List
              a_list= []
        2) list with multiple elements
             a_list  = ["1", 2 , "stringtest"]
        3) Iteration on list
            for i in a_list:
                print(i)
            output
                1
                2
                stringtest
        4) membership on list:
            print(2 in  a_list)
            output
                True
            if not there then false
             print(3 in  a_list)
            output
                False

            print(2 not in  a_list)
            output
                False

            print(3 not in  a_list)
            output
                True
        5) Updation in list
            a_list = [1,2,4,5]
            # Insertion
            a_list[0] = 3
            a_list = [3,2,4,5]

            #deletion
            del a_list[1]
            alist = [3,4,5]

        6) Concatentation
            a1 = [1,3,4]
            a2 = [4,7,9
            print(a1+ a2)  # [1,3,4,4,7,9]

        7) Replication
            print(a1 *3) # [1,3,4,1,3,4,1,3,4]

    Methods of List
        1)append(object) -- it appends an onject to the end of the list
        2)clear() -- it removes all elements from the list
        3)count(a) -- it gives total number of occurances of "a" value in the list.
        4)extend(iterable) --> it extends list by appending elements from iterable
            s = "abc"
            l = [1, 2, 3]
            l.extends(s)
            print(l) #  [1,2,3, "a", "b", "c"]
        5) index(val, start =0, stop=2147483647) -- returns index of the given value within start:stop,
                it raises value error if value is not in list.
            l = [1,2,3,1,5,1,8]
            print(l.index(1)) # 0
            print(l.index(1,start=1)) # 3
            print(l.index(1,start=4)) # 5
            print(l.index(1,start=6)) # raises val error
       6) insert (index, object )
            it inserts object before specified index
         l = [1, 2, 3, 1, 5, 1, 8]
         l.insert(3, 9)
        print(l)
        l.insert(-1, 0)
        print(l)

        7) pop(index = -1)
         it removes and return item at specified index (defualt last)
         it raises index error if list is empty or index is out of range
            l = [1, 4, 5]
            print(l.pop())
            l = [1, 4, 5]
            print(l.pop(1))
            print(l.pop(20))
        8) remove(val)
            it removes the first occurrence of given value
            it raises value error if value is not present
                l = [ 1,4,5,7,9,5]
                l.remove(5)
                print(l)
                l.remove(11)
                # print(l)
        9) reverse()
            it reverses the list by position
            l = [1,4,5,6]
            l.reverse()
            print(l)
        10)sort(key=None,reverse=False)
            it sort the list in ascending order , if key is specified apply once to each item of list and sort them
            ascending or descending according to their function values.
            Reverse is use to sort the list in descending order
                l = [1,4,5,6,3,2]
                l.sort()
                print(l)
                l.sort(reverse=True)
                print(l)
                l = [1,4,5,6,3,2 , 'd', 'c', 6.5, 3.5]
                l.sort(key=str)
                print(l)
                print(ord('c'))
                l = [['a', 3,],['c',1],['b',2]]
                l.sort()
                print(l)
                def first(seq):
                    return seq[1]
                l.sort(key=first)
                print(l)
"""
# This problem was asked by Quora.
# You are given a list of (website, user) pairs that represent users visiting websites. Come up with a program that identifies the top k pairs of websites with the greatest similarity.
# For example, suppose k = 1, and the list of tuples is:
"""
l= [('a', 1), ('a', 3), ('a', 5),
 ('b', 2), ('b', 6),
 ('c', 1), ('c', 2), ('c', 3), ('c', 4), ('c', 5),
 ('d', 4), ('d', 5), ('d', 6), ('d', 7),
 ('e', 1), ('e', 3), ('e', 5), ('e', 6)]
# Then a reasonable similarity metric would most likely conclude that a and e are the most similar, so your program should return [('a', 'e')].
# print(l)

def first(seq):
    return seq[1]

l.sort(key=first)
print(l)
"""
"""
Problem to solve 
l = [1,3,4,8,10,11,14]
n = int(input("Enter a value:"))
# if n = 2  output will be [11,14,1,3,4,8,10]
if n < len(l):
    a = l[-n:]
    b = l[:-n]
    print(a)
    a.extend(b)
    print(a)
else:
    print(l)
    
second sol'n for the above problem 

l = [1,3,4,8,10,11,14]
n = int(input("Enter a value:"))

for i in range(n):
    a = l.pop()
    print(a)
    l.insert(0,a)
print(l)
"""

"""
w.a.p to count and return string that starts and ends with similar character from given list of strings

l = ['abc','xyz', 'aba','1221', '1111', 'tqr']
c = 0
res = []
for element in l:
    if element[0] == element[-1]:
        #print (element)
        c +=1
        #print(c)
        res.append(element)
print(res)
print(c)

"""

"""
l1 = [1,2,3]
l2 = [1,3,5]

l3 = []
for element in l1:
    for j in l2:
        if element != j:
            l3.append([element,j])
print(l3)
"""

"""
program to create identity matrix using list of 3 * 3 dimensions:

l1=[]
for i in range(3):
    l2 = []
    for j in range(3):
        if i == j:
            l2.append(1)
        else:
            l2.append(0)
    l1.append(l2)
print(l1)
"""

"""
l1 = list of 10 numbers  then calculate the sum of even location elements and odd locations 

l1 = [i for i in range(1,11)]
print(l1)
sum_of_even = 0
sum_of_odd = 0
for index in range(len(l1)):
    if index % 2 ==0:
        #print("even location", l1[index])
        sum_of_even += l1[index]
    else:
        sum_of_odd += l1[index]
print(sum_of_even)
print(sum_of_odd)

"""

"""
write a program to make transpose of a matrix.
l1 =[[1,2,3],[4,5,6],[7,8,9]]
# 1 2 3       1 4 7
# 4 5 6       2 5 6
# 7 8 9       3

l2 = []
for i in range(3): # i = 0
    l3 =[]
    for j in range(3): # j = 0,1,2
        l3.append(l1[j][i])
    l2.append(l3)
print(l2)
"""
"""
write a program to make transpose of a matrix.
l1 =[[1,2,3],[4,5,6],[7,8,9]]
output = [1,2,3,4,5,6,7,8,9]

l1 =[[1,2,3],[4,5,6],[7,8,9]]
l2 = []

for i in l1:
    l2.extend(i)
print(l2)


s = 'abc.....xyz'
l = [[], [], []]
import string
s = string.ascii_lowercase
print(s)
l = [[], [], []]
for i in range(len(l)):
    l[i].extend(s[i::3])
print(l)
"""

