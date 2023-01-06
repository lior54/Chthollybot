import sqlite3
conn = sqlite3.connect("data.db")

conn.execute('insert into users(server,user,options) values("test", "big", "options");')
print("added succesfuly")
conn.commit()
conn.close()