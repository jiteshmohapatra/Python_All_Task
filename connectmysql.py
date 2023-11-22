#For mysql connectivity yoy need to install mysqlclient and mysql installer in python

import mysql.connector
'''
mycon = mysql.connector.connect(host="localhost",user="root",passwd="Nsti123")
if mycon.is_connected:
    print("successfully connected")
cur = mycon.cursor()
cur.execute("CREATE DATABASE ibmadit")'''

'''mycon=mysql.connector.connect(host="localhost",user="root",passwd="Nsti123",database="ibmadit")

str = "CREATE TABLE software(Software_id integer(20),Dept_Name varchar(25),Employe_Name varchar(25),salary integer(20),Ratings float(5,2))"
cur = mycon.cursor()
cur.execute(str)'''



# how to insert data multiple data 
# to the databases


'''mycon = mysql.connector.connect(host="localhost",user="root",passwd="Nsti123",database="ibmadit")
str = "INSERT INTO software(Software_id,Dept_Name,Employe_Name,salary,Ratings)VALUES(%s,%s,%s,%s,%s)"
b1 = [(101,"Ai","peter",50000,4.2),(102,"Web_devlopment","harry",60000,4.1),(103,"Android Devlopment","morgan",65000,4.5),(104,"cloud_practioner","chess",49000,4.7),(105,"django-devloper","maya",55000,4.1)]
cur = mycon.cursor()
cur.executemany(str,b1)
mycon.commit()'''


#how to extracting the data

'''
mycon = mysql.connector.connect(host="localhost",user="root",passwd="Nsti123",database="ibmadit")
str = "SELECT * FROM software"
cur = mycon.cursor()
cur.execute(str)
result = cur.fetchall()
for res in result:
    print(res)
'''


#How to update the data

'''
mycon = mysql.connector.connect(host="localhost",user="root",passwd="Nsti123",database="ibmadit")
str = "UPDATE software set salary = salary-5000 WHERE salary>45000"
cur = mycon.cursor()
cur.execute(str)
mycon.commit()'''

# how to delete the data from database

mycon = mysql.connector.connect(host="localhost",user="root",passwd="Nsti123",database="ibmadit")
str = "DELETE FROM software WHERE Employe_Name ='maya'"
CUR = mycon.cursor()
CUR.execute(str)
mycon.commit()
