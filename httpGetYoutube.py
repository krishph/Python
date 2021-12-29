import requests
import webbrowser

searchText = 'Skillsoft'
PARAMS = {'q': searchText}
url='https://www.youtube.com/search'
rGet = requests.get(url, params=PARAMS)
print(rGet.url)
webbrowser.open(rGet.url)