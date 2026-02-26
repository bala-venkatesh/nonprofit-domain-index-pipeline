import sqlite3

conn = sqlite3.connect("nonprofit.db")
c = conn.cursor()

c.execute("""
CREATE TABLE IF NOT EXISTS nonprofit_domains(
root_domain TEXT,
score INT,
signals TEXT
)
""")

print("Database & Table Created")

conn.commit()
conn.close()
