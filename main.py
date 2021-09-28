import re, json
import argparse

def main(autosubmit, source, values, url):
    
    responce = json.load(open(values, "r"))

    # read entries
    with open(source, "r") as d:
        entries = d.read()

    # preprocessing
    tmp = re.findall(f'\d+', entries)
    tmp = list(filter(lambda i: i > 1000 and i < 1000000000000000, list(map(int, tmp))))

    # extract entries
    entries = []
    for x in range(1, len(tmp), 2):
        entries.append(tmp[x])
        
    if autosubmit: url += "formResponse?"
    else: url += "viewform?"

    for x in range(len(entries)+1):
        if x < len(list(responce.values())):
            url += f"entry.{entries[x]}={list(responce.values())[x]}&"
    return url

if __name__ == "__main__":
    parser=argparse.ArgumentParser(description="Simple script to generate a url for PVA attendance form")
    parser.add_argument("-s", "--source", action="store", default="source.txt", help="source code for form webpage")
    parser.add_argument("-v", "--values", action="store", default="values.json", help="values to insert into url")
    parser.add_argument("-u", "--url", action="store", default="https://docs.google.com/forms/d/e/1FAIpQLSdBkt1jwgWZgpxhKUdQUM9S3Gn5qzXKJrtW0_HZbPAJaOeo5w/", help="url to form")
    parser.add_argument("-a", "--autosubmit", action="store", default=False, help="auto submit the form without user action")
    parser.add_argument("-o", "--output", action="store", default="stdout", help="file to write to, stdout for print to terminal")
    s,v,u,a=parser.parse_args().source, parser.parse_args().values, parser.parse_args().url, parser.parse_args().autosubmit
    returnvalue = main(a,s,v,u)
    o=parser.parse_args().output
    if not o == "stdout":
        with open(o, "w") as output_file:
            output_file.write(returnvalue)
            output_file.close()
    else:
        print(returnvalue)
