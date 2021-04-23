import socket
import sys

if len(sys.argv) != 2:
	print "Usage: "+sys.argv[0]+" <username>"
	sys.exit(0)

# create a socket and connect to the server
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
connect = s.connect(('<target ip>', 25))

# receive the banner
banner = s.recv(1024)
print banner

# verify a user
s.send('VRFY '+sys.argv[1]+'\r\n')
result = s.recv(1024)
print result

# close the socket
s.close()
