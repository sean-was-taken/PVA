base_url = "https://docs.google.com/forms/d/e/1FAIpQLSdBkt1jwgWZgpxhKUdQUM9S3Gn5qzXKJrtW0_HZbPAJaOeo5w/viewform"

responce = {
    "First Name": "Xinle",
    "Last Name": "Yao",
    "Student Number": "109018",
    "Success": "Yes"
}
codes = {
    "First Name": 911369318,
    "Last Name": 1500907496,
    "Student Number": 2050994802,
    "Success": 243311362
}
append_url = "?"
for name, code in codes.items():
    append_url += "entry."
    append_url += str(code)
    append_url += "="
    append_url += responce.get(name)
    append_url += "&"

print(base_url + append_url)

