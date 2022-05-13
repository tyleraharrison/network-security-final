#!/usr/bin/env python3

from th_rsa import *
from th_present import *
import random
import socket

def get_random_key():
    return random.randint(0, 2**64)

# Create a session key
session_key = get_random_key()
print("Session key:", session_key)

# Encrypt the session key with the server's public key
server_public_key = (97, 3337)
hex_session_key = hex(session_key)
encrypted_session_key = encrypt(server_public_key, hex_session_key)

# create a TCP socket object
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 

# update with the IP address of your server
host = "127.0.0.1"
print("Connecting to", host)

# connection to hostname on the port.
port = 10000
s.connect((host, port))

# Send session key to server
message = str(encrypted_session_key)
print("Sending session key:", message)
s.send(message.encode())

# Receive no more than 1024 bytes
msg = s.recv(1024)
print("[Server] " + msg.decode())

# Prepare message for sending
message = "0x28B4D27B225F8BD8".lower()
print("Sending message:", message)

# Encrypt the message with the session key
encrypted_message = generateRoundKeys(message, hex_session_key, 1)
s.send(encrypted_message.encode())

# Send the message to the server
msg = s.recv(1024)
print("[Server] " + msg.decode())

# Close connection
print("Closing connection")
s.close()

