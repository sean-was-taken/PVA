import urllib.request

# url of form. 
form = "https://docs.google.com/forms/d/e/1FAIpQLSdBkt1jwgWZgpxhKUdQUM9S3Gn5qzXKJrtW0_HZbPAJaOeo5w/viewform?"

with urllib.request.urlopen(form) as page:
    data = page.read().decode('urf-8')

print(data)
exit(1)
responce = {
    "First Name": "your firstname here",
    "Last Name": "your lastname here",
    "Student Number": "student number here",
}
# need to add javascript parser to automatically update the codes
codes = {
    "First Name": 911369318,
    "Last Name": 1500907496,
    "Student Number": 2050994802
}
for name, code in codes.items():
    page += f"entry.{code}={responce.get(name)}&"

print(page)

