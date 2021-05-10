###############################################
##                                           ##
##              Classe Machine               ##
##               Version : 1.0               ##
##           Editeur : Omar & Amine          ##
##                                           ##
###############################################

class Machine:
    # les différents attributs demandé "typé"
    nom = ""
    ip = ""
    nb_cpu = 0
    ram = 0
    nb_disk = 0
    size_disk = 0
    os = "" 
    version = ""
    #initialisation du constructeur a l'aide d'un dictionnaire
    def __init__(self, dico):
        self.nom = dico['nom']
        self.ip = dico['ip']
        self.nb_cpu = dico['cpu']
        self.ram = dico['ram']
        self.nb_disk = dico['disk']
        self.size_disk = dico['s_disk']
        self.os = dico['os'] 
        self.version = dico['vers']
    
    
    #Définition de la méthode lister
    def lister(self):
        dico = {'nom':'','ip':'127.0.0.1','cpu':0,'ram':0,'disk':0,'s_disk':0,'os':'','vers':''}
        dicoreturn = {}
        monFichier = open("machine.txt", "r")
        maLine=monFichier.readline()
        newfile = ""
        while maLine :
            splitline = maLine.split(",")
            dico['nom'] = splitline[0]
            dico['ip'] = splitline[1]
            dico['cpu'] = splitline[2]
            dico['ram'] = splitline[3]
            dico['disk'] = splitline[4]
            dico['s_disk'] = splitline[5]
            dico['os']  = splitline[6]
            dico['vers'] = splitline[7]
            dicoreturn[splitline[0]] = Machine(dico)
            maLine=monFichier.readline()
        monFichier.close()
        return dicoreturn
    
    # afficher la machine
    def affiche(self):
        return " Hostname : {} \n IP : {} \n Nombre de CPU : {} \n RAM {} GO \n Nombre de Disque(s) : {} \n Taille disque(s) : {} GO \n OS : {} \n Version : {}".format(self.nom,self.ip,self.nb_cpu,self.ram,self.nb_disk,self.size_disk,self.os,self.version)
    
    #update de la machine
    def UpDate(self,dico):
        self.ip = dico['ip']
        self.nb_cpu = dico['cpu']
        self.ram = dico['ram']
        self.nb_disk = dico['disk']
        self.size_disk = dico['s_disk']
        self.os = dico['os'] 
        self.version = dico['vers']
    