import socket

client_to_serv = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_to_serv.connect(("localhost", 25565))

msg_recu = ""
while msg_recu[-4:] != "\end":
    msg_recu += client_to_serv.recv(1024)
msg_recu = msg_recu[:-4]
print(msg_recu)

if msg_recu == "OK":
    msg = raw_input("votre message:\n>>> ")
    client_to_serv.send(msg + "\end")

    msg_recu = ""
    while msg_recu[-4:] != "\end":
        msg_recu += client_to_serv.recv(1024)
    msg_recu = msg_recu[:-4]
    print(msg_recu)

    if msg_recu == "OK":
        del msg

    client_to_serv.close()

class HandleScoreClient(object):
    def __init__(self):
        object.__init__()
        self.suppr_score = False

    def envoyerScore(self, score):
        client_to_serv = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        client_to_serv.connect(("localhost", 25565))

        msg_recu = ""
        while msg_recu[-4:] != "\end":
            msg_recu += client_to_serv.recv(1024)
        msg_recu = msg_recu[:-4]
        print(msg_recu)

        if msg_recu == "OK":
            client_to_serv.send(msg + "PUSH\end")

            msg_recu = ""
            while msg_recu[-4:] != "\end":
                msg_recu += client_to_serv.recv(1024)
            msg_recu = msg_recu[:-4]
            print(msg_recu)
            if msg_recu == "OK":

                # On envoie le score
                # client_to_serv.send(score)

                msg_recu = ""
                while msg_recu[-4:] != "\end":
                    msg_recu += client_to_serv.recv(1024)
                msg_recu = msg_recu[:-4]
                print(msg_recu)

                if msg_recu == "OK":
                    self.suppr_score = True

    def recevoirScore(self):
        client_to_serv = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        client_to_serv.connect(("localhost", 25565))

        msg_recu = ""
        while msg_recu[-4:] != "\end":
            msg_recu += client_to_serv.recv(1024)
        msg_recu = msg_recu[:-4]
        print(msg_recu)

        if msg_recu == "OK":
            client_to_serv.send(msg + "PULL\end")

            msg_recu = ""
            while msg_recu[-4:] != "\end":
                msg_recu += client_to_serv.recv(1024)
            msg_recu = msg_recu[:-4]
            print(msg_recu)
            if msg_recu == "OK":

                # On envoie le score
                # client_to_serv.send(score)

                msg_recu = ""
                while msg_recu[-4:] != "\end":
                    msg_recu += client_to_serv.recv(1024)
                msg_recu = msg_recu[:-4]
                print(msg_recu)

                if msg_recu == "OK":
                    self.suppr_score = True
