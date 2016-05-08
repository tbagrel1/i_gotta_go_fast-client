import pickle

fichier_db = open("../score/local_db.db", "rb")
mon_pickler = pickle.Unpickler(fichier_db)
liste = mon_pickler.load()
print(type(liste))
print(liste)
fichier_db.close()
