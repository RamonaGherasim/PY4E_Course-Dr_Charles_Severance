from urllib.request import urlopen
from bs4 import BeautifulSoup
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter - ')
if not url:
    url = "http://py4e-data.dr-chuck.net/comments_1719381.html"
html = urlopen(url, context=ctx).read()
soup = BeautifulSoup(html, "html.parser")

# Retrieve all of the anchor tags
spans = soup('span')
num = []
for span in spans:
    # Look at the parts of a tag
    num.append(span.contents[0])
total = sum([int(i) for i in num])
print(total)
