"""
tuple:
    tuple is ordered collection of immutable data type.
    Tuples are quiet similar to lists but the difference is tuples are immutable , where lists are mutable

    Basic Operations on tuple
    tpl = ()
    tpl = (1,3,4,'Hi')
    tpl = (1,)  tuple with single element have to pass trailing comma

    Methods
    1) count(val) --> returns number of occurrences of given val in a tuple

    2) index(val,start, stop) --> returns the first index of the given value in a tuple
      It raises value error if value is not present.

t = ([],[])
for i in range(int(input("Enter how many coordinates:"))):
    x = int(input("Enter x coordinates:"))
    y = int(input("Enter y coordinates:"))
    t[0].append(x)
    t[1].append(y)

print(t)


"""


