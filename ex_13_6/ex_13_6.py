import urllib.request, urllib.parse, urllib.error
import json

# Specifying the API url for this task #

serviceurl = "http://py4e-data.dr-chuck.net/geojson?"

# Requesting the location and encode and concatenate it into the new url#
while True:
    address = input('Enter Location: ')
    if len(address) < 1: break

    url = serviceurl + urllib.parse.urlencode(
    {'address': address}
    )
    print('Retrieving: ', url)

# Opening, reading the url, and decoding the json from UTF-8 to unicode for internal application#
    uh = urllib.request.urlopen(url)
    data = uh.read().decode()
    print('Retrieved', len(data), 'characters')

# Parsing the json library, and making sure it's no problem#
    try:
        js = json.loads(data)
    except:
        js = None

    if not js or 'status' not in js or js['status'] != 'OK':
        print ('=== Failure to Retrieve===')
        print (data)
        continue


# Searching for place_id in the first object/dictionary in the array#
    place = js["results"][0]["place_id"]
    print ('Place id ', place)
    break
