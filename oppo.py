import xml.etree.ElementTree as ET
import requests

tree = ET.parse('oppo.xml')

root = tree.getroot()
count = 0;
for child in root:
	if (count<=5):
		count = count+1
	else:
		name =  child[0].text
		url = 'https://iucf-icon-sg.s3.ap-southeast-1.amazonaws.com/' + name
		r = requests.get(url, allow_redirects=True)
		open(url.rsplit('/',1)[1], 'wb').write(r.content)
		print url.rsplit('/', 1)[1]+" downloaded"

