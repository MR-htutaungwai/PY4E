import urllib.parse, urllib.request, urllib.error
import xml.etree.ElementTree as ET

list_of_ints = []
url = ('http://py4e-data.dr-chuck.net/comments_1034609.xml')
output = urllib.request.urlopen(url).read()
tree = ET.fromstring(output)

total = 0
for comments in tree.findall('comments'):
    for comment in comments.findall('comment'):
        total += int(comment.find('count').text)

print(total)