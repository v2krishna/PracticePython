"""
Object Oriented Programming:
============================
Its a programming style to write a program which contains classes , objects , methods
under single block.
OP is generally used to perform different kinds of functionality under single block.
Difference between OP vs procedural oriented programming
=========================================================

POP                                                 OP
This follows procedures                            This allows access to randomly any kind of functions
will not allow access randomly

It follows top down approach                       It follows bottom-up approach

it consumes more memory than OOP                   it consumes less memory

OOP Attributes:
================
class: Its user-defined data structure which can perform multiple functionalities under single block.
       Classes may have methods, objects , attributes.

Methods: Methods are dependent on classes, they look similar like functions with single parameter
          "self"
         One class method cannot be used for another class

Object: Objects are the variables which can initialize class with instance variables, objects are generally
        used to perform/access methods of the class.
        can declare multiple objects for single class.

self: Its similar like "this" keyword in java/c++, but its not a keyword , its normal parameter
      which can be used for point the current instance of a class

__init__: Its a class initializer method which can initialize objects of the class and instance
          variable. This is alternatively known as dundor method.
          this method is a constructor for the class in python

class variables: These are declared outside of instance method, but under class.
                These variables can be accessed with object of the class, as well as class name.
                These variables behave similar with all the instances/objects of the class

instance variables: These are declared within init method. These variables are accessed only with
                   object of the class.
                   It cannot be accessed with class name.
                   These variables behaves differently with different objects of the class.

Pillars of OOPS:
================
1) Inheritance: Accessing all/some properties of base class in derived class.
               Allows us to re-used the code(DRY-- Dont Repeat Yourself)
     Types of Inheritances:
    1) Single Inheritance
    2) Multiple Inheritance
    3) Multi-level Inheritance
    4) Hierarchial Inheritance
    5) Hybrid Inheritance

2)Encapsulation: Binding of data together and give it protection. The Protection can be given properties like
                public private protected.

3)Data Abstraction: Hiding unnecessary information and showing  only needed information.
                    Abstraction always comes with encapsulation.
                    It hides information using public private protected properties of the encapsulation.
4) Polymorphism: Single method may have multiple functionalities.
                 polymorphism can be achieved using below properties
                 1) Method Overloading
                 2) Method Overriding


class Demo:
    name = "Python"
    def __init__(self,a,b):
        self.a = a
        self.b = b
    def display(self):
        print("Accessing class variables within class")
        print("Using class Name:", Demo.name)
        print("Using instance variables:", self.name)
        print("Accessing instance variables within class")
        print("Using instance Name:", self.a , self.b)
        # print("Using class Name:", Demo.a)

obj = Demo(10,20)
obj.display()

obj1 = Demo('Hi','bye')
obj1.display()

=======================

class Demo:
    name = "Python"
    def __init__(self,name, age):
        self.name = name
        self.age = age
    def display(self):

        print("Name Ambiguity")
        print(self.name) # it gives instance variable  as we are accessing using instance
        print(Demo.name) # it gives class variables as we are accessing class name

obj = Demo('RK',35)
obj.display()
===============================


"""

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def display(self):
        print(f"Name: {self.name} \n Age: {self.age}")

class Employee(Person):
    def __init__(self,name,age, id, salary):
        Person.__init__(self, name,age)
        self.id = id
        self.salary = salary
    def display(self):
        print(f"ID:{self.id}")
        Person.display(self)
        print(f"Salary: {self.salary}")

emp = Employee('RK',20, 1, 10000)
emp.display();

