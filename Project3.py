import requests

def get_ip():
    response = requests.get().json()
    return response["ip"]