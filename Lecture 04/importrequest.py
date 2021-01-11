import requests

url = "http://facebook.com"

response = requests.get(url)
with open("riyadh.html") as f:
    f.write(response.text)