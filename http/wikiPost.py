import requests
import json
from pprint import pprint
import webbrowser
import time

url = 'https://en.wikipedia.org/w/index.php'
body = { 'search': 'skillsoft'}

rPost = requests.post(url, data=body)
print(rPost.status_code)
pprint(rPost.text)

with open('skillsoft.html', 'wb') as f:
    for chunk in rPost.iter_content(chunk_size=10000):
        f.write(chunk)
time.sleep(1)
file = 'file:///Users/krish/Documents/Repos/Python/http/skillsoft.html'
webbrowser.open(file, new=1)