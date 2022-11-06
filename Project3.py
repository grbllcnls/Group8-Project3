# import library
from distutils.log import info
import requests
import tkinter as tk
from tkinter import END, Text
from tkinter.ttk import Button
from tkinter import messagebox
# create a main window
root = tk.Tk()
root.title('Project 4 - Group 8')
root.geometry("250x170")


# function that will get the data
# from the API

def get_ip():
    response = requests.get('https://api64.ipify.org/?format=json').json()
    return response["ip"]


    
    
def onClick1():
    messagebox.showinfo("Information from IP address", get_ip())

get_button = Button(root, text="Get IP", command=onClick1)


get_button.pack()


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
        "version" : response.get("version"),
        "region" : response.get("region"),
        "country_name" : response.get("country_name"),
        "version" : response.get("version"),
        "region" : response.get("region"),
        "country_name" : response.get("country_name"),
        "org" : response.get("org"),
        "postal" : response.get("postal")
    }
    return information_data


def onClick():
    messagebox.showinfo("Information from IP address", get_information())

get_button1 = Button(root, text="Get Info", command=onClick)
get_button1.pack()


b2 = Button(root, text="Exit", command=root.destroy)
b2.pack()
root.mainloop()

 