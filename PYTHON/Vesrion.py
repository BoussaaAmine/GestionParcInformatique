import random
import string
class Version:
    __prop['systemProp.http.proxyHost']='proxy'
    __prop['systemProp.http.proxyPort']='8081'
    __prop['systemProp.http.nonProxyHosts']='192.168.1.12'
    __prop['systemProp.https.proxyHost']='proxy'
    __prop['systemProp.https.proxyPort']='8081'
    __prop['systemProp.https.nonProxyHosts']='192.168.1.12'
    __prop['nom'] = "Gestion Parc Informatique"
    __prop['Version'] = 1.0
    __prop['auteur'] = "Omar & Amine"
    __prop['licens'] = ""
    __file = "/var/lib/jenkins/workspace/GestionParcInformatique/"


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
        monFichier = open(self.___file + "gradle.properties", "r")
        maLine=monFichier.readline()
        self.__prop['systemProp.http.proxyHost']=maLine.split("=")[1].strip()
        maLine=monFichier.readline()
        self.__prop['systemProp.http.proxyPort']=maLine.split("=")[1].strip()
        maLine=monFichier.readline()
        self.__prop['systemProp.http.nonProxyHosts']=maLine.split("=")[1].strip()
        maLine=monFichier.readline()
        self.__prop['systemProp.https.proxyHost']=maLine.split("=")[1].strip()
        maLine=monFichier.readline()
        self.__prop['systemProp.https.proxyPort']=maLine.split("=")[1].strip()
        maLine=monFichier.readline()
        self.__prop['systemProp.https.nonProxyHosts']=maLine.split("=")[1].strip()
        maLine=monFichier.readline()
        self.__prop['nom'] = maLine.split("=")[1].strip()
        maLine=monFichier.readline()
        self.__prop['Version'] = float(maLine.split("=")[1]).strip()
        maLine=monFichier.readline()
        self.__prop['auteur'] = maLine.split("=")[1].strip()
        maLine=monFichier.readline()
        self.__prop['licens'] = maLine.split("=")[1].strip()
        monFichier.close()

    
#################################################
######     Auto genere license 50 char    #######
#################################################
    def newLicense(self):
        letters = string.ascii_letters
        self.__prop['licens'] = ''.join(random.choice(letters) for i in range(50))
        
        
#################################################
###### Update and save des modifications ########
#################################################

    def save(self):
        __prop['Version'] +=  0.1
        self.newLicense()
        monFichier = open(self.___file + "gradle.properties", "w")
        v = "%.1f" % float(self.Version)
        monFichier.write("systemProp.http.proxyHost={}\n,systemProp.http.proxyPort={}\n,systemProp.http.nonProxyHosts={}\n,systemProp.https.proxyHost={}\n,systemProp.https.proxyPort={}\n,systemProp.https.nonProxyHosts={}\n,nom={}\n,Version={}\n,auteur={}\n,licens={}\n".format(self.__prop['systemProp.http.proxyHost'],self.__prop['systemProp.http.proxyPort'],self.__prop['systemProp.http.nonProxyHosts'],self.__prop['systemProp.https.proxyHost'],self.__prop['systemProp.https.proxyPort'],self.__prop['systemProp.https.nonProxyHosts'],self.__prop['nom'],self.__prop['Version'],self.__prop['auteur'],self.__prop['licens']))
        monFichier.close()
        return "la nouvelle license est : " + self.licens




#################################################
######     Exec le save et automatise     #######
######             la gestion             #######
#################################################
v = Version()
print(v.save())