# pandas is better, but here are the python basics of processing raw data
import csv
import json
from pprint import pprint

data = open("data/bank_data.csv")

reader = csv.DictReader(data)


def output_json():
    json_data = json.dumps([row for row in reader], indent=4)
    # other options - load into database, feed api, etc.
    with open("data/banks.json", "w") as file:
        file.write(json_data)


def output_xml():
    xml = ['<?xml version="1.0" encoding="UTF-8">']
    xml.append("<banks>")
    for row in reader:
        xml.append("    <bank>")
        for k, v in row.items():
            xml.append(f"    <{k}>{v}</{k}>")
        xml.append("    </bank>")
    xml.append("</banks>")
    with open("data/banks.xml", "w") as file:
        file.write("\n".join(xml))


# sum of DEPSUM for all banks
def total_deposits():
    total = 0
    for row in reader:
        total += int(row["DEPSUM"].replace(",", ""))  # better ways, but works
    print(f"total: ${total}")


def bank_deposits():
    deposits = {}
    for row in reader:
        if row["NAMEFULL"] not in deposits:
            deposits[row["NAMEFULL"]] = 0
        deposits[row["NAMEFULL"]] += int(row["DEPSUM"].replace(",", ""))

    deplist = []
    for k, v in deposits.items():
        deplist.append({"name": k, "deposits": v})

    deplist.sort(key=lambda k: k["deposits"])
    pprint(deplist)


print("[1] convert to json")
print("[2] convert to xml")
print("[3] get total deposits")
print("[4] get deposits by bank")
print("")
choice = int(input("What to do? "))


if choice == 1:
    output_json()
if choice == 2:
    output_xml()
if choice == 3:
    total_deposits()
if choice == 4:
    bank_deposits()
