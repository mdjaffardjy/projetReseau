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

liste_utilisateurs=[]

liste_commandes = ['changernom', 'changersalon', 'creersalon', 'listeutilisateurs\n']
#list of the the list of the last messages for all conversations. We keep a maximum of 20 messages
list_of_conversations = {'Hub' : deque([], 20), 'Blabla' : deque([], 20)} 


def changerchan(conn, name, ancien, nouveau) :
	remove(conn, ancien)
	list_of_clients[nouveau].append(conn)
	conn.send("Bienvenue dans "+nouveau+'\n')
	for message in list_of_conversations[nouveau]: #displays the last 20 messages
		conn.send(message+"\n")
	broadcast(name+" est entre dans le salon", conn, nouveau)

def connected_users(liste_utilisateurs):
  res =""
  for s in liste_utilisateurs:
	  res = res +" - " + s
  res=res+" sont actuellement connectes\n"
  return res

def clientthread(conn, addr): 
	name=addr[0]
	conn.send("Choissisez un nom :\n")
	name=conn.recv(2048)[:-1]
	while name in liste_utilisateurs :
		conn.send("Nom deja utilise\n")
		conn.send("Choissisez un nom :\n")
		name=conn.recv(2048)[:-1]
		
	liste_utilisateurs.append(name)
	liste_utilisateurs.sort()
	
	
# Infos sur les utilisateurs du reseau 
	
	# sends a message to the client whose user object is connected

	conn.send("Bienvenue dans le Hub !\nIl y a actuellement " + str(len(liste_utilisateurs)) + " utilisateurs connecte(s) : \n"+ connected_users(liste_utilisateurs) + "\nChoissisez un salon : \n")
	liste_chan=''
	for s in list_of_clients.keys() :
		liste_chan+=s+';'
	conn.send(liste_chan)
	
	chan=conn.recv(2048)[:-1]
	while chan not in list_of_clients.keys() :
		conn.send("Salon inexistant\nChoisissez un salon : \n")
		conn.send(liste_chan)
		chan=conn.recv(2048)[:-1]

	changerchan(conn, name, 'Hub', chan)
  

	while True: 
		try: 
			message = conn.recv(2048) 
			if message: 
		  #prints on the terminal :  message and address of the user
				print("<" + name + "> " + message) 
				if message.startswith('/') :
					comm=message.split(' ')
					if comm[0][1:] not in liste_commandes :
						conn.send("Commande inconnue ou incomplete\n")
					else :
						if comm[0][1:]=='changernom' :
							nv=comm[1].rstrip("\n")
							if nv not in liste_utilisateurs :
								liste_utilisateurs.remove(name)
								liste_utilisateurs.append(nv)
								broadcast(name+" a change son nom en "+nv, conn, chan)
								name=nv
							else :
								conn.send("Nom deja utilise\n")
						elif comm[0][1:]=='changersalon' :
							if comm[1].rstrip("\n") in list_of_clients.keys() :
								changerchan(conn, name, chan, comm[1].rstrip("\n"))
								chan=comm[1].rstrip("\n")

						elif comm[0][1:]=='listeutilisateurs\n' :
							for u in liste_utilisateurs :
								conn.send(u+"\n")
				else :
				# Calls broadcast function to send message to all and saves the message in the list
					message_to_send = "<" + name + "> " + message 
					broadcast(message_to_send, conn, chan) 
					if(len(list_of_conversations[chan])==20):
						list_of_conversations[chan].popleft()
					msg = "<" + name + "> " + message
					list_of_conversations[chan].append(msg)

			else: 
				#remove connection when it's broken
				remove(conn, chan) 
				broadcast(name+" a quitte le salon", conn, chan)
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
