import mysql.connector

db1=mysql.connector.connect(host="localhost", user="root", password="Kumar@8887" , database="demodatabase1")

mycursor=db1.cursor()

# mycursor.execute("show databases")

# mycursor.execute("create database demodatabase1")

# mycursor.execute("create table demotable1(SI int,fullname text)")

# mycursor.execute("""insert into demotable1(SI,fullname) values(2,'Shoaib Anshari')""")
# mycursor.execute("""insert into demotable1(SI,fullname) values(3,'Prasanta Kumar Sethy')""")

# db1.commit()    ## You have to commit at the end to save all your changes and show to everyone . 

# mycursor.execute("insert into demotable1(SI,fullname) values(4,'Priyarajan Nayak')")
# db1.commit()

# mycursor.execute("update demotable1 set fullname='Akash Rout' where SI=2")
# db1.commit()

# mycursor.execute("alter table demotable1 add column(address text)")
# db1.commit()

# mycursor.execute("update demotable1 set address='Keonjhar' where SN=1")
# db1.commit()

# mycursor.execute("update demotable1 set address='Bhadrak' where SN=2")
# mycursor.execute("update demotable1 set address='Nayagarh' where SN=3")
# mycursor.execute("update demotable1 set address='Kendrapada' where SN=4")
# db1.commit()

# mycursor.execute("select fullname from demotable1 where SI=3 ")
# alldata=mycursor.fetchone()

# mycursor.execute("alter table demotable1 rename column SI to SN")
# db1.commit()

# for data in alldata:
#     print(data)

mycursor.execute("select * from demotable1")
alldata=mycursor.fetchall()

for data in alldata:
    print(data)