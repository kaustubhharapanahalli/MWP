import sqlite3

con = sqlite3.connect("books_db.sqlite3")
cur = con.cursor()

try:
	cur.execute("CREATE TABLE books (id INTEGER PRIMARY KEY, name TEXT, rating REAL)")
except sqlite3.OperationalError:
	print("Table Already exists...")

cur.execute("""INSERT INTO books VALUES(1, "Deep Learning", 4.5)""")
cur.execute("""INSERT INTO books VALUES(2, "The One Thing", 4.2)""")
cur.execute("""INSERT INTO books VALUES(3, "Machine Learning", 4.3)""")

con.commit()