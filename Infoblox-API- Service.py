import requests
import json
session = requests.Session()
session.auth = ('admin', '*******')
url = 'https://10.20.64.94/wapi/v2.7/'
session.verify = False
####GET Call to view something in infoblox#########
"""
r = session.get(url + 'record:cname')
r.status_code
print (r.content)
"""
###Delete zone from Infoblox#####
"""
ref = "zone_auth/ZG5zLnpvbmUkLl9kZWZhdWx0LmNvbS5tdXR1YWxvZm9tYWhhLnRlc3QudGVzdDY: test6.test.mutualofomaha.com/default"
"""
####POST call to add zone in infoblox####
"""
z = str(input('enter Zone Name'))
data = { 'fqdn': z}
r = session.post(url + 'zone_auth', data=data)
r.status_code
"""
####POST call to add Cname in infoblox####
"""
x = str(input('enter CName'))
y = str(input('enter canonical Name'))
data = { 'name': x, 'canonical':y }
r = session.post(url + 'record:cname', data=data)
r.status_code
"""