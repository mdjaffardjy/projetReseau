def changerchan(conn, name, ancien, nouveau) :
	"""Permet de changer de canal
	
	"""
	remove(conn, ancien)
	list_of_clients[nouveau].append(conn)
	conn.send("Bienvenue dans "+nouveau+'\n')
	for message in list_of_conversations[nouveau]: #displays the last 20 messages
		conn.send(message+"\n")
	broadcast(name+" est entre dans le salon", conn, nouveau)
