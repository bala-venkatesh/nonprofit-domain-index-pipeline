import sqlite3
import csv

conn = sqlite3.connect("nonprofit.db")
c = conn.cursor()

c.execute("SELECT * FROM nonprofit_domains_dedup")

rows = c.fetchall()

with open("output/nonprofit_domains.csv", "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerow(["root_domain","nonprofit_score","signals"])
    writer.writerows(rows)

conn.close()

print("CSV Exported Successfully")
