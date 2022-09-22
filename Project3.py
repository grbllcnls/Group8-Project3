import requests

def get_ip():
    response = requests.get('https://api64.ipify.org/?format=json').json()
    return response["ip"]

def get_information():
   
    response = requests.get(f'https://ipapi.co/{ip_address}/json/').json()


get_information()
