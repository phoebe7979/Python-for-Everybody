# To run this, you can install BeautifulSoup
# https://pypi.python.org/pypi/beautifulsoup4

# Or download the file
# http://www.py4e.com/code3/bs4.zip
# and unzip it in the same directory as this file

import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl
linklist = list()

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE


url = input('Enter - ')
if len(url) < 1:
    url = 'http://py4e-data.dr-chuck.net/known_by_Ashley.html'
count = int(input('Enter count:'))
position = int(input('Enter position:'))

# Retrieve all of the anchor tags
while count >= 1:
    html = urllib.request.urlopen(url, context=ctx).read()
    soup = BeautifulSoup(html, 'html.parser')
    tags = soup('a')
    for tag in tags:
        link = (tag.get('href', None))
        linklist.append(link)
    followlink = linklist[position-1]
    print('Retrieving: ', followlink)
    count = count - 1
    url = followlink
    linklist = list()
