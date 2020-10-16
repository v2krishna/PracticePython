"""
Regular Expression
====================
Regular Expression
    re,regex=> Pattern matching engine, it search text from inputs(file data, s/m data,many more)
    import re
    Matching Characters:
    1)Meta chars
    The special characters are:
       1)"."     Matches any character except a newline.
       2)"^"     Matches the start of the string.
       3)"$"     Matches the end of the string or just before the newline at
                 the end of the string.
       4)"*"     Matches 0 or more (greedy) repetitions of the preceding RE.
                 Greedy means that it will match as many repetitions as possible.
       5)"+"     Matches 1 or more (greedy) repetitions of the preceding RE.
       6)"?"     Matches 0 or 1 (greedy) of the preceding RE.
       7){m,n}   Matches from m to n repetitions of the preceding RE.m=Lower bound, n=Upper bound
                  r'ab{3}'=>abbb
                  r'a{2,4}b'=>aab,aaab,aaaab
       8)[]      Indicates a set of characters(range)
                    r'[a-e]'=>a,b,c,d,e
                    r'[0-5]'=>0,1,2,3,4,5
                    r'[0-9]'=>0,1,2,3,4,5,6,7,8,9
                    r'[0-5][0-9]'=>00,01,02,03...09,10,11....19,....59
                    +91-997-534-0919
                    r'\+91-[7-9]{1}[0-9]{2}-[0-9]{3}-[0-9]{4}'
                    r'[amk]'=> 'a', 'm','k'

        9)"\"     Either escapes special characters or signals a special sequence(10 10\.11 0\.10)
        10)"|"    r'A|B', creates an RE that will match either A or B.
        11)()    Matches the RE inside the parentheses=>used exact
                r'(amk)'=>'amk'

                 import re
                >>> s='Python Programming'
                >>> re.findall(r'P*',s)
                ['P', '', '', '', '', '', '', 'P', '', '', '', '', '', '', '', '', '', '', '']
                >>> re.findall(r'P+',s)
                ['P', 'P']
                >>> s1='Python Programming PPPPPPPPPP'
                >>> re.findall(r'P+',s1)
                ['P', 'P', 'PPPPPPPPPP']
                >>> re.findall(r'P*',s1)
                ['P', '', '', '', '', '', '', 'P', '', '', '', '', '', '', '', '', '', '', '', 'PPPPPPPPPP', '']
                >>> re.findall(r'P?',s1)
                ['P', '', '', '', '', '', '', 'P', '', '', '', '', '', '', '', '', '', '', '', 'P', 'P', 'P', 'P', 'P', 'P', 'P', 'P', 'P', 'P', '']

    2)Escape chars
        1)\A   Matches begining of string like '^'
        2)\Z   Matches ending of string like '$'
        3)\d   Matches all digits~ [0-9]
        4)\s   Matches whitespace~[\t,\n,\s,\r,\f]
        5)\w   Matches all ascii letters~[A-Za-z0-9_]eg.  s='admin_123'
        6)\b   Matches boundry of words

    Methods of regex
        1)re.search(pattern, string, flags=None)=>It matches pattern into string and returns match object
        2)re.match(pattern, string, flags=None)=>It matches pattern into string if pattern
                                                is at begining of string and returns match object
        3)re.split(pattern,string, maxsplit=-1,flags=None )=>it splits string where pattern matches
                    and returns list

                    s2="abc#def@ghi&bef xyz! pqr"
                    >>> s2="abc#def@ghi&bef xyz!pqr"
                    >>> re.split(r'[@#&!\s]',s2)
                    ['abc', 'def', 'ghi', 'bef', 'xyz', 'pqr']
                    >>> re.split(r'[@#&!\s]',s2,3)
                    ['abc', 'def', 'ghi', 'bef xyz!pqr']

        4)re.findall(pattern,string, flags=None)=>it returns list of matches found
        5)re.sub(pattern, repl, string, counts=-1,flags=None)=>It replace count occurences of pattern by repl
                                    and returns new string
                            >>> re.sub(r'[@#&!]',' ',s2)
                            'abc def ghi bef xyz pqr'
                            >>> re.sub(r'[@#&!]',' ',s2,3)
                            'abc def ghi bef xyz!pqr'
                            >>> re.subn(r'[@#&!]',' ',s2,3)
                            ('abc def ghi bef xyz!pqr', 3)
                            >>> re.subn(r'[@#&!]',' ',s2)
                            ('abc def ghi bef xyz pqr', 4)

    Flags of regex
        1)re.DOTALL=> if this specified '.' will search all char including newline
        2)re.MULTILINE=>if this specified '^,$' will match beginig and end of each line resp.
        3)re.IGNORECASE=>if specified \w|[a-z] will matches upper case also i.e [A-Z]

import re
str = "Cats are  smarter than Dogs"
vowels = re.findall(r'[aeiou]',str,re.IGNORECASE)
print(vowels)

import re
s = "Bob is born on 6 October 2010 at 8:00 AM"
date = re.findall(r'[0-9]+ [a-z]+ [0-9]+',s,re.I)
print(date)
time = re.findall(r'[0-9]+:[0-9]+ [A-Z]+', s, re.I)
print(time)


import re
s = "abc!def@ghi#pqr%xyz&stu vwl"
l = re.split(r'[!@#%&\s]',s)
print(l)

sb = re.sub(r'[!@#%&]',' ',s)
print(sb)

import re
ph = ['+1-937-768-1668', '+1-937-768-345', '+1-637-768-3466', '+91-37-768-3466', '+1-937-768-1669']
vph = []
for i in ph:
    if re.match(r'\+1-[7-9]{1}[0-9]{2}-[0-9]{3}-[0-9]{4}',i):
        vph.append(i)
print(vph)

import re
f =  open('squares.txt')
#print(f.readlines())
d = []
for i in f.readlines():
    l = re.findall(r'\d+',i)
    d.extend(l)
print(d)

import re
f =  open('squares.txt')
#print(f.readlines())
d = []
c=0
for i in f.readlines():
    l = re.findall(r'\d+',i)
    c += int(l[-1])
print(c)

import re
ex_str="Jessica is 15 years old, and Daniel is 27 years old.\
    Edward is 97 years old, and his grandfather, Oscar, is 102."
names = re.findall(r'[A-Z][a-z]+',ex_str)
age = re.findall(r'[0-9]+',ex_str)
print(names)
print(age)

import re
s="rabcdeefgyYhFjkloomnpOeorteeeeet"
vowels = re.findall(r'[aeiou]+',s,re.I)
print(vowels)

import re
s='abc.test@gmail.com, xyz@test.in, test.first@analyticsvidhya.com, first.test@rest.biz'
d = re.findall(r'@\w+\.(\w+)',s)
d1 = re.findall(r'@(\w+)',s)
print(d)
print(d1)

import re
s='Amit 34-3456 12-05-2007, XYZ 56-4532 11-11-2011, ABC 67-8945 12-01-2009'
dt = re.findall(r'[0-9]{2}-[0-9]{2}-[0-9]{4}',s)
print(dt)

import re
s='Amit 34-3456 12-05-2007, XYZ 56-4532 11-11-2011, ABC 67-8945 12-01-2009'
dt = re.findall(r'[0-9]{2}-[0-9]{2}-[0-9]{4}',s)
id = re.findall(r'[0-9]{2}-[0-9]{4}',s)
names = re.findall(r'[A-Z]+',s,re.I)
print(names)
print(id)
print(dt)
"""
import re
s="Customer number: 232454, Date: February 12, 2011"
dt = re.findall(r'Date: (\w+ \w+, \w+)',s)
dt1 = re.findall(r': (.*)',s)
print(dt1)
print(dt)
