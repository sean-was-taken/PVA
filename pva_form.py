import re, json
# replace the following values with the information you wish to send to the form. 
responce = json.read(open("entries.json", "r"))

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
#print(entries)

parser = {
    "First Name": entries[0],
    "Last Name": entries[1],
    "Student Number": entries[2],
    "Grade Level": entries[3],
    "unwanted classes": entries[4],
    "another school": entries[5]
}
url = "https://docs.google.com/forms/d/e/1FAIpQLSdBkt1jwgWZgpxhKUdQUM9S3Gn5qzXKJrtW0_HZbPAJaOeo5w/"
if autosubmit: url += "formresponce?"
else: url += "viewform?"

for name, code in parser.items():
    url += f"entry.{code}={responce.get(name)}&"

print(url)

