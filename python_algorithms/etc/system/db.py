import sqlite3

db = sqlite3.connect("database.db")

# to do anything create a cursor
c = db.cursor()
c.execute("create table portfolio (symbol text. shares integer, price real)")
db.commit()

# insert sequence
c.executemany("insert into portfolio values (?,?,?)", stocks)
db.commit()

# query
for row in db.execute("select * from portfolio"):
    print(row)

min_price = 100
for row in db.execute("select * from portfolio where price >= ?", (min_price,)):
    print(row)
