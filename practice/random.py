import sqlite3
import os
import random

con=sqlite3.connect("C:\\Users\\CJCU-CC\\Downloads\\DB.Browser.for.SQLite-3.12.2-win64\\DB Browser for SQLite\\Book.sqlite")

al=con.execute("SELECT * FROM book")


    

sql="INSERT INTO book (id,title,price) VALUES"
for i in range(50,10000):
    title ="title" +str(random.randint(1, 100))
    price=random.randint(100, 10000)
    sql +="(\'"+str(i)+"\',\'"+title+"\',"+str(price)+"),"
sql=sql[:-1]
print(sql)
cc=con.execute(sql)
print(cc.rowcount)
con.commit()
con.close()
    

'''
con.commit()

for row  in al:
    for i in range(len(row)):
        print(str(row[i])+" ",end="")
    print("\n")
con.close()'''