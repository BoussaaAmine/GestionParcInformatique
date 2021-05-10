###############################################
##                                           ##
##                Classe Parc                ##
##               Version : 1.0               ##
##           Editeur : Omar & Amine          ##
##                                           ##
###############################################



from Machine import Machine
class Parc:

    allmachine = {}

    #initie le parc des machines
    def __init__(self):
        dico = {'nom':'','ip':'127.0.0.1','cpu':0,'ram':0,'disk':0,'s_disk':0,'os':'','vers':''}
        self.allmachine = Machine(dico).lister()
    #Check if key exist in dictionnary allmachine
    def checkKey(self, key):
        if key in self.allmachine.keys():
            return True
        else:
            return False

    #verification adresse ip
    def checkip(self,ip):
        try:
            myip = ip.split(".")
            if(len(myip) != 4):
                return False
            #if(type(int(myip[0])) is int and type(int(myip[1])) is int and type(int(myip[2])) is int and type(int(myip[3])) is int):
            p1 = int(myip[0])
            p2 = int(myip[1])
            p3 = int(myip[2])
            p4 = int(myip[3])
            if(0 < p1 <= 255) :
                if(0 <= p2 <= 255) :
                    if (0 <= p3 <= 255) :
                        if (0 < p4 <= 255):
                            return True
            return False
        except ValueError:
            return False
    # recherche une machine par hostname
    def rechercher(self):
        try:
            hostname = input("Veuillez saisir le HostName Rechercher: ")
            return self.allmachine[hostname].affiche()
        except KeyError:
            return "\n ----------- HostName not found ------------\n"

    # supprime une machine par hostname
    def delete(self):
        try:
            hostname = input("Veuillez saisir le HostName Rechercher: ")
            del self.allmachine[hostname]
            return "\n ----------- machine " + hostname + " supprimé ------------\n"
        except KeyError:
            return "HostName not found"

    # met a jour une machine dans allmachine
    def updateMachine(self):
        dico = {'nom':'','ip':'127.0.0.1','cpu':0,'ram':0,'disk':0,'s_disk':0,'os':'','vers':''}
        try:
            dico['nom'] = input("Veuillez saisir le HostName Rechercher: ")
            dico['ip'] = input("Veuillez saisir la nouvelle adresse IP: ")
            while(self.checkip(dico['ip'])==False):
                dico['ip'] = input("adresse ip invalide, reessayer (1.0.0.1-255.255.255.255) ")
            dico['cpu'] = input("Veuillez saisir Nombre CPU: ")
            dico['ram'] = input("Veuillez saisir la taille de RAM: ")
            dico['disk'] = input("Veuillez saisir le nombre de disque(s): ")
            dico['s_disk'] = input("Veuillez saisir la tailles de(s) disque(s): ")
            dico['os']  = input("Veuillez saisir l'os: ")
            dico['vers'] = input("Veuillez saisir la version: ")
            self.allmachine[dico['nom']].UpDate(dico)
            return "\n ----------- machine " + dico['nom'] + " mis à jour------------\n"
        except KeyError:
            return "\n ----------- HostName not found------------\n"

    # ecrase le fichier machines avec l'ensemble des modification apporté a la liste des machines (fin du programme)
    #version.strip() permet de supprimé le saut de ligne en trop a la fin de la machine
    def save(self):
        monFichier = open("machine.txt", "w")
        newfile = ""
        for cle, valeur in self.allmachine.items():
            newfile += "{},{},{},{},{},{},{},{}\n".format(valeur.nom,valeur.ip,valeur.nb_cpu,valeur.ram,valeur.nb_disk,valeur.size_disk,valeur.os,valeur.version.strip())
        monFichier.write(newfile)
        monFichier.close()
        return "\n ----------- les modifications ont été enregistrées------------\n"

    #afficher tout le parc
    def all(self):
        allparc = ""
        for cle, valeur in self.allmachine.items():
            allparc += valeur.affiche() + "\n ---------------- \n" 
        return allparc
        #Ajouter machine au marc
    def add(self):
        dico = {'nom':'','ip':'','cpu':0,'ram':0,'disk':0,'s_disk':0,'os':'','vers':''}
        dico['nom'] = input("Veuillez saisir le HostName de la nouvelle machine: ")
        if(self.checkKey(dico['nom'])):
            return "\n ----------- Machine already exists ------------\n"
        dico['ip'] = input("Veuillez saisir son adresse IP: ")
        while(self.checkip(dico['ip'])==False):
            dico['ip'] = input("adresse ip invalide, reessayer (1.0.0.1-255.255.255.255) ")
        dico['cpu'] = input("Veuillez saisir Nombre CPU: ")
        dico['ram'] = input("Veuillez saisir la taille de RAM: ")
        dico['disk'] = input("Veuillez saisir le nombre de disque(s): ")
        dico['s_disk'] = input("Veuillez saisir la tailles de(s) disque(s): ")
        dico['os']  = input("Veuillez saisir l'os: ")
        dico['vers'] = input("Veuillez saisir la version: ")
        self.allmachine[dico['nom']] = Machine(dico)
        return "\n ----------- machine " + dico['nom'] + " ajoutée------------\n"
    
    