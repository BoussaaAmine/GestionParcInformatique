###############################################
##                                           ##
##                Classe Parc                ##
##               Version : 1.0               ##
##           Editeur : Omar & Amine          ##
##                                           ##
###############################################



from machine import Machine
class Parc:
    allmachine = {}
    
    
#################################################
############## init parc machines ###############
#################################################
    def __init__(self):
        dico = {'nom':'','ip':'127.0.0.1','cpu':0,'ram':0,'disk':0,'s_disk':0,'os':'','vers':''}
        self.allmachine = Machine(dico).lister()
        
        
        
#################################################
######    Les Méthodes de Vérifcations   ########
#################################################
    
#################################################
###### Saisie & Vérifie que c'est un int ########
#################################################
    def saisieINT(self,msg):
        test = False
        n=0
        while (not test):
            try:
                num = input(msg).strip()
                if (num == 'q' and n==1):
                    return 'q'
                n+=1
                if (int(num)):
                    return num
            except ValueError:
                print("Must be integer (q to leave)")
        return num
        
        
#################################################
###### Saisie & Vérifie que c'est un int ########
######       avec default res = 1        ########
#################################################
    def saisieIntDef1(self,msg):
        test = False
        n=0
        while (not test):
            try:
                num = input(msg).strip()
                if (num == 'q' and n==1):
                    return 'q'
                n+=1
                if(num == ''):
                    num = 1
                    test = True
                else :
                    if (int(num)<1):
                        test=False
                        print("Must be integer and upper than 0 (q to leave)")
                    else :
                        test = True
            except ValueError:
                print("Must be integer and upper than 0 (q to leave)")
        return num
    

#################################################
############## Verifie Key unique ###############
#################################################
    def checkKey(self, key):
        if key in self.allmachine.keys():
            return True
        else:
            return False
            
#################################################
############## Verifie IP correct ###############
##############      no char       ###############
##############        IPV4        ###############
##############  between 0and 255  ###############
#################################################
    def checkip(self,ip):
        try:
            myip = ip.split(".")
            if(len(myip) != 4):
                return False
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
            
#################################################
######                                   ########
######                                   ########
######               CRUD                ########
######                                   ########
######                                   ########
#################################################
            
#################################################
########### Recherche Machine by key ############
#################################################
    def rechercher(self):
        try:
            hostname = input("Veuillez saisir le HostName Rechercher: ")
            return self.allmachine[hostname].affiche()
        except KeyError:
            return "\n ----------- HostName not found ------------\n"
            
#################################################
########### Supprime Machine by key  ############
#################################################
    def delete(self):
        try:
            hostname = input("Veuillez saisir le HostName Rechercher: ")
            del self.allmachine[hostname]
            return "\n ----------- machine " + hostname + " supprimé ------------\n"
        except KeyError:
            return "HostName not found"
            
            
            
#################################################
############ Modifie Machine by key #############
#################################################
    def updateMachine(self):
        dico = {'nom':'','ip':'127.0.0.1','cpu':0,'ram':0,'disk':0,'s_disk':0,'os':'','vers':''}
        try:
            dico['nom'] = input("Veuillez saisir le HostName Rechercher: ")
            dico['ip'] = input("Veuillez saisir la nouvelle adresse IP: ")
            while(self.checkip(dico['ip'])==False):
                dico['ip'] = input("adresse ip invalide, reessayer (1.0.0.1-255.255.255.255) ")
            dico['cpu'] = self.saisieIntDef1("Veuillez saisir Nombre CPU (default 1): ")
            if (dico['cpu'] == 'q'):
                return "update annuler"
            dico['ram'] = self.saisieINT("Veuillez saisir la taille de RAM (GO): ")
            if (dico['ram'] == 'q'):
                return "update annuler"
            dico['disk'] = self.saisieIntDef1("Veuillez saisir le nombre de disque(s) (default 1): ")
            if (dico['disk'] == 'q'):
                return "update annuler"
            dico['s_disk'] = self.saisieINT("Veuillez saisir la tailles de(s) disque(s) (GO): ")
            if (dico['s_disk'] == 'q'):
                return "update annuler"
            dico['os']  = input("Veuillez saisir l'os: ")
            dico['vers'] = input("Veuillez saisir la version: ")
            self.allmachine[dico['nom']].UpDate(dico)
            return "\n ----------- machine " + dico['nom'] + " mis à jour------------\n"
        except KeyError:
            return "\n ----------- HostName not found------------\n"
    
            
#################################################
######     Enregistre les changements     #######
######    Dans le fichier des machines    #######
###### écrase le contenue par un nouveau  #######
######   version.strip() supprime le \r   #######
#################################################
    def save(self):
        monFichier = open("machine.txt", "w")
        newfile = ""
        for cle, valeur in self.allmachine.items():
            newfile += "{},{},{},{},{},{},{},{}\n".format(valeur.nom,valeur.ip,valeur.nb_cpu,valeur.ram,valeur.nb_disk,valeur.size_disk,valeur.os,valeur.version.strip())
        monFichier.write(newfile)
        monFichier.close()
        return "\n ----------- les modifications ont été enregistrées------------\n"
        
        
#################################################
########## Liste les machines du parc ###########
#################################################
    def all(self):
        allparc = ""
        for cle, valeur in self.allmachine.items():
            allparc += valeur.affiche() + "\n ---------------- \n" 
        return allparc
        
        
#################################################
##### Ajoute une machine depuis la console ######
#################################################
    def add(self):
        test = False
        dico = {'nom':'','ip':'','cpu':0,'ram':0,'disk':0,'s_disk':0,'os':'','vers':''}
        dico['nom'] = input("Veuillez saisir le HostName de la nouvelle machine: ")
        if(self.checkKey(dico['nom'])):
            return "\n ----------- Machine already exists ------------\n"
        dico['ip'] = input("Veuillez saisir son adresse IP: ")
        while(self.checkip(dico['ip'])==False):
            dico['ip'] = input("adresse ip invalide, reessayer (1.0.0.1-255.255.255.255) ")
        dico['cpu'] = self.saisieIntDef1("Veuillez saisir Nombre CPU (default 1): ")
        if (dico['cpu'] == 'q'):
            return "ajout annuler"
        dico['ram'] = self.saisieINT("Veuillez saisir la taille de RAM (GO): ")
        if (dico['ram'] == 'q'):
            return "ajout annuler"
        dico['disk'] = self.saisieIntDef1("Veuillez saisir le nombre de disque(s) (default 1): ")
        if (dico['disk'] == 'q'):
            return "ajout annuler"
        dico['s_disk'] = self.saisieINT("Veuillez saisir la tailles de(s) disque(s) (GO): ")
        if (dico['s_disk'] == 'q'):
            return "ajout annuler"
        dico['os']  = input("Veuillez saisir l'os: ")
        dico['vers'] = input("Veuillez saisir la version: ")
        self.allmachine[dico['nom']] = Machine(dico)
        return "\n ----------- machine " + dico['nom'] + " ajoutée------------\n"  
    
    

#################################################
################ Méthode de l'API ###############
#################################################

#################################################
##########   Les méthode d'affichage    #########
##########   ne demande pas de saisie   #########
##############   Rien a changer    ##############
#################################################

#################################################
################   Suppression    ###############
#################################################
    def deleteAPI(self,hostname):
        del self.allmachine[hostname]
        self.save()

#################################################
###############       Ajout       ###############
#################################################
    def add2(self,dico):
        if(self.checkKey(dico['nom'])):
            return "Machine already exists"
        self.allmachine[dico['nom']] = Machine(dico)
        self.save()
        return "Machine Added"
