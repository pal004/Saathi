import sqlite3
conn = sqlite3.connect("maitri.db")
cur = conn.cursor()
cur.execute("DROP TABLE IF EXISTS conversations;")
conn.commit()
conn.close()
print("Dropped old conversations table.")
