import gzip
import os
import tldextract
import sqlite3

file_path = "data/"

signals = {
    "501(c)(3)": 5,
    "nonprofit": 3,
    "charity": 2,
    "donate": 2,
    "foundation": 2,
    "mission": 1
}

conn = sqlite3.connect("nonprofit.db")
c = conn.cursor()

for fname in os.listdir(file_path):
    if fname.endswith(".wet.gz"):
        wet_file = os.path.join(file_path, fname)

with gzip.open(wet_file, 'rt', errors='ignore') as f:

    current_url = None
    page_text = ""

    for line in f:

        if line.startswith("WARC-Target-URI"):

            # Process previous page first
            if current_url and ".org" in current_url:

                score = 0
                found = []

                for keyword, value in signals.items():
                    if keyword in page_text:
                        score += value
                        found.append(keyword)

                if score > 0:
                    ext = tldextract.extract(current_url)
                    root = ext.domain + "." + ext.suffix

                    c.execute("""
                    INSERT INTO nonprofit_domains(root_domain,score,signals)
                    VALUES (?,?,?)
                    """,(root,score,str(found)))

            # Start new page
            current_url = line.split(": ")[1].strip()
            page_text = ""

        else:
            page_text += line.lower()

conn.commit()
conn.close()

print("Nonprofit domains stored successfully in DB")
