import urllib.request, urllib.parse, urllib.error
import json

url = 'http://py4e-data.dr-chuck.net/comments_1669281.json'
print('Retrieving', url)

total = 0
count = 0

# Open the URL and read the data
uh = urllib.request.urlopen(url)
data = uh.read()
print('Retrieved', len(data), 'characters')

# Parse the JSON data
js = json.loads(data)

# Iterate over each comment and calculate the total count
for u in js['comments']:
    count = count + 1
    t = int(u['count'])
    total = total + t

# Print the count and sum of all comments
print('Count:', count)
print('Sum:', total)
