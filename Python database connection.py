import mysql.connector

mydb = mysql.connector.connect(host="localhost",user="root",passwd="Kumar@8887", database="amit")

mycursor=mydb.cursor()
mycursor.execute("select * from NIT")
for i in mycursor:
    print(i)