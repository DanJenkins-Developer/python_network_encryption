# This is tcpserver.py file
import socket
from substitution_functions import *
# create a TCP/IP socket object
serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# update with the IP address of your local machine
# host = "10.228.217.50"
host = "127.0.0.1"
# set port number for this server
port = 10000

# bind to the port
serversocket.bind((host, port))

# Listen for incoming connections, queue up to 5 requests
serversocket.listen(5)

# Accept connection

# while True:
#     print('waiting for a connetion on port ' + str(port) + '\n')
#     clientsocket, addr = serversocket.accept()
#     print("Got a connection from " + str(addr))

#    # Recieve the data
#     while True:
#         data = clientsocket.recv(1024).decode()
#         if data != '':

#             print("recieved (encrypted)", data,
#                   ", data:", decryptCaesar(data), "\n")
#             reply = data
#             clientsocket.send(reply.encode())
#         else:
#             print("No more data from" + str(addr))
#             break

# ROT 13
while True:
    print('waiting for a connetion on port ' + str(port) + '\n')
    clientsocket, addr = serversocket.accept()
    print("Got a connection from " + str(addr))

   # Recieve the data
    while True:
        data = clientsocket.recv(1024).decode()
        if data != '':

            print("recieved (encrypted)", data, ", data:", ROT13(data), "\n")

            reply = data
            clientsocket.send(reply.encode())
        else:
            print("No more data from" + str(addr))
            break

# Three round encryption
# while True:
#     print('waiting for a connetion on port ' + str(port) + '\n')
#     clientsocket, addr = serversocket.accept()
#     print("Got a connection from " + str(addr))

#    # Recieve the data
#     while True:
#         data = clientsocket.recv(1024).decode()
#         if data != '':

#             # Decryption
#             C3 = inv_sBox(data)
#             C2 = ROT13(C3)
#             C1 = decryptCaesar(C2)
#             print("recieved (encrypted)", data, ", data:", C1, "\n")

#             # Reply with the same data
#             reply = data
#             clientsocket.send(reply.encode())
#         else:
#             print("No more data from" + str(addr))
#             break

clientsocket.close()
