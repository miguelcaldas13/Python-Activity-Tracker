import sqlite3

conn = sqlite3.connect("physical.db")

cur = conn.cursor()

cur.execute("""DROP TABLE IF EXISTS activities""")

cur.execute("""CREATE TABLE IF NOT EXISTS activities 
(
id INTEGER PRIMARY KEY,
date DATE,
description TEXT,
category TEXT,
total_distance INT,
total_steps INT,
kcal_burned INT
)
""")

conn.commit()
conn.close()