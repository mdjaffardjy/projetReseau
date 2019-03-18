# Projet Programmation Réseau - Serveur Chat-Room

  This chat-room server is composed of multiple rooms. A user can chat with other users that are present in the same room, using the computer terminal.
  The user can navigate in the different rooms and create new ones using commands, and can send private messages to all users connected to the server.
   
### Included

This README
All source files (server.py and client.py)


## Getting started

This software can be run on one machine, or on multiple machines, using Python2.7.

Libraries that need to be installed are :
-socket
-select
-sys
-thread
-collections

## Installing

First, install the server using the command in the computer terminal :
```python
python server.py <localhost> <port>
```

For example : ```python python server.py 127.0.0.1 8888```

Once the server is set, users that want to connect to the server should use the following command :
```python
python client.py <localhost> <port>
```

## Authors

* **Marine Djaffardjy** - *Initial work* - [GitHub](https://github.com/mdjaffardjy)

* **Olivia Brunet** - *Initial work* - [GitHub](https://github.com/OliviaBnt)

* **Théophile Moreal de Brevans** - *Initial work* - [GitHub](https://github.com/MorealDeBrevans/)

See also the list of [contributors](https://github.com/mdjaffardjy/projetReseau) who participated in this project.

## License

This project is open source.
