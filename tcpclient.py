# This is tcpclient.py file

import socket
from substitution_functions import *

blueTeam = ["Ana", "Emily", "Michael", "John"]
wordArr = ["zoo", "xray", "rellis", "college station", "csci458"]

# create a TCP socket object
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# update with the IP address of your server
# host = "10.228.217.50"
host = "127.0.0.1"
# print to make sure it has an IP address
print(host)

# set destination port
port = 10000

# connection to hostname on the port.
s.connect((host, port))

# Caesar
# for word in wordArr:
#     # encryption
#     message = word
#     encryptedMessage = encryptCaesar(message)

#     # send message
#     print('message:', message, ",sending (encrypted):", encryptedMessage)
#     s.send(encryptedMessage.encode())

#     # recieve message
#     msg = s.recv(1024)
#     print("received (encrypted):", msg.decode(),
#           ", message:", decryptCaesar(msg.decode()), "\n")

# ROT13
for word in wordArr:

    # encryption
    message = word
    encryptedMessage = ROT13(message)

    # send message
    print('message:', message, ",sending (encrypted):", encryptedMessage)
    s.send(encryptedMessage.encode())

    # recieve message
    msg = s.recv(1024)
    print("received (encrypted):", msg.decode(),
          ", message:", ROT13(msg.decode()), "\n")

# Three round encryption
# for word in wordArr:
#     message = word

#     # Encryption
#     C1 = encryptCaesar(message)
#     C2 = ROT13(C1)
#     C3 = sBox(C2)

#     # send message
#     print('message:', message, ", sending (encrypted):", C3)
#     s.send(C3.encode())

#     # recieve message and decrypt
#     msg = s.recv(1024)

#     # Decryption
#     C3 = inv_sBox(msg.decode())
#     C2 = ROT13(C3)
#     C1 = decryptCaesar(C2)

#     print("received (encrypted):", msg.decode(),
#           ", message:", C1, "\n")

# Close connection
s.close()
