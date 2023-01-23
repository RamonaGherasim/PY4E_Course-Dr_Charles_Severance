import json
import urllib.request, urllib.error
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE


url = input('Enter location: ')
print('Retrieving ', url)
uh = urllib.request.urlopen(url, context=ctx)

data = uh.read()

info = json.loads(data)
print('User count:', len(info))

print(json.dumps(info, indent=2))

print(sum(i['count'] for i in info['comments']))
