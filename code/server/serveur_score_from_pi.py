#!/usr/bin/python2
# -*- coding: utf-8 -*

# Import des modules
import socket as so

serv = so.socket(so.AF_INET, so.SOCK_STREAM)
serv.bind(("", 25565))
serv.listen(1)

while True:
	serv_to_client, infos_co = serv.accept()
	print(infos_co)
	msg_recu = ""
	while msg_recu[-4:] != "\end":
		msg_recu += serv_to_client.recv(1024)
	msg_recu = msg_recu[:-4]
	print(msg_recu)	
	serv_to_client.send("Reçu !\end")
	serv_to_client.close()
