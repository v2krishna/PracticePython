"""
Exception Handling
==================
Error -- when it occurs at compile time.
Exception -- occurs at run-time

try      -->  we write suspicious code within this statements or clause
except   -->  this block executes only if there's exception occured in try block, single try block may have multiple except clauses
              we can use except clause to handle individual or multiple exceptions at a time.
else    -->   This block exceutes only if there's no exception occured in try block,
              we can use only single else block per try block
finally -->   This block executes anyhow that is may or may not error occured, it executes
raise   -->   This statement raises an exception which can be handled by except clause.

l = [0, 0.7, 'high', 2]

for i in l:
    print("i is {}".format(i))
    try:
        c = 1/int(i)
    except ZeroDivisionError as Z:
        print(Z)
    except ValueError as V:
        print(V)
    else:
        print("This is else block")
        print(c)
    finally:
        print("This is finally block")
===============================================================
n numbers average
import sys

tot= 0
count=0
while True:
    num = input("Please enter number or No to break: ")
    if num =='No':
        break
    else:
        try:
            tot += float(num)
            count +=1
        except:
            print(sys.exc_info()[0])
        else:
            print("This is else block")
        finally:
            print("This is final block")
avg = tot/count
print("Average is {}".format(avg))
===============================================================
import sys
def throw():
    raise  RuntimeError("This is the error")
try:
    throw()
except:
    print(sys.exc_info()[0])

===============================================================
try:
    a = 10/0
    print(a)
except:
    print(sys.exc_info()[0])
===============================================================
import sys
try:
    a = int(input('a value:'))
    b = int(input('b value:'))
    assert a==b, 'Value mismatch'
except:
    print(sys.exc_info()[0])
===============================================================
import sys
try:
    print("Press return or control plus C")
    ignore = input("Enter")
except:
    print(sys.exc_info()[0])
===============================================================
import sys
try:
    exec('1+10')
except:
    print(sys.exc_info()[0])
===============================================================
s = "abcd"
it = iter(s)
for i in range(5):
    try:
        print(next(it))
    except StopIteration as st:
        print('Stop Iteration')
===============================================================
"""
