#!/usr/bin/env python3

from part2 import *
import socket

# create a TCP socket object
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 

# update with the IP address of your server
host = "127.0.0.1"
#print to make sure it has an IP address
print(host)

# set destination port
port = 10000

# connection to hostname on the port.
s.connect((host, port))

# send message. The string needs to be converted to bytes.
# message = 'Hello. How are you?'
message = "csci458"
print("Sending:", message)
ciphertext = message
s.send(ciphertext.encode())
print("Encrypted:", ciphertext)

# Receive no more than 1024 bytes
msg = s.recv(1024)

print("received: " + msg.decode())

# Close connection
s.close()

