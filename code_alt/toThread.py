# Import toThread (A replier)
if True:  # Ajout du module threadTBAG
    from threading import *

    def static(var_name, value):
        def decorate(func):
            setattr(func, var_name, value)
            return func
        return decorate

    # Définition des classes et fonctions :
    class aThread(Thread):
        def __init__(self, threadID, name, command):
            Thread.__init__(self)
            self.threadID = threadID
            print("id: <{}>".format(self.threadID))
            self.name = name
            print("name: <{}>".format(self.name))
            self.command = command
            print("command: <{}>".format(self.command))

        def run(self):
            print("Starting " + self.name + " : " + str(self.threadID) +
                  " { " + self.command + " }")
            exec(self.command)
            print("Exiting " + self.name + " : " + str(self.threadID) +
                  " { " + self.command + " }")

    @static("c", 0)
    def toThread(name, command):
        exec("Thread_" + str(toThread.c) + " = aThread(" + str(toThread.c) +
             ", \"" + name + "\", \"" + command + "\")")
        exec("Thread_" + str(toThread.c) + ".daemon = True")
        exec("Thread_" + str(toThread.c) + ".start()")
        toThread.c += 1
