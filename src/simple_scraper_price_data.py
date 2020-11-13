import requests
import re

url = 'https://www.marketwatch.com/investing/stock/live'
response = requests.get(url)
content = response.text
noCodeTags = re.sub('<[^<]+?>', '', content)

print(noCodeTags)
