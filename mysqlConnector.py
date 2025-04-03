import mysql.connector as sqlcon

# connecting to database succefully 
con=sqlcon.connect(host='localhost',user='root',password='')
print(con)

# creating cursor 
mycursor=con.cursor()


# showing databases available in mysql
# mycursor.execute("Show Databases")
# for i in mycursor:
#     print(i)

# creating  student database 
# DBS=mycursor.execute("create database studentDatabase")

mycursor.execute("USE studentDatabase")

mycursor.execute("SHOW TABLES")
for i in mycursor:
    print(i)

#Create Operations (DB,Tables)

# mycursor.execute("""CREATE TABLE STUDENT (id int auto_increment primary key,
#         name text,
#         age int,
#         joining_date date,
#         class_id int unique)""")



# Inserting Single Row 
"""

sql="insert into student (name,age,joining_date,class_id)values(%s,%s,%s,%s)"
mycursor.execute(sql,("lavanya","24",'2024-11-18',"2"))

"""

# Inserting multiple rows 
"""
sql="insert into student (name,age,joining_date,class_id) values (%s,%s,%s,%s)"
vals=[
    ("Nitish","25","2018-1-5","1"),
    ("Yash","19","2020-8-12","4")
]
mycursor.executemany(sql,vals)
con.commit()
"""

# inserting with user defined input
"""
name=input("enter name ")
age=input("enter age ")
joining_date=input("enter date ")
class_id=input("enter class ID ")

sql="insert into student(name,age,joining_date,class_id) values(%s,%s,%s,%s)"

vals=(name,age,joining_date,class_id)
mycursor.execute(sql,vals)
con.commit()"
"""


# select statement
mycursor.execute("Select * from student")
tabledata=mycursor.fetchall()
for i in tabledata:
    print(i)


#updated
"""
mycursor.execute("update student set joining_date='2020-18-12' where id=3")
con.commit()
"""


#delete 
# mycursor.execute("delete from student where id=3")


#drop table
# mycursor.execute('create table student_copy select * from student')
# mycursor.execute("drop table student_copy")
# mycursor.execute("Select * from student_copy")
# tabledata=mycursor.fetchall()
# for i in tabledata:
#     print(i)

mycursor.execute("Select * from student")
tabledata=mycursor.fetchall()
for i in tabledata:
    print(i)







