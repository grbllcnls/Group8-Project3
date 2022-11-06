import requests

def get_ip():
    response = requests.get('https://api64.ipify.org/?format=json').json()
    return response["ip"]

def get_network():
    response = requests.get(f'https://ipapi.co/{ip_address}/json/').json()
    network = {"Network" : response.get("network")}
    return network

def get_city():
    ip_address = get_ip()
    response = requests.get(f'https://ipapi.co/{ip_address}/json/').json()
    city = {"City" : response.get("city")}
    return city

def get_version():
    ip_address = get_ip()
    response = requests.get(f'https://ipapi.co/{ip_address}/json/').json()
    version = {"Version" : response.get("version")}
    return version

def get_region():
    ip_address = get_ip()
    response = requests.get(f'https://ipapi.co/{ip_address}/json/').json()
    region = {"Region" : response.get("region")}
    return region

def get_countryname():
    ip_address = get_ip()
    response = requests.get(f'https://ipapi.co/{ip_address}/json/').json()
    countryname = {"Country Name" : response.get("country_name")}
    return countryname

def get_org():
    ip_address = get_ip()
    response = requests.get(f'https://ipapi.co/{ip_address}/json/').json()
    org = {"Org" : response.get("org")}
    return org

def get_postal():
    ip_address = get_ip()
    response = requests.get(f'https://ipapi.co/{ip_address}/json/').json()
    postal = {"Postal" : response.get("postal")}
    return postal

def get_information():
    ip_address = get_ip()
    response = requests.get(f'https://ipapi.co/{ip_address}/json/').json()
    information_data = {
        "ip": ip_address,
        "network" : response.get("network"),
        "city" : response.get("city"),
        "version" : response.get("version"),
	    "region" : response.get("region"),
        "country_name" : response.get("country_name"),
        "org" : response.get("org"),
        "postal" : response.get("postal")
    }
    return information_data

print (get_information())
print (get_postal())
print (get_org())
print (get_countryname())
