import pymysql

conn = pymysql.connect(user="root",\
                       password ="Rani0518",\
                       host ="127.0.0.1",\
                       port=3306,\
                       database="mysql")
c = conn.cursor()
# c.execute("SELECT VERSION()")
# data =  c.fetchone()
# print(f'database version is: {data}')

def create_table():
    c.execute("create table example (Id int, Name text, Age  int, Salaray real)")

create_table()
def insert_data():
    c.execute("insert into example (Id , Name, Age , Salaray) values (1 , 'Rama', 23, 100.00)")
    conn.commit()

insert_data()

def read_data():
    c.execute("select * from example")
    print(c.fetchall())
read_data()

