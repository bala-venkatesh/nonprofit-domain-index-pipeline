import gzip

file_path = "data/"  # folder path

import os
for fname in os.listdir(file_path):
    if fname.endswith(".wet.gz"):
        wet_file = os.path.join(file_path, fname)

print("Reading:", wet_file)

with gzip.open(wet_file, 'rt', errors='ignore') as f:
    count = 0
    for line in f:
        print(line.strip())
        count += 1
        if count == 100:
            break
