import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="sql_learn"
)

db = mydb.cursor()

#Insert data into database
"""
sql = 'insert into users (name, email, password) values (%s, %s, %s)'
values = ('Admin', 'admin@mail.com', 'admim')

db.execute(sql, values)

mydb.commit()

print(db.rowcount, "record inserted.")
"""

#Get all records
"""
db.execute('select * from users')

myresult = db.fetchall()

for x in myresult:
    print(x)
"""

db.execute('drop table replies')
db.execute('drop table comments')
db.execute('drop table posts')