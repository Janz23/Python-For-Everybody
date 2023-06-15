import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

# Prompt the user to enter a URL, count, and position
url = input('Enter URL:')
count = input('Enter count:')
count = int(count)
pos = input('Enter position:')
pos = int(pos)

# Initialize a counter variable
i = 1

# Perform the following steps 'count' number of times
while i <= count:
    # Read the HTML content from the specified URL
    html = urllib.request.urlopen(url, context=ctx).read()

    # Create a BeautifulSoup object to parse the HTML
    soup = BeautifulSoup(html, "html.parser")

    # Initialize a variable to store the new URL
    new_url = pos

    # Create an empty list to store the URLs
    lista = []

    # Find all the 'a' tags (hyperlinks) in the HTML
    tags = soup('a')

    # Extract the href attribute (URL) from each 'a' tag and add it to the list
    for tag in tags:
        lista.append(tag.get('href', None))

    # Set the new URL based on the position specified
    new_url = lista[pos-1]

    # Print the retrieved URL
    print('Retrieving: ', new_url)

    # Increment the counter
    i = i + 1

    # Update the URL to continue the loop with the new URL
    url = new_url
