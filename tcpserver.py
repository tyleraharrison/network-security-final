#!/usr/bin/env python3

from th_rsa import *
from th_present import *
import socket                                         

server_public_key = (97, 3337)
server_private_key = (1693, 3337)

# create a TCP/IP socket object
serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 

# update with the IP address of your local machine
host = "127.0.0.1"                         

#set port number for this server
port = 10000                                          

# bind to the port
serversocket.bind((host, port))                                  

# Listen for incoming connections, queue up to 5 requests
serversocket.listen(5)

# wait for a connection
print('waiting for a connetion on port ' + str(port) + '\n')
clientsocket,addr = serversocket.accept()      
print("Got a connection from " + str(addr))

def get_session_key():
   data = clientsocket.recv(1024)
   raw_string = data.decode()
   # Remove first and last characters
   raw_string = raw_string[1:]
   raw_string = raw_string[:-1]
   # Convert to list of integers
   print("Received session key: " + raw_string)
   encrypted_session_key = raw_string.split(", ")
   for i in range(len(encrypted_session_key)):
         encrypted_session_key[i] = int(encrypted_session_key[i])
   decrypted = decrypt(server_private_key, encrypted_session_key)
   # Convert from hex string to integer
   session_key = int(decrypted, 16)
   print("Decrypted:", session_key)
   msg = 'Session key received'+ "\n"
   clientsocket.send(msg.encode())

def get_message():
   # Receive the data of 1024 bytes maximum. The received data is binary data. 
   data = clientsocket.recv(1024).decode()
   decrypted = data
   print("\n[Client] " + data)
   print("Decrypted:", decrypted)
   msg = 'Message received'+ "\n"
   clientsocket.send(msg.encode())

session_key = get_session_key()
get_message()
clientsocket.close()
serversocket.close()
print("\nServer closed")