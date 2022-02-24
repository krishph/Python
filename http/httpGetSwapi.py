import requests
import json
from pprint import pprint

r_get = requests.get("https://swapi.dev/api/people/20/")

print(r_get.status_code)
data = json.loads(r_get.text)

pprint(data)