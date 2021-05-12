import random
import string
class Version:
    nom = "Gestion Parc Informatique"
    Version = 1.0
    auteur = "Omar & Amine"
    licens = ""



#################################################
######              Gestion              ########
######                Des                ########
######              Versions             ########
######       Auto Version & License      ########
#################################################



#################################################
######       Récupére dernière info      ########
#################################################
    def __init__(self):
        monFichier = open("version.txt", "r")
        maLine=monFichier.readline()
        splitline = maLine.split(",")
        self.nom = splitline[0]
        self.Version = float(splitline[1])
        self.auteur = splitline[2]
        self.licens = splitline[3]
        monFichier.close()

    
#################################################
######     Auto genere license 50 char    #######
#################################################
    def newLicense(self):
        letters = string.ascii_letters
        self.licens = ''.join(random.choice(letters) for i in range(50))
        
        
#################################################
###### Update and save des modifications ########
#################################################

    def save(self):
        self.Version +=  0.1
        self.newLicense()
        monFichier = open("version.txt", "w")
        v = "%.1f" % float(self.Version)
        monFichier.write("{},{},{},{}".format(self.nom,v,self.auteur,self.licens))
        monFichier.close()
        return "la nouvelle license est : " + self.licens




#################################################
######     Exec le save et automatise     #######
######             la gestion             #######
#################################################
v = Version()
print(v.save())