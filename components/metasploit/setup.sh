#!/bin/bash
systemctl enable postgresql
systemctl start postgresql
sudo msfdb init
sudo apt update; sudo apt install metasploit-framework
