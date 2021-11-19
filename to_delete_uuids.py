import json
from tetpyclient import RestClient

API_ENDPOINT="https:10.10.10.10"

# ``verify`` is an optional param to disable SSL server authentication.
# By default, |product| appliance dashboard IP uses self signed cert after
# deployment. Hence, ``verify=False`` might be used to disable server
# authentication in SSL for API clients. If users upload their own
# certificate to |product| appliance (from ``Settings > Company`` Tab)
# which is signed by their enterprise CA, then server side authentication
# should be enabled.
# credentials.json looks like:
# {
# "api_key": "<hex string>",
# "api_secret": "<hex string>"
# }


restclient = RestClient(API_ENDPOINT,
             credentials_file='api_credentials.json', 
			 verify=False)

# followed by API calls, for example API to retrieve list of agents.
# API can be passed /openapi/v1/sensors or just /sensors.
i = 1
server_list = []
with open('uuids_list.txt', 'r') as f:
  for line in f:
    server_list.append(line.strip())

for string in server_list:
    resp = restclient.delete('/sensors/'+string)
    print (i , string , resp.status_code)
    i += 1
input ('Finish')