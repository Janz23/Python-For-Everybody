import urllib.request, urllib.parse, urllib.error
import xml.etree.ElementTree as ET

url = 'http://py4e-data.dr-chuck.net/comments_1669280.xml'
print('Retrieving', url)

total = 0
count = 0

uh = urllib.request.urlopen(url)
data = uh.read()
print('Retrieved', len(data), 'characters')
# print(data.decode())

tree = ET.fromstring(data)
lst = tree.findall ('comments/comment')

print(lst)

for tag in lst:
    x = tag.find('count').text
    print(x)
    
for item in lst:
    count = count + 1
    t = item.find ('count').text
    total = total + float(t)

print ('Count:', count)
print ('Sum:' , total)
