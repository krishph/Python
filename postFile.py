import os
import requests

os.system("echo 'This is a sample test 123' >> sample.txt")
os.system("cat sample.txt")

url = 'http://httpbin.org/post'
files = {
    'files': open('sample.txt', 'rb')
}
values = {'upload_file' : 'sample.txt', 'OUT': 'csv'}

rPost = requests.post(url, files=files, data=values)

print(rPost.status_code)