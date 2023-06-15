'''
This code demonstrates how to use the Google Geocoding API to retrieve the
place ID for a given address. It can either use a Google Places API key or
use a default key and service URL.
'''
import urllib.request, urllib.parse, urllib.error
import json
import ssl

api_key = False
# If you have a Google Places API key, enter it here
# api_key = 'AIzaSy___IDByT70'
# https://developers.google.com/maps/documentation/geocoding/intro

if api_key is False:
    api_key = 42
    serviceurl = 'http://py4e-data.dr-chuck.net/json?'
else:
    serviceurl = 'https://maps.googleapis.com/maps/api/geocode/json?'

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

address = 'University of Malaya'

parms = dict()
parms['address'] = address
if api_key is not False:
    parms['key'] = api_key
url = serviceurl + urllib.parse.urlencode(parms)

# Print the URL being retrieved
print('Retrieving', url)

# Open the URL and read the data, decoding it as a string
uh = urllib.request.urlopen(url, context=ctx)
data = uh.read().decode()

# Print the number of characters retrieved
print('Retrieved', len(data), 'characters')

try:
    # Attempt to parse the JSON data
    js = json.loads(data)
except:
    js = None

# Uncomment the line below to print the JSON response in an indented format
# print(json.dumps(js, indent=4))

# Extract the place ID from the JSON response
place_id = js['results'][0]['place_id']

# Print the retrieved place ID
print("Place ID:", place_id)
