import socket

client_to_serv = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_to_serv.connect(("pi-pc", 25565))

msg = raw_input("votre message:\n>>> ")
client_to_serv.send(msg + "\end")
msg_recu = ""
while msg_recu[-4:] != "\end":
    msg_recu += client_to_serv.recv(1024)
msg_recu = msg_recu[:-4]
print(msg_recu)
client_to_serv.close()
