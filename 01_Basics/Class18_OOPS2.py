"""
Polymorphism and Inheritance
"""
#
class CollegeMember:
    def __init__(self,id, name, age):
        self.id = id
        self.name = name
        self.age = age

    def display(self):
        print(f"ID:{self.id}")
        print(f"Name:{self.name}")
        print(f"Age:{self.age}")

class Teacher(CollegeMember):
    def __init__(self,id,name,age,subject,salary,exp):
        CollegeMember.__init__(self,id,name,age)
        self.subject =subject
        self.salary=salary
        self.exp = exp

    def display(self):
        CollegeMember.display(self)
        print(f"subject:{self.subject}")
        print(f"salary:{self.salary}")
        print(f"experience: {self.exp}")


class Student(CollegeMember):
    def __init__(self,id,name,age,year,marks):
        CollegeMember.__init__(self,id, name, age)
        self.year = year
        self.marks = marks

    def display(self):
        CollegeMember.display(self)
        print(f"year:{self.year}")
        print(f"marks:{self.marks}")

std = Student(10,'Kris',30,'second year','87%')
std.display()

teach = Teacher(11,'Rama', 45, 'Maths', 10000, 15)
teach.display()
