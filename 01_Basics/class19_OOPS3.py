"""
Encapsulation
=============
name = "public"
_name = "protected"
__name = "private"
"""
class Demo:
    def __init__(self):
        self.name = "public"
        self._age = "protected"
        self.__year = "private"

    def display(self):
        print(self.name)
        print(self._age)
        print(self.__year)

    def __view(self):
        print("This is private method")
obj = Demo()
obj.display()

print('Acccessing from outside of the class')
print(obj.name)
print(obj._age)
#print(obj.__year) # it will raise error


#to access private variables /members of the class use 'object._classname__variablename'
print(obj._Demo__year)

#obj.__view()
obj._Demo__view()
