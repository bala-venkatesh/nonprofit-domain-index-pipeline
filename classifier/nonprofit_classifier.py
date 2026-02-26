import gzip
import os
import tldextract

file_path = "data/"

signals = {
    "501(c)(3)": 5,
    "nonprofit": 3,
    "charity": 2,
    "donate": 2,
    "foundation": 2,
    "mission": 1
}

results = []

for fname in os.listdir(file_path):
    if fname.endswith(".wet.gz"):
        wet_file = os.path.join(file_path, fname)

with gzip.open(wet_file, 'rt', errors='ignore') as f:
    current_url = ""
    current_text = ""

    for line in f:

        if "WARC-Target-URI" in line:
            current_url = line.split(": ")[1].strip()
            current_text = ""

        elif line.strip() == "":
            continue

        else:
            current_text += line.lower()

        if current_url and ".org" in current_url:
            score = 0
            found = []

            for keyword, value in signals.items():
                if keyword in current_text:
                    score += value
                    found.append(keyword)

            if score > 0:
                ext = tldextract.extract(current_url)
                root = ext.domain + "." + ext.suffix
                results.append((root, score, found))

print("Detected Nonprofit Candidates:", len(results))
print(results[:20])
