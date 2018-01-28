import urllib.request, urllib.parse, urllib.error
import xml.etree.ElementTree as ET

# Promting the url
url = input ('Enter location:')
if len(url) < 1:
    url = 'http://py4e-data.dr-chuck.net/comments_34539.xml'
print('Retrieving', url)

# Opening the url and reads it using urllib
uh = urllib.request.urlopen(url)
data = uh.read()
tree = ET.fromstring(data)

#Length of the xml file
print('Retrieved', len(data), 'characters')

#Count the number of 'count'
counts = tree.findall('.//count')
print('Count:', len(counts))

#Sum the total number in count
lst = tree.findall('comments/comment')
total = 0
for item in lst:
    sum = item.find('count').text
    total = total + int(sum)
print('Sum:', total)
