#!/usr/bin/python3
import sys

if len(sys.argv) != 3:
    print("\nUsage : "+sys.argv[0]+" <file to convert> <output file>")
    exit(1)

fileFrom = sys.argv[1]
fileTo = sys.argv[2]

fFrom = open(fileFrom, "r")
buf = ""
line = fFrom.readline().replace("\n","")
while len(line) > 0:
    buf += "echo "+line+" >> "+fileFrom+"\n"
    line = fFrom.readline().replace("\n","")
fFrom.close()
fTo = open(fileTo, "w")
fTo.write(buf)
fTo.close()
