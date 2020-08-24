"""
DDL
    CREATE
    DROP
    TRUNCATE
DML
    SELECT
    DELETE
DCL
    GRANT
    REVOKE
JOINS
    INNER JOIN
    LEFT JOIN
    RIGHT JOIN
    FULL OUTER JOIN
    CROSS JOIN
CORRELATED
ANALYTICAL FUNCTIONS
    RANK
    MAX     OVER ()
    MIN     OVER ()
    SUM()   OVER ()

sqlite3 --> DB API interface for sqllite databases
SQLite is a C library that provides light weight disk based database that doesn't require separate process and allows
accessing the database using a non-standard variant of the sql query language

To use the sqlite3 module you must first create connection object that represents the database.

import sqlite3
conn = sqlite3.connect("DBName.db")

Methods of connection Object
=============================
1) conn.cursor(factory=cursor) This method accepts signal from sql query result and makes changes into databases
and returns an instance of cursor

2)conn.commit() --> This method commits the current transaction, if you dont call this method anything you need
since the last call to commit is not visible from other db connections.

If you wonder , why you don't see the data you've written to the database, please check you  didnt forget to call this method.

3)conn.close() -->  this closes the db connection. Note that this method doesn't automatically call commit.
If you just close your db connection, without calling to commit first your changes will be lost.

4)conn.rollback() --> This method rollsback any changes to the database since the last call to commit


Methods of cursor object
========================
1) execute(sql,parameters) --> This method executes an sql statement.
         the sql statement may be parameterized, that is place holders instead of sql literals. The sqlite3 modules supports
         two kinds of place holders, a --> ? , b --> named place holders

2)fetchall() --> It fetches all rows from the query result and returning as a list. Note that the cursors array size attribute can effect the
                 performance of this operation. an empty result is returned when no more rows are available.

3)close()  --> This will close the cursor object, a ProgrammingError exception will be raised if any operation is attempted with the cursor

sqlite3 datatypes
==================
python type             sqlite type
None                       NULL
int                        int
float                      real
str                        text
bytes                      blob

"""

import sqlite3, random, time
conn = sqlite3.connect("mysqldb1.db")
c = conn.cursor()
def create_table():
    c.execute("create table example (Id int, Name text, Age  int, Salaray real)")

# create_table()
def insert_data():
    c.execute("insert into example (Id , Name, Age , Salaray) values (1 , 'Rama', 23, 100.00)")
    conn.commit()

# insert_data()

def read_data():
    c.execute("select * from example")
    print(c.fetchall())
#read_data()

def dynamic_entries():
    id1 = random.randint(2,51)
    n   = random.choice(['krishna','rama','Haan','kris','chris'])
    a   = random.randint(23,65)
    s   = random.randint(1000, 50000)
    c.execute("insert into example (Id , Name, Age , Salaray) values (?, ?, ?,?)", (id1, n , a, s))
    conn.commit()

# for i in range(int(input("Enter a no of entries:"))):
#     dynamic_entries()
#     time.sleep(2)
#

def create_table2():
    c.execute("create table colors (Id int, color text)")

def dynamic_entries():
    id1 = random.randint(2,51)
    n   = random.choice(['red','green','blue','white'])

    c.execute("insert into colors (Id , color) values (?, ?)", (id1, n ))
    conn.commit()

# create_table2()

# for i in range(int(input("Enter a no of entries:"))):
#     dynamic_entries()
#     time.sleep(2)


def left_join():
    c.execute("select * from example e left outer join colors c on e.Id = c.Id ")
    print(c.fetchall())

# left_join()

# def right_join():
#     c.execute("select * from example e right inner join colors c on e.Id = c.Id ")
#     print(c.fetchall())
# right_join()

# def semi_join():
#     c.execute("select * from example e where exists (select  1 from colors c where e.Id = c.Id )")
#     print(c.fetchall())
# semi_join()

# def inner_join():
#     c.execute("select * from example e inner join colors c on e.Id = c.Id ")
#     print(c.fetchall())
# inner_join()

# def anti_semi_join():
#     c.execute("select * from example e where not exists (select 1 from colors c where c.Id = e.Id)")
#     print(c.fetchall())
# anti_semi_join()

# def full_outer_join():
#     c.execute("select * from example e full outer join colors c on e.Id = c.Id")
#     print(c.fetchall())
# full_outer_join()


# def cross_apply_function():
#     c.execute("select * from example e cross c apply colors c(e.Id)")
#     print(c.fetchall())
# cross_apply_function()
