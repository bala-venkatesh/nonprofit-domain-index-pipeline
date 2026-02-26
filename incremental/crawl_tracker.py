import os

tracker_file = "last_processed.txt"
new_crawl = "CC-MAIN-2024-18"

if not os.path.exists(tracker_file):
    with open(tracker_file, "w") as f:
        f.write("NONE")

with open(tracker_file, "r") as f:
    last_crawl = f.read().strip()

print("Last Processed:", last_crawl)
print("New Crawl:", new_crawl)

if last_crawl == "NONE" or new_crawl != last_crawl:
    print("Processing new crawl...")
    with open(tracker_file, "w") as f:
        f.write(new_crawl)
else:
    print("Crawl already processed. Skipping...")
