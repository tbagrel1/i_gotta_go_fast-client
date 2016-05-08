#!/usr/bin/python2
# -*- coding: utf-8 -*

from Crypto.Cipher import AES

encodeur = AES.new('mot_de_passe_16o', AES.MODE_CBC, "vecteur_init_16o")
message = raw_input("Message :\n>>> ")
message += "\0" * (16 - (len(message) % 16))
mess_code = encodeur.encrypt(message)

#------------------------------------------------------------------------------

decodeur = AES.new('mot_de_passe_16o', AES.MODE_CBC, "vecteur_init_16o")
mess_decode = decodeur.decrypt(mess_code)
mess_decode = mess_decode.replace("\0", "")
print(mess_decode)
