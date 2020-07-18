"""
Dictionary -- Unordered collection of mutable data types
              Contains elements as a key-value pair where each key is unique within a dictionary.
Properties of Dictionary keys:
==============================
1) Unique
2) immutable List cannot be used as dictionary key

Basic operations on dictionary
==============================
1)empty dictionary
d={}
2) dictionary with multiple elements
d={'a':10,'b':20,'c':30}

3)Iteration on dictionary using for loop
for i in d:
    print(i) --will give keys
    #output a , b ,c

4)hashing dictionary elements
syntax dict_name[key] #output value for that specific key
print(d['a']) # output = 10
print(d['c']) # output = 30
print(d['f']) # key error

5)updating dictionary
#inserting
syntax dict_name['key'] = value
d['f']=40
d['b'] ='Hello'
print(d)
{'a':10, 'b':'Hello', 'c':30, 'f':40}

#deleting
del d['a']
print(d) # {'b':'Hello', 'c':30, 'f':40}
idf key not present , key error is raises

Methods of dictionary
d={'a':10,'b':20,'c':30}
1) clear() -> it removes all elements from dictionary and returns None
d.clear()
print(d) # {}

2) get(key,default=None) # it returns the value for key if key is in the dictionary,
                        returns default (None) if key is not in the dictionary.

print(d.get('a'))  # 10
print(d.get('f'))  # None
print(d.get('f', 'NotPresent'))  # NotPresent


3) setdefault(key, default=None)  # it inserts key with value of default if key is not in the dictionary.
                                    it returns the value for key if key is in the dictionary else it returns default

print(d.setdefault('g')) # updates dictionary and output is only returned "None"

print(d.setdefault('f',50)) #  updates dictionary and output is only returned 50

print(d.setdefault('a',60)) # it will not update , but returns only 10

print(d)
d={'a':10,'b':20,'c':30, 'g':None, 'f':50}

4)pop(key,default)  # it removes specified key and returns the corresponding value. if key is not found and default is given it returns default.
                      If key is not present and default also not given , then it raises key error

print(d.pop('f'))  # 50
print(d.pop('e','Notpresent')) # NotPresent
print(d.pop('e'))  # key error raises
print(d.pop('b','Hello'))  # returns 20
print(d) # {'a':10,'c':30, 'g':None}

5)popitem() # it removes and return arbitrary (key,value) pairs from the dictionary as a 2-tuple.
               Pairs are returned as a LIFO order
d={'a':10,'b':20,'c':30}
print(d.popitem()) # ('c',30)
print(d.popitem()) # ('d',20)
print(d.popitem()) # ('a',10)
print(d.popitem()) # key error raises

6)update(dict2) # it updates current dictionary by overwriting the existing keys  and inserting new keys
d1 = {'c:'hello', 'f':'bye'}
d.update(d1)  #
print(d) # {'a':10,'b':20,'c':'hello', 'f':'bye'}

7)keys()  # it returns list of dictionary keys
print(d.keys())  # ['a','b','c','f']

8)values()  # it returns list of dictionary values
print(d.values())  # [10, 20,'hello','bye']

9)items() # it returns list of 2-tuples containing key,value pairs
print(d.items()) # [('a',10), ('b',20) ,('c','hello'), ('f','bye')]

for k,v in d.items():
    print(k,v)
('a',10)
('b',20)
('c','hello')
('f','bye')

10) fromkeys(iterable,value=None) # it create a new temporary dictionary with keys from iterable and values set to value
s='abc'
d1={}.fromkeys(s)
print(d1)  # {'a':None, 'b':None,'c':None}
print({}.fromkeys(s,10)) # {'a':10 , 'b':10,'c':10}


"""