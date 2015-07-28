__author__ = 'Christoffer Holmberg'
####
# Example CSV to TLKmAPI importer.
####
import csv
import json
import requests
from config import url, user, pasw

headers = {'content-type': 'application/json'}

csvfile = open('mockdata.csv', 'r', encoding="utf-8",)

fieldnames = ("firstname", "middlenames", "lastname",
              "dob", "dod", "birthplace", "phone",
              "email", "address", "city", "zip",
              "country", "joined", "graduated",
              "company", "company_email",
              "company_phone", "notes")
reader = csv.DictReader(csvfile, fieldnames)
for row in reader:
    for i, j in row.items():
        if j == '':
            row[i] = None
    row['members'] = []
    row['boards'] = []
    row['officials'] = []
    row['merits'] = []
    row['committees'] = []

    print(row)
    r = requests.post(url, auth=(user, pasw), headers=headers, data=(json.dumps(row)))
    print(json.dumps(row))
    print(r.headers)
    print(r.status_code)
#    print(r.text)
    print(r.content)
