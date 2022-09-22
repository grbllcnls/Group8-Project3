import requests

def get_ip():
    response = requests.get('https://api64.ipify.org/?format=json').json()
    return response["ip"]

def get_information():
    ip_address = get_ip()
    response = requests.get(f'https://ipapi.co/{ip_address}/json/').json()
    information_data = {
        "ip": ip_address,
        "network" : response.get("network"),
        "city" : response.get("city"),
        "version" : response.get("version")

        
    }
    return information_data

print (get_information())
