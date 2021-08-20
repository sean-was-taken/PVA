base_url = "https://docs.google.com/forms/d/e/1FAIpQLSdBkt1jwgWZgpxhKUdQUM9S3Gn5qzXKJrtW0_HZbPAJaOeo5w/viewform?"

responce = {
    "First Name": "your firstname here",
    "Last Name": "your lastname here",
    "Student Number": "student number ere",
}
# need to add javascript parser to automatically update the codes
codes = {
    "First Name": 911369318,
    "Last Name": 1500907496,
    "Student Number": 2050994802
}
for name, code in codes.items():
    base_url += f"entry.{code}={responce.get(name)}&"

print(base_url)

