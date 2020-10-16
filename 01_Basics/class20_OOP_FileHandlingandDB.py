"""
Filehandling
class File:
    def __init__(self):
        self.f = open('test.txt','a+')

    def WriteInto(self,text):
        self.f.write(text)
        self.f.flush()
    def ReadFrom(self):
        self.f.seek(0)
        for i in self.f.readlines():
            print(i)

obj = File()
obj.WriteInto('my name is krisha')
print('')
obj.ReadFrom()

"""
import sqlite3
class Database:
    def __init__(self):
        self.con = sqlite3.connect('OOPDB.db')
        self.cur = self.con.cursor()

    def create_table(self):
        self.cur.exceute('delete from table employee')
        self.cur.execute('Create table employee (Id int, Name text, Age int, Salaary real)')

    def insert_data(self):
        self.cur.execute('Insert into employee (Id, Name, Age, Salaary) values (1, "kris", 23, 10000)')
        self.con.commit()

    def read_from(self):
        self.cur.execute('Select * from employee')
        print(self.cur.fetchall())

db = Database()
#db.create_table()
db.insert_data()
db.read_from()
