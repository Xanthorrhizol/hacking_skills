#!/bin/bash

# Clear iptables rules
iptables -P INPUT ACCEPT
iptables -P FORWARD ACCEPT
iptables -P OUTPUT ACCEPT
iptables -F
iptables -X

# SSH Scenario
iptables -F
iptables -P INPUT DROP
iptables -P FORWARD DROP
iptables -A INPUT -i lo -j ACCEPT
iptables -A INPUT -m state --state ESTABLISHED,RELATED -j ACCEPT

#   Allow the target protocol and port
iptables -A INPUT -p <protocol(tcp|udp)> --dport <port> -m state --state NEW -j ACCEPT

iptables -A INPUT -i lo -j ACCEPT
