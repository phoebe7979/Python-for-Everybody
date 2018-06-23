import urllib.request, urllib.parse, urllib.error
import json

url = input ('Enter location:')
if len(url) < 1:
    url = 'http://py4e-data.dr-chuck.net/comments_34540.json'
print ('Retrieving', url)

# Opening the url and retrieving it using urllib
uh = urllib.request.urlopen(url)

# Read the url and parse json
data = uh.read()
info = json.loads(data)
jsoninfo = info['comments']

# Printing characters and data
print('Retrivied', len(data), 'characters')
print ('Count: ', len(jsoninfo))

#Printing total sum for 'count'
sum = 0
for item in jsoninfo:
    sum = sum + item['count']
print('Sum: ', sum)
