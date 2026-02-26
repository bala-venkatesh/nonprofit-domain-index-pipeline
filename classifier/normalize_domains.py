import gzip
import os
import tldextract

file_path = "data/"

root_domains = set()

for fname in os.listdir(file_path):
    if fname.endswith(".wet.gz"):
        wet_file = os.path.join(file_path, fname)

with gzip.open(wet_file, 'rt', errors='ignore') as f:
    for line in f:
        if "WARC-Target-URI" in line:
            url = line.split(": ")[1].strip()
            if ".org" in url:
                ext = tldextract.extract(url)
                domain = ext.domain + "." + ext.suffix
                root_domains.add(domain)

print("Unique Root .org Domains:", len(root_domains))
print(list(root_domains)[:20])
