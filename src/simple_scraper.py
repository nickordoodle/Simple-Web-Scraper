import requests

url = 'https://stackoverflow.com/questions/529034/python-pass-or-sleep-for-long-running-processes'
response = requests.get(url)
html = response.content
print(html)
