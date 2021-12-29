import requests
from pprint import pprint
import json

#/locationId/year/month/date
print(requests.__version__)
#r_get = requests.get("https://www.metaweather.com/api/location/2477058/2021/12/28/")
#r_get = requests.get("https://www.metaweather.com/api//api/location/search/?query=london")
#r_get = requests.get("https://www.metaweather.com/api/location/44418")
r_get = requests.get("https://www.metaweather.com/api/location/2465512/2021/12/28/")


print(r_get)
print(r_get.status_code)
print(type(r_get))
print(r_get.headers)

##
data = json.loads(r_get.text)
pprint(data)

print(r_get.is_redirect)
