# Projet Programmation Réseau - Serveur Chat-Room

  This chat-room server is composed of multiple rooms. A user can chat with other users that are present in the same room, using the computer terminal.
  
  The user can browse different rooms and create new ones using commands, and can send private messages to all users connected to the server.
   
### Included

* This README
* All source files (serveur.py and client.py)


## Getting started

This software can be run on one machine, or on multiple machines, using Python2.7.

Libraries that need to be installed are :
* socket
* select
* sys
* thread
* collections

Language of the server : french

## Installing / Tests

First, install the server using the following command in the computer terminal :
```python
python server.py <IP_address> <port>
```
For example : ```python python serveur.py 127.0.0.1 8888```

> If the server is correctly set, you will see a written confirmation in the terminal : "Your server is up".
> If an error appears, please refer to the Authors part to contact us.


Once the server is set, users that want to connect to the server should use the following command (can be written in a new terminal window or in a separate computer terminal window):
```python
python client.py <IP_address> <port>
```
> Be aware that the users connect to the same localhost and port as the ones of the server !
> If the client is correctly connected, you will see a written confirmation in the terminal : "Choisissez un nom".

#### Commands and use of the chat-room
This part is client-oriented. Indeed, once the server is up, no further handling is required. 
First, "Choisissez un nom" appears on the terminal. Other users will see you under this name in the server.
If this name does not already exist, a welcome message appears with other informations (like the number of users and a list of their names).

Then, you can chose a room in which you wish to enter (amongst the rooms in the list). Just write the name of the chosen room in the terminal.

WARNING : No special command can be used before this step.

##### Special commands
* ``` /changernom <nom> ``` : enables to change the user's own name. Warning : no space allowed ; no already used name can be taken (except if the user using this name left the server).

Example : ``` /changernom Fifi ```

* ``` /changersalon <name_of_room> ``` : enables to change room amongst existing rooms.

Example : ``` /changersalon Hub ```

* ``` /creersalon <name_of_new_room> ``` : create a new chat room named after *name_of_room*. No space allowed. Two chat rooms cannot have the same name.

Example : ``` /creersalon Forum ```

* ``` /listeutilisateurs ``` : prints the list of connected users in the terminal window.

* ``` /help ``` : provide help on how to use the server and commands

* ``` /exit ``` : enables an user to leave the server properly. Type ``` y ``` if you are sure to leave. ``` n ``` enables to come back to server.


## Authors
* **Olivia Brunet** - *Initial work* - [GitHub](https://github.com/OliviaBnt)

* **Marine Djaffardjy** - *Initial work* - [GitHub](https://github.com/mdjaffardjy)

* **Théophile Moreal de Brevans** - *Initial work* - [GitHub](https://github.com/MorealDeBrevans/)

See also the list of [contributors](https://github.com/mdjaffardjy/projetReseau) who participated in this project.

## License

This project is open source.
