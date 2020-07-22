"""
String -- Is a ordered collection of immutable data type
          Are iterable ,hashable and contains data within quotation marks(" , ')
Multi-line String -- """ """          

All methods give temp results/output.
Methods of string:
1) capitalize() -- returns capitalized version of string more specifically it makes the first character have upper case \n 
                   and rest have lower case
example 
s = "Hello world!"
print(s.capitalize()) # Hello world!

2) count(substring, start, end ) --  returns the number of occurences of given substring in original string
example
s = "Hello world!"
print(s.count('l')) # 3
print(s.count('x')) # 0 
print(s.count('l', 4) # 1

3) endswith(substring, start, end)      - - it returns true if string ends with specified suffix, otherwise it returns 
                                     false, within [start : end]  
4) startswith(substring, start, end) --- it returns true if string starts with specified suffix, otherwise it returns 
                                     false, within [start : end]  
s = "Hello world!"
print(s.endswith('d') )  # True
print(s.startswith('w') )  # False
print(s.endswith('word'))  # False

5)find(substring, start, end)  # it returns the lowest index in string, where substring is found
                                 returns -1 if substring is not found in string.
                                 
s = "Hello world!"
print(s.find('l'))  # 2
print(s.find('l',3)) #3
print(s.find('l',4)) # 9
print(s.find('l',10)) # -1
print(s.find('x'))    # -1

6)index(substring, start, end)  # it returns the lowest index in string, where substring is found
                                 returns value error if substring is not found
                                 
s = "Hello world!"
print(s.index('l'))  # 2
print(s.index('l',3)) #3
print(s.index('l',4)) # 9
print(s.index('l',10)) # value error
print(s.index('x'))    # value error   

SRNO    Method      s1 = "abc123"       s2 = "ABC"      s3 = "123"      s4 = "Hello World!"     s5 = " "
7      isalnum()        True                True          True              False                False
8      isalpha()        False               True          False             False                False
9      isdigit()        False               False         True              False                False
10     islower()        True                False         False             False                False
11     isupper()        False               True          False             True                 False
12     isspace()        False               False         False             False                True
13     istitle()        False               False         False             True                 False

14)lower() # returns all the characters in lower case
15)upper() # returns all the characters in upper case
16)swapcase() # swaps the cases upper to lower and lower to upper
17)title()  # returns title cased version of string i.e. each word starts with upper case character and all remaining 
characters in lower case

examples

s = "Hello world!"
print(s.lower()) # hello world!
print(s.upper()) # HELLO WORLD!
print(s.swapcase()) # hELLO WORLD!
print(s.title()))   # Hello World!

18)lstrip(ch=None) # returns copy of the string with leading white space removed
                     if ch's is given and its not a none , it removes characters in ch instead
s="         hello"
s1="hahahahahahah Admin"
print(s.lstrip()) # hello
print(s.lstrip('ha') # Admin

19)rstrip(ch=None) # returns copy of the string with trailing white space removed
                     if ch's is given and its not a none , it removes characters in ch instead
s="         hello              "
s1="Admin hahahahahahaha"
print(s.rstrip()) #  "        hello"
print(s.rstrip('ha') # "Admin "

20)strip(ch=None) # returns copy of the string with leading and trailing white space removed
                     if ch's is given and its not a none , it removes characters in ch instead
s="         hello              "
s1="hahahahahahaha Admin hahahahahahaha"
print(s.strip()) #  "hello"
print(s.strip('ha') # " Admin ")

21)partition(sep) # it partition  into 3 parts using the given separator, this will search for the separator in the string.
                    If the separator is found , it returns 3-tuple containing, the part before the separator, separator itself and the part after the separator.
                    If separator doesnot found , it returns 3-tuple containing,  original string and two empty strings
                    
s = "hello world"
print(s.partition("ll") # ('he' , 'll', 'o world')
print(s.partition('x')  # ('hello world', '' , '')

22)split(sep=None, maxsplit=-1) returns list of words in the string using sep as the delimiter string. 
                                 sep -- its the delimiter according to the split the string, None means split according to white space
                                 maxsplit --- it the maximum number of splits to do.

s ="welcome to python class"
print(s.split()) --['welcome' ,'to', 'python', 'class']
print(s.split('o'))  # ['welc', 'me t', ' pyth', 'n class']
print(s.split('o',2))  # ['welc', 'me t', ' python class']

23) join(iterable) --> it concatenates any number of strings
l =  ['welcome' ,'to', 'python', 'class']
s = " ".join(l)                        
print(s) # "welcome to python class"

24) replace(old_string, new_string, count=-1)   # returns a copy with all occurrences of substring of old replace by new.
                                                  count = it is maximum number of occurrences to replace 
                                                  -1 means replace all
s ="welcome to python class"
print(s.replace("o", "#")) == welc#me t# pyth#n class
print(s.replace("o", "#",2)) == welc#me t# python class

25)format(*args, **kwargs) # returns formatted version of string using substitutions from args and kwargs.
                             The substitutions are identified by {}

age = 25 
name = "python"
# old formatting (using %)
print("Name is %s and age is %d" %(name, age))
#new formatting using (format()
print("Name is {} and age is {}".format(name, age))
#advance formatting-- its available from py >3.5
print(f "name is {name}, and age is {age}")
==========================================================================================================================================================
write a program to eliminate capital letters from user inputted string
 str = input("Enter a string:")
result = ""
for ch in str:
    if ch.isupper():
        pass
    else:
        result += ch
print(result)
==========================================================================================================================================================
write a program to check if strings are relationally equivalent
example 
    gfg 
    fgg
str1 = "gfg"
str2 = "fgg"
str1List = [ch for ch in str1]
str2list = [ch for ch in str2]
print(str1List)
print(str2list)
if len(str1List) == len(str2list):
    if str1List.sort() == str2list.sort():
        print("str1 and str2 are rationally equally")
==========================================================================================================================================================

to find maximum length word
str = "returns capitalized version of string more specifically it makes the first character have upper case and rest have lower case"
str = "returns capitalized version of string more specifically it makes the first character have upper case and rest have lower case"
strlist = str.split()
print(strlist)
max_len = 0
max_len_word = ""
for element in strlist:
    if len(element) > max_len:
        max_len = len(element)
        word = element
print(max_len)
print(word)

==========================================================================================================================================================
position the word in the reverse order
str = "returns capitalized version of string more specifically it makes the first character have upper case and rest have lower case"
strlist = str.split()
print(strlist)
strlist_rev = strlist[::-1]
print(strlist_rev)
str_rev = " ".join(strlist_rev)
print(str_rev)
==========================================================================================================================================================
return the string in the ascending order of the length of the word

str = "returns capitalized version of string more specifically it makes the first character have upper case and rest have lower case"

str_list = str.split()
str_list.sort(key=len)
str_new = " ".join(str_list)
print(str_new)
==========================================================================================================================================================
write a program to capitalize the word in the string
str = "returns capitalized version of string more specifically it makes the first character have upper case and rest have lower case"

def str_capitalize(s):
    return s.title()
str2 = str_capitalize(str)
print(str2)
# str_new = " ".join(str2)
# print(str_new)
==========================================================================================================================================================
remve the elements which are in other list
str = "returns capitalized version of string more specifically it makes the first character have upper case and rest have lower case"
l = ['of', 'the', 'an', 'a', 'have', 'are', 'you', 'is', 'was', 'had']
str_list = str.split()

word = []
for element in str_list:
    if element not in l:
        word.append(element)

new_str = " ".join(word)
print(new_str)
=========================================================================================================================================================
wrp to calculate number of occurrences of each character of a given string and return list of tuple 
exampe of output , dont count space
l = [('T', 1), ('h',1),('e',2) ...]
s = "The quick brown fox jumps over lazy dog"
count = 0
l = []
for ch in s:
    if ch.isspace():
        pass
    else:
        if (ch, s.count(ch)) not in l:
            l.append((ch, s.count(ch)))
print(l)
=========================================================================================================================================================
wrp to reverse a word on its own place from a given string.
s = "The quick brown fox jumps over lazy dog"
l = s.split()
print(l)
for element in range(len(l)):
    l[element] = l[element][::-1]
print(l)
=========================================================================================================================================================
wrp 
s = input("Enter a string:")        #python
n = int(input("enter a number:"))   #3
# output "p1p2p3y1y2y3.....n1n2n3n"
s2 = ""
for ch in s:
    for i in range(1,n+1):
        s2 += ch+str(i)
print(s2)
=========================================================================================================================================================
wrp to eliminate capital letters starting words from the string
s = "The quick Brown fox jumps over lazy Dog"
l = s.split()
for element in l:
    if element.istitle():
        l.remove(element)
print(l)
s1 = " ".join(l)
print(s1)
=========================================================================================================================================================
wrp to return numbers from a given string
s = "g4g no3 in#py3"
s2=""
for ch in s:
    if ch.isdigit():
        s2 += ch
print(s2)
=========================================================================================================================================================
s = "The quick Brown fox jumps over The lazy Dog"
l = s.split()
l2 =[]
for element in l:
     if [element[0]] not in l2:
         l2.append([element[0], element])
     else:
         c = l2.index([element[0], element])
         l2[c].append(element)
print(l2)
=========================================================================================================================================================
s = "The quick Brown fox jumps over The lazy Dog"
n = int(input("Enter number:"))
#output n=2 ['Th' , 'e ', 'qu'   ...]
l =[]
for i in range(0,len(s),n):
    l.append(s[i:i+n])

print(l)
=========================================================================================================================================================
s = "The quick Brown fox jumps over The lazy Dog"
#max occured character from a given string.
max_count= 0
max_count_char = ""
for ch in s:
    if not ch.isspace():
        if s.count(ch) > max_count:
            max_count_char=ch
            max_count =s.count(ch)
print(max_count_char)
=========================================================================================================================================================
s = "The quick Brown fox jumps over The lazy Dog"
count=0
for ch in s:
    if not ch.isspace():
        if ch in 'aeiou':
            count +=1
print(count)
=========================================================================================================================================================
s = "The3quick4Brown5fox6jumps7over8The9lazy9Dog10"
#findout the digits and remove all the digits
#The quick Brown fox
s2=""
sum =0
for ch in s:
    if ch.isdigit():
        s2 += " "
        sum += int(ch)
    else: 
        s2 += ch
print(sum)
print(s2)
=========================================================================================================================================================
"""
