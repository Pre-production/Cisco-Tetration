import json
from tetpyclient import RestClient

API_ENDPOINT="https://10.10.10.10"

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

resp = restclient.get('/sensors')

offset = resp.json().get('offset') 
server_list = resp.json()['results']

while offset:
    resp_next = restclient.get('/sensors?offset=' + offset)
    offset = resp_next.json().get('offset')
    server_list = server_list + resp_next.json()['results']

with open('deleted_servers_list.txt', 'w+') as f:
    for server in server_list:
        if 'deleted_at' in server:		        
                f.write(str(server['uuid'])+' '+ str(server['host_name'])+' '+'Removal time is: '+ str(server['deleted_at'])+ '\n')

input('File created successfully. Press any key to finish...')

