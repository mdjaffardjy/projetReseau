# Python program to implement server side of chat room. 
import socket 
import select 
import sys 
from thread import *
from collections import deque

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1) 

# checks whether IP address and port number have been provided 
if len(sys.argv) != 3: 
	print("Entrez : script, addresse IP, numero de port")
	exit() 


IP_address = str(sys.argv[1]) 
 
Port = int(sys.argv[2]) 

#The client must be aware of the IP address and port number parameters 
server.bind((IP_address, Port)) 

#listens for "100" active connections
server.listen(100) 

list_of_clients = {'Hub' : [], 'Blabla' : []}

#list of the last messages for a conversation. We keep maximum 20 messages
conversation = deque([], 20)

def clientthread(conn, addr): 

	# sends a message to the client whose user object is connected
	conn.send("Bienvenue dans le Hub !") 
	conn.send("Choissisez un salon : ")
	conn.send(s for s in list_of_clients.keys())
	while True: 
			try: 
				message = conn.recv(2048) 
				if message: 

		  #prints on the terminal :  message and address of the user
					print("<" + addr[0] + "> " + message) 

					# Calls broadcast function to send message to all 
					message_to_send = "<" + addr[0] + "> " + message 
					broadcast(message_to_send, conn) 

				else: 
					#remove connection when it's broken
					remove(conn) 

			except: 
				continue

#Broadcast the message to all clients except the one who sent the message
def broadcast(message, connection): 
	for clients in list_of_clients: 
		if clients!=connection: 
			try: 
				clients.send(message) 
			except: 
				clients.close() 

				# if the link is broken, we remove the client 
				remove(clients) 

#removes the client from the list of clients
def remove(connection): 
	if connection in list_of_clients: 
		list_of_clients.remove(connection) 

#Sends a message when the server is in place
print("Your server is up.")


while True: 

	"""Accepts a connection request and stores two parameters, 
	socket object for that user, and IP address of the client"""
	conn, addr = server.accept() 

	"""Maintains a list of clients in the chatroom"""
	list_of_clients['Hub'].append(conn) 

	# prints the address of the user that just connected 
	print(addr[0] + " connected")

	# creates and individual thread for every user 
	# that connects 
	start_new_thread(clientthread,(conn,addr))	 

conn.close() 
server.close()
