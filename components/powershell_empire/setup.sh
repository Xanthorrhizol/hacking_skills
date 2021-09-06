#!/bin/bash

# install python2
sudo apt install python2 swig m2crypto

# install empire
cd /opt
sudo git clone https://github.com/Xanthorrhizol/Empire.git
cd Empire
sudo ./setup/install.sh

# start
sudo ./empire


