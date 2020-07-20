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


==================================================================================================
problems
1)to count number of occurrences of characters of given string (The quick Brown fox jumps over The lazy Dog )
s ="The quick Brown fox jumps over The lazy Dog"
char_count_dict = {}
for ch in s:
    if ch in char_count_dict:
        char_count_dict[ch] +=1
    else:
        char_count_dict[ch] =1
print(char_count_dict)

# using functions

def char_count_dict(str):
    char_count_dict ={}
    for ch in str:
        if ch in char_count_dict:
            char_count_dict[ch] +=1
        else:
            char_count_dict[ch] =1
    return char_count_dict

s = "The quick Brown fox jumps over The lazy Dog"
print(char_count_dict(s))
==================================================================================================
3)program to set words first character as key and remaining as a value, if the more than one word starting with same character, concat all the words
{T:'TheTheThis'}
==================================================================================================
2)program to count number of occurrences of input word in a input string (The quick Brown fox jumps over The lazy Dog )
def fn_word_count_dict(in_word, in_str):
    words = in_str.split()
    print(words)
    word_count_dict = {}
    for word in words:
       if in_word == word:
            if word in word_count_dict:
                word_count_dict[in_word] +=1
            else:
                word_count_dict[in_word] = 1
    if len(word_count_dict) == 0:
        word_count_dict[in_word] = 0
    return word_count_dict

s = "The quick Brown fox jumps over The lazy Dog"
w =  input("Enter a string:")
print(fn_word_count_dict(w, s))
==================================================================================================
3)program to set words first character as key and remaining as a value, if the more than one word starting with same character, concat all the words
{T:'TheTheThis'}
str = "program to set words first character as key and remaining as a value if the more than one word starting with same character concat all the words"
print(len(str.split()))
cd = {}
for ch in str.split():
    if ch[0] not in cd:
        cd[ch[0]] = ch
    else:
        cd[ch[0]] = cd[ch[0]] + " " + ch

print(cd)
==================================================================================================
4) wrp to make even location word as a key and odd location word has a value from a given string.
str = "program to set words first character as key and remaining as a value if the more than one word starting with same character concat all the wordsss"
print(len(str.split()))
wd = {}
words = str.split()
for i in range(0, len(words), 2):
    print(i)
    if i+1 >= len(words):
        wd[words[i]] = "None"
    else:
        print(words[i])
        wd[words[i]] = words[i+1]
print(wd)
==================================================================================================
str = ''' jan  year    feb  year    mar  year    apr  year    may  year    jun  year    jul  year    aug  year    sep  year    oct  year    nov  year    dec  year     win  year     spr  year     sum  year     aut  year     ann  year
    9.0  1916   10.0  2019   12.1  2012   15.7  2011   17.2  2018   20.5  1940   23.3  2006   22.8  1995   19.4  1895   15.6  1921   11.6  2011   10.7  2015    8.59  1989   13.99  1893   20.99  1976   14.84  2006   13.54  2014'''
# output {jan: 9.0, years:[1916,2019, 2012, 2011, 2018.. ], feb:10.0 , Mar: 12.1}
words = str.split("   ")
cd = {"years":[]}
l= []
l1 = []

for word in words:
    w = word.strip().split("  ")
    #print(w)
    if not w[1].isalpha():
        cd['years'] .append(w[1])

    if w[0].isalpha():
        l.append(w[0])
    else:
        l1.append(w[0])
print(l)
print(l1)
for i in range(len(l)):
    cd[l[i]] = l1[i]
print(cd)
==================================================================================================
d = {'id':[], 'name':[], 'age':[], 'salary':[]}
take user input for id, age- integer field,
name: string
salary:float
take an input for how many inputs:

d = {'id':[], 'name':[], 'age':[], 'salary':[]}
n = int(input("enter no of inputs:"))
for i in range(n):
    for k in d :
        if k == 'id' or k=='age':
            d[k].append(int(input(f"please enter {k}")))
        elif k == 'salary':
            d[k].append(float(input(f"please enter {k}")))
        elif k == 'name':
            d[k].append(input(f"please enter {k}"))
print(d)
==================================================================================================
"""

