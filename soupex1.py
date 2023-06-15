import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl
import re

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter - ')
# url = http://py4e-data.dr-chuck.net/comments_1669278.html
html = urllib.request.urlopen(url, context=ctx).read()
soup = BeautifulSoup(html, "html.parser")

# Retrieve all of the anchor tags
count = 0
sum = 0
tags = soup('span')
for tag in tags:
    tag = str(tag)
    x = re.findall('[0-9]+', tag)
    for num in x:
        sum = sum + int(num)
    count = count + 1

print('Count', count)
print('Sum', sum)
    # Look at the parts of a tag
'''
    print('TAG:', tag)
    print('URL:', tag.get('href', None))
    print('Contents:', tag.contents[0])
    print('Attrs:', tag.attrs)
'''
