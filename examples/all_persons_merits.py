import requests
from requests.auth import HTTPBasicAuth

#Constants
url = "http://127.0.0.1:8000/"
auth = HTTPBasicAuth("root", "root")

#Helper functions
def tlk_get_request(endpoint):
    r = requests.get("%s%s/" % (url, endpoint), auth=auth)
    return r.json()

def tlk_url_request(url):
    r = requests.get(url, auth=auth)
    return r.json()

def tlk_get_person_merits(person):
    merits = []
    for merit in person["merits"]:
        merit_json = tlk_url_request(str(merit))
        merit_type_json = tlk_url_request(str(merit_json["type"]))
        merits.append(str(merit_type_json["name"]))

    return merits

#"Main"
persons = tlk_get_request("persons")

for person in persons:
    print("%s %s" % (str(person["firstname"]), str(person["lastname"])))
    print("--------------------------")
    merits = tlk_get_person_merits(person)
    for merit in merits:
        print("%s" % merit)

    print("\n")