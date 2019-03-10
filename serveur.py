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
	conn.send("Bienvenue dans le Hub !\n") 
	conn.send("Choissisez un salon : \n")
	liste_chan=''
	for s in list_of_clients.keys() :
		liste_chan+=s+';'
	conn.send(liste_chan)
	
	chan=conn.recv(2048)[:-1]
	while chan not in list_of_clients.keys() :
		conn.send("Salon inexsitant\n""Choissisez un salon : \n")
		conn.send(liste_chan)
		chan=conn.recv(2048)[:-1]
	
	remove(conn, 'Hub')
	list_of_clients[chan].append(conn)
	conn.send("Bienvenue dans "+chan+'\n')
	broadcast(addr[0]+" est entre dans le salon", conn, chan)
	
	
	while True: 
			try: 
				message = conn.recv(2048) 
				if message: 
		  #prints on the terminal :  message and address of the user
					print("<" + addr[0] + "> " + message) 

					# Calls broadcast function to send message to all 
					message_to_send = "<" + addr[0] + "> " + message 
					broadcast(message_to_send, conn, chan) 

				else: 
					#remove connection when it's broken
					remove(conn, chan) 
					broadcast(addr[0]+" a quitte le salon", conn, chan)
					break
			except: 
				continue

#Broadcast the message to all clients except the one who sent the message
def broadcast(message, connection, chan): 
	for clients in list_of_clients[chan]: 
		if clients!=connection: 
			try: 
				clients.send(message) 
			except: 
				clients.close() 

				# if the link is broken, we remove the client 
				remove(clients) 

#removes the client from the list of clients
def remove(connection, chan): 
	if connection in list_of_clients[chan]: 
		list_of_clients[chan].remove(connection) 

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
