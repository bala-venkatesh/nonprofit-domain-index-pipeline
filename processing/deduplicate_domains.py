import sqlite3

conn = sqlite3.connect("nonprofit.db")
c = conn.cursor()

c.execute("""
CREATE TABLE IF NOT EXISTS nonprofit_domains_dedup AS
SELECT root_domain,
MAX(score) as nonprofit_score,
signals
FROM nonprofit_domains
GROUP BY root_domain
""")

conn.commit()
conn.close()

print("Deduplicated Table Created")
