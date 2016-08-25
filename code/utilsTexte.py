#!/usr/bin/python2
# -*- coding: utf-8 -*
#ref_to_md

from Crypto.Cipher import AES
import binascii

def crypterTexte(texte):
    encodeur = AES.new("FAU8PdmPi7dxXFc9", AES.MODE_CBC, "84yD8kXUiZsyc22n")
    texte += "\0" * (16 - (len(texte) % 16))
    texte_code = binascii.b2a_hex(encodeur.encrypt(texte))
    return texte_code

def decrypterTexte(texte_code):
    decodeur = AES.new("FAU8PdmPi7dxXFc9", AES.MODE_CBC, "84yD8kXUiZsyc22n")
    texte = decodeur.decrypt(binascii.a2b_hex(texte_code))
    while texte[-1] == "\0":
        texte = texte[:-1]
    return texte

def main():
    def menu():
        choix = raw_input("\nQue voulez vous faire ?\n    1. Encoder\n" +
                          "    2. Décoder\n>>> ")
        return choix

    def ouvrirCrypterTexte(nom):
        try:
            nom_source = "_sources_txt/" + nom + ".txt"
            nom_dest = "txt/" + nom + "_e.txt"

            print("\n--- CRYPTAGE ---")
            print("[ {} ] -> [ {} ]".format(nom_source, nom_dest))

            fichier_source = open(nom_source, "r")
            fichier_dest = open(nom_dest, "w")

            source = fichier_source.read()
            dest = crypterTexte(source)

            print("[ {} ] -> [ {} ]".format(source[:min(len(source), 10)],
                                            dest[:min(len(source), 10)]))

            fichier_dest.write(dest)

            fichier_source.close()
            fichier_dest.close()

            print("--> Terminé\n")
        except:
            print("--> Erreur\n")

    def ouvrirDecrypterTexte(nom):

        try:
            nom_source = "txt/" + nom + "_e.txt"

            print("\n--- DECRYPTAGE ---")

            fichier_source = open(nom_source, "r")

            print("[ {} ]".format(nom_source))

            source = fichier_source.read()
            dest = decrypterTexte(source)

            print("[ {} ]".format(dest))
            print("--> Terminé\n")
        except:
            print("--> Erreur\n")

    while True:
        choix = menu()
        if choix[0:2] == "1 ":
            ouvrirCrypterTexte(choix[2:])
        elif choix[0:2] == "2 ":
            ouvrirDecrypterTexte(choix[2:])
        elif choix == "\exit":
            return
        else:
            print("--> Choix incorrect. Recommencez")

if __name__ == "__main__":
    main()
