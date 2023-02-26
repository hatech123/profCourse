import sqlite3
con= sqlite3.connect("people.db")
cursor=con.cursor()
# cursor.execute("CREATE TABLE my_table (id INTEGER PRIMARY KEY AUTOINCREMENT, name TEXT, age INTEGER)")
# cursor.execute("INSERT INTO my_table (name,age) VALUES ('Dima', 13)")
# people=[('Bob', 72),('Dod', 103), ('Gog',154)]
# cursor.executemany("INSERT INTO my_table (name,age) VALUES (?, ?)", people)
#
#
# con.commit()
# cursor.execute("SELECT * FROM my_table")
# x=cursor.fetchall()
# print(x)

# cursor.execute("SELECT name, age FROM my_table WHERE id=3")
# name,age=cursor.fetchone()
# print((name,age))

cursor.execute("UPDATE my_table SET name='Petr' WHERE name='Dod'")
con.commit()