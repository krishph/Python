import requests
import webbrowser

url = "https://www.wikipedia.org"

resp = requests.get(url)

print(resp.url)
webbrowser.open(resp.url)