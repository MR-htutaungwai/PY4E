import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

a = int(input("Position: "))-1
b = int(input("Times: "))
url = input("Enter URL: ")
x = urllib.request.urlopen(url).read()
y = BeautifulSoup(x,'html.parser')
for c in range(b):
    z = y('a')
    d = z[a].get('href',None)
    url = d
    e = z[a].contents[0]
print(e)