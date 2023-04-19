#!/bin/bash

# Update and install packages
sudo apt-get update && sudo apt-get install -y ettercap-text-only macof yersinia driftnet beef-xss tshark xterm netdiscover lolcat figlet iptables firefox-esr python3 hamster-sidejack

# Install Python packages
pip3 install colorama==0.4.4
pip3 install mitmproxy
pip3 install atexit
pip3 install argparse
pip3 install multiprocessing
pip3 install zipfile
pip3 install mitmproxy
pip3 install json

# Download and extract mitmproxy
wget "https://downloads.mitmproxy.org/9.0.1/mitmproxy-9.0.1-linux.tar.gz"
tar -xvzf mitmproxy-9.0.1-linux.tar.gz

# Download and install AutoIt
sudo wget "https://www.autoitscript.com/cgi-bin/getfile.pl?autoit3/autoit-v3-setup.zip"
sudo unzip autoit-v3-setup.zip
sudo wine autoit-v3-setup.exe
