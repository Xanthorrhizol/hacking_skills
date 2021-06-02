#!/bin/bash

# install python2
sudo apt install python2

# install pip2
curl https://bootstrap.pypa.io/pip/2.7/get-pip.py --output get-pip.py
sudo python2 get-pip.py
rm get-pip.py

# install empire
cd /opt
sudo git clone https://github.com/PowerShellEmpire/Empire.git
cd Empire
sudo ./setup/install.sh

# install pip packages
sudo pip2 install setuptools
sudo pip2 install flask cryptography iptools netifaces pydispatch
sudo ./empire


