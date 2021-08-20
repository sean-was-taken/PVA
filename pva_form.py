import re

# read entries
with open("entries.txt", "r") as d:
    entries = d.read()

# preprocessing
tmp = re.findall(f'\d+', entries)
tmp = list(map(int, tmp))
tmp = list(filter(lambda i: i > 1000 and i < 1000000000000000, tmp))
entries = []

# extract entries
for x in range(1, len(tmp), 2):
    entries.append(tmp[x])
print(entries)

responce = {
    "First Name": "your firstname here",
    "Last Name": "your lastname here",
    "Student Number": "student number here",
}

parser = {
    "First Name": entries[0],
    "Last Name": entries[1],
    "Student Number": 205099
}
url = "https://docs.google.com/forms/d/e/1FAIpQLSdBkt1jwgWZgpxhKUdQUM9S3Gn5qzXKJrtW0_HZbPAJaOeo5w/viewform?"
for name, code in parser.items():
    url += f"entry.{code}={responce.get(name)}&"

print(url)

