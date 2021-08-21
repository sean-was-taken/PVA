import re, json
responce = json.load(open("entries.json", "r"))

# use autosubmit = True for auto submit
autosubmit = False


# read entries
with open("entries.txt", "r") as d:
    entries = d.read()

# preprocessing
tmp = re.findall(f'\d+', entries)
tmp = list(filter(lambda i: i > 1000 and i < 1000000000000000, list(map(int, tmp))))

# extract entries
entries = []
for x in range(1, len(tmp), 2):
    entries.append(tmp[x])

url = "https://docs.google.com/forms/d/e/1FAIpQLSdBkt1jwgWZgpxhKUdQUM9S3Gn5qzXKJrtW0_HZbPAJaOeo5w/"
if autosubmit: url += "formresponce?"
else: url += "viewform?"

for x in range(len(entries)+1):
    if x < len(list(responce.values())):
        url += f"entry.{entries[x]}={list(responce.values())[x]}&"
    

print(url)

