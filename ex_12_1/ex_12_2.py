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
html = urllib.request.urlopen('http://py4e-data.dr-chuck.net/known_by_Fikret.html', context=ctx).read()
soup = BeautifulSoup(html, 'html.parser')

# Retrieve all of the anchor tags
tags = soup('a')
for tag in tags:
    link = (tag.get('href', None))
    linklist.append(link)

#Set an interation. When the count is done, break the iteration.
count = int(input('Enter count:'))
position = int(input('Enter position:'))
while count >= 1:
    print('Retrieving: ', linklist[position-1])
    del linklist[0:position-2]
    count = count - 1
