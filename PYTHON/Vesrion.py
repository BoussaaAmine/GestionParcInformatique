import random
import string
class Version:

    __prop = {}
    __file = "/var/lib/jenkins/workspace/GestionParcInformatique/"
    #__file = "/home/rsync/tp_python/"


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
        monFichier = open(self.__file + "gradle.properties", "r")
        try :
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
            self.__prop['Version'] = float(maLine.split("=")[1].strip())
            maLine=monFichier.readline()
            self.__prop['auteur'] = maLine.split("=")[1].strip()
            maLine=monFichier.readline()
            self.__prop['licens'] = maLine.split("=")[1].strip()
        except IndexError:
            self.__prop['systemProp.http.proxyHost']='proxy'
            self.__prop['systemProp.http.proxyPort']='8081'
            self.__prop['systemProp.http.nonProxyHosts']='192.168.1.12'
            self.__prop['systemProp.https.proxyHost']='proxy'
            self.__prop['systemProp.https.proxyPort']='8081'
            self.__prop['systemProp.https.nonProxyHosts']='192.168.1.12'
            self.__prop['nom'] = "Gestion Parc Informatique"
            self.__prop['Version'] = 1.0
            self.__prop['auteur'] = "Omar & Amine"
            self.__prop['licens'] = self.newLicense()
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
        self.__prop['Version'] +=  0.1
        self.newLicense()
        monFichier = open(self.__file + "gradle.properties", "w")
        v = "%.1f" % float(self.__prop['Version'])
        monFichier.write("systemProp.http.proxyHost={}\nsystemProp.http.proxyPort={}\nsystemProp.http.nonProxyHosts={}\nsystemProp.https.proxyHost={}\nsystemProp.https.proxyPort={}\nsystemProp.https.nonProxyHosts={}\nnom={}\nVersion={}\nauteur={}\nlicens={}\n".format(self.__prop['systemProp.http.proxyHost'],self.__prop['systemProp.http.proxyPort'],self.__prop['systemProp.http.nonProxyHosts'],self.__prop['systemProp.https.proxyHost'],self.__prop['systemProp.https.proxyPort'],self.__prop['systemProp.https.nonProxyHosts'],self.__prop['nom'],v,self.__prop['auteur'],self.__prop['licens']))
        monFichier.close()
        return "la nouvelle license est : " + self.__prop['licens']

#################################################
######     Exec le save et automatise     #######
######             la gestion             #######
#################################################
v = Version()
print(v.save())