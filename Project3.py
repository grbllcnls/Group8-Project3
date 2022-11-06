# import library
from distutils.log import info
import requests
import tkinter as tk
from tkinter import END, Text
from tkinter.ttk import Button
# create a main window
root = tk.Tk()
root.title('Project 4 - Group 8')

# function that will get the data
# from the API
def get_ip():
	# API request
	r = requests.get('https://api64.ipify.org/?format=json')
	data = r.json()
	ip = data['ip']



	# deletes all the text that is currently
	# in the TextBox
	text_box.delete('1.0', END)
	
	# inserts new data into the TextBox
	text_box.insert(END,ip)


    
    
text_box = Text(root, height=10, width=50)
get_button = Button(root, text="Get IP", command=get_ip)

text_box.pack()
get_button.pack()


def get_network():
    ip_address = get_ip()
    response = requests.get(f'https://ipapi.co/{ip_address}/json/').json()
    network = {"Network" : response.get("network")}
    print(network)
    
    text_box1.delete('1.0', END)
	
    text_box1.insert(END, get_network)


text_box1 = Text(root, height=10, width=50) 


get_button1 = Button(root, text="Get Information", command=get_network)

get_button1.pack()




b2 = Button(root, text="Exit", command=root.destroy)

get_button.pack()
b2.pack()

root.mainloop()