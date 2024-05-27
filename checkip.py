

import requests
import json

def get_ip_info(ip_address):
    # API token from ipinfo.io
    token = '8481288f106c65'
    url = f'https://ipinfo.io/{ip_address}?token={token}'

    response = requests.get(url)
    data = response.json()

    return data

# Check IP 
ip_address = '45.122.220.65'  
data = get_ip_info(ip_address)
print(json.dumps(data, indent=4))  #Print JSON

# Check VPN/Proxy
if 'bogon' in data:
    print('Bogon IP detected')
elif 'privacy' in data:
    if data['privacy'].get('vpn'):
        print('VPN detected')
    if data['privacy'].get('proxy'):
        print('Proxy detected')
