"""
Set
    Is unordered collection of immutable datatype with unique elements
    The common uses of sets are removing duplicates from the sequence, performing mathematical operations
    like union intersection etc
    Sets can only store immutable data.
    Types of Sets
    Mutable             immutable
    -------             ---------
    set                 frozenset

    OPERATIONS ON SETS
    ==================
1) empty set
set1 = set() # mutable
set2 = frozenset() immutable

2) set with multiple elements
s  = {10,20,30,'Hi'}

f = frozenset({10,20,30,'Hi'})

3)membership
print(10 in s)        # True
print(11 in s)        # False
print(20 not in s)    # False
print("Hello" not in s)  # True

4)Type Conversion
s1 = "Programming"
st = set(s1)
print(st)
#{'a', 'g', 'r', 'n', 'i', 'P', 'o', 'm'}
"""

"""
Methods of Sets 
===============
1)add(element) --> it adds an element to the set
                    This method has no effect, if element is already present.

        s = {1,2,3,4}
        s.add(4)
        s.add(5)
        s.add(11)
        print(s)
        # {1,2,3,4,5,11}

2) clear() --  it removes all elements from the set
        s = {1,2,3,4}
        s.clear()
        print(s)
        # set()
3) (frozen set) difference(s2) [-]  --> returns the difference of two sets as new set that is , all elements that are in current set
    but not in other
    s1 = {'a','b','c'}
    s2 = {'e','f', 'b'}
    
    print(s1.difference(s2))
    # {'a',c'}  returns temp set

4)difference_update(s2) [-=] --> removes all elements of another set from current set
        s1 = {'a','b','c'}
        s2 = {'e','f', 'b'}
    
        s1.difference_update(s2)
        print(s1)
        # {'a',c'}
5) (frozen set) symmetric_difference(s2) [^] -- > returns the symmetrix difference of two sets as a new set that is all elements
    that are in exactly one of the set.
    
        s1 = {'a','b','c'}
        s2 = {'e','f', 'b'}
    
        print(s1.symmetric_difference(s2))
       # {'a',c','e','f'}
6)symmetric_difference_udpate(s2)[^=] --> it updates the set with symmetric difference of itself and another.
        s1 = {'a','b','c'}
        s2 = {'e','f', 'b'}
        s1.symmetic_difference_update(s2)
        print(s1)
       # {'a',c','e','f'}
7)discard (element) --> removes an element from a set if it is a member of set.
    if the element is not member, it do nothing.
        s1 = {'a','b','c'}
        s1.discord('a')
        print(s1)  # {'b','c'}
        
        s1.discord('d')
        print(s1) # {'b','c'} do nothing

8)remove(element) --> removes an element from a set if it is a member of set.
    if the element is not member, raises a error
        s1 = {'a','b','c'}
        s1.remove('a')
        print(s1)  # {'b','c'}
        
        s1.remove('d') # raise the error

9)pop() -- remove and returns orbituary set elemment.It raises key error if the set is empty/
        s1 = {'a','b','c'}
        print(s1.pop()) # 'c'
        print(s1.pop()) # 'b'
        print(s1.pop()) # 'a'
        print(s1.pop())# raises key the error

10)  (frozen set)  intersection(s2) [&] --> returns intersection of two sets as a new set .i.e all elements that are common in both sets.
        s1 = {'a','b','c'}
        s2 = {'e','f', 'b'}
        print(s1.intersection(s2)) # {'b'}
        
11) intersection_update(s2) [&=] --> it update current set with intersection of itself and another.
        s1 = {'a','b','c'}
        s2 = {'e','f', 'b'}
        s1.intersection_update(s2)
        print(s1) # {'b'}
12) (frozen set)  union(s2) [|] --> returned a union of two sets as new set.
i.e. all elements are in either set. 
        s1 = {'a','b','c'}
        s2 = {'e','f', 'b'}
        
        print(s1.union(s2)) # {'a','b','c','e','f'}
13)update(s2) [|=] -- update the current set with union of itself another.
        s1 = {'a','b','c'}
        s2 = {'e','f', 'b'}
        
        s1.update(s2)
        print(s1) # {'a','b','c','e','f'}

14) (frozen set)  isdisjoint(s2) -- returns true if two sets have null intersection

15) (frozen set)  issubset(s2) -- reports whether another set contains current set

16) (frozen set)  issuperset(s2) -- > reports whether current set another set
         s1 = {'a','b','c'}
         s2 = {'a','b','c','e','f'}
         
         s3 = {'x,'y'}
         
         print(s1.isdisjoint(s3))  # True
         print(s1.isdisjoint(s2)) # False
         
         print(s1.issubset(s3))  # False
         print(s1.issubset(s2)) # True
        
         print(s1.issuperset(s2))  # False
         print(s2.issuperset(s1)) # True         

wrp to remove duplicate elements from inputted string using set
str = input("Enter the strings:")
s1 = set(str)
print(s1)
==================================================================
wrp to remove an element only if that element is a member of a set
element will be a user input 
s1 = set(str)
print(s1)
s = input("please eneter element to remove:")
s1.discard(s)
print(s1)
str = input("Enter the strings:")
==================================================================
wrp to calculate maximum number from a given set
s = {1,2,3,45,100,750, 1000}
s = {0,1, 2,3, 45, 100, 750, 1000}
max = 0
min = s.pop()
s.add(min)
for element in s:
    if element > max:
        max = element
    if element < min:
        min = element
print(max)
print(min)
==================================================================
wrp to return elements which present in current set but not in other
s1 = {1,2,3,45,100,750, 1000}
s2 = {2,45,67}
s1 = {1,2,3,45,100,750, 1000}
s2 = {2,45,67}
print(s1.difference(s2))
==================================================================
calculate the length of set without using len function

s1 = {1,2,3,45,100,750, 1000}
count = 0
for element in s1:
    count += 1
print(count)
==================================================================
to calculate maximum length word from given set of words

s1 = {"rama", "sagar","krishna", "ramakrishna"}
max_len = 0
s = ""
for element in s1:
    if len(element) > max_len:
        max_len = len(element)
        s = element
print(max_len)
print(s)
==================================================================
wrp to insert random 100 numbers into set of the range 1 to 100

import random
s = set()
c = 0
while len(s) < 100:
    s.add(random.randint(1,100))
    c += 1
print(s)
print(len(s))
print(c)
==================================================================
wrp to calculate the element which are present in either set
s1 = {1,2,45,565, 100}
s2 = {89, 29,65,45,565, 100}
print(s1.symmetric_difference(s2))
==================================================================
1 2 3 6 5 4 4 2 5 3 6 1 6 5 3 2 4 1 2 5 1 4 3 6 8 4 3 1 5 6 2
return the unique value in the above list
l = [1, 2, 3, 6, 5, 4, 4, 2, 5, 3, 6, 1, 6, 5, 3, 2, 4, 1, 2, 5, 1, 4, 3, 6, 8, 4, 3, 1, 5, 6, 2]
for element in l:
    if l.count(element) == 1:
        print(element)
==================================================================
def average(array):
    s = set(array)
    count = len(s)
    avg = sum(s) / count
    return avg

if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    result = average(arr)
    print(result)
==================================================================
Task

Now, let's use our knowledge of sets and help Mickey.

Ms. Gabriel Williams is a botany professor at District College. One day, she asked her student Mickey to compute the average of all the plants with distinct heights in her greenhouse.

Formula used:

==================================================================

"""
