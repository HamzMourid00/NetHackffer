
# NetHackffer

NetHackffer is an automation python script that perform post network attacks for test the security of your network and to be wary from this danger

![Github Banner](https://github.com/HamzMourid00/NetHackffer/blob/main/Nethackffer.png)

### Linux installation
```sh
cd /opt && sudo su
git clone https://github.com/HamzMourid00/NetHackffer.git
cd NetHackffer
chmod 770 NetHackffer.py
chmod 770 setup.sh
./setup.sh
./NetHackffer.py
```
# Requirements

To set up the environment, you will need:

- Kali Linux OS (or similar Debian-based Linux distribution)
- Internet connection
- Superuser (sudo) privileges
- The following packages need to be installed using the package manager (apt-get):

    - ettercap-text-only
    - macof
    - yersinia
    - driftnet
    - beef-xss
    - tshark
    - xterm
    - netdiscover
    - lolcat
    - figlet
    - iptables
    - firefox-esr
    - python3
    - hamster-sidejack
    
- Additionally, the following Python packages need to be installed using pip3:

    - colorama==0.4.4
    - mitmproxy
    - atexit
    - argparse
    - multiprocessing
    - zipfile
    
- You also need to download and extract mitmproxy version 9.0.1 for Linux 
- Finally, you need to download and install AutoIt using Wine

**Note**: These requirements are for setting up a specific environment and may vary depending on your use case.

## Attacks

The following attacks can be performed using this project:

1. **Mitm & BACKDOOR DOWNLOADED FILES IN THE Fly & SNIFFING:** Intercept network traffic, backdoor downloaded files with an evil file of your choice (trojan, keylogger, malware..), and install backdoors while sniffing for sensitive information and bypassing SSL. 
2. **ARP_DNS SPOOFING & SNIFFING:** Spoof ARP and DNS packets to redirect network traffic and sniff for sensitive information (inames) and bypass SSL.
3. **Mitm & INJECTING Beef js code:** Intercept network traffic and inject malicious JavaScript code using the Beef framework and bypass SSL.
4. **Mitm ATTACK & SNIFFING:** Intercept network traffic and perform various attacks while sniffing for sensitive information and bypassing SSL.
5. **Switch MAC flooding:** Flood a switch with fake MAC addresses to cause it to crash or become unresponsive.
6. **DHCP starvation Attack:** Overwhelm a DHCP server with bogus requests to exhaust its address pool and prevent legitimate clients from obtaining an IP address.
7. **DOS attack deleting all VTP vlans:** Perform a denial-of-service attack to delete all VTP VLANs on a switch, potentially causing network-wide disruption.
8. **DOS attack flooding CDP table:** Perform a denial-of-service attack to flood a switch's CDP table with fake information, potentially causing network-wide disruption.
