import gzip
import os

file_path = "data/"

org_urls = []

for fname in os.listdir(file_path):
    if fname.endswith(".wet.gz"):
        wet_file = os.path.join(file_path, fname)

with gzip.open(wet_file, 'rt', errors='ignore') as f:
    for line in f:
        if "WARC-Target-URI" in line:
            url = line.split(": ")[1].strip()
            if ".org" in url:
                org_urls.append(url)

print("Total .org URLs:", len(org_urls))
print(org_urls[:20])
