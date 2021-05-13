#################################################
############     Connect to API    ##############
############ Implement ALL Methode ##############
############ Get_ALL, Search ,Add, ##############
############   Update And Remove   ##############
#################################################
from flask import Flask, request
import json
import re
from Parc import Parc
from Machine import Machine
p = Parc()
app = Flask(__name__)


#################################################
################ 127.0.0.1:5000 #################
#################################################
@app.route("/")
def home():
    return "welcome try with 127.0.0.1:5000/machine/<hostname>* \n* optionnel "

#################################################
####### Retourne JSON Format d'une machine ######
#################################################
@app.route("/machine/<hostname>", methods=["GET"])
def getMachine(hostname):
    try :
        return json.dumps(p.allmachine[hostname].__dict__)
    except KeyError:
        return "HostName not found"

#################################################
####### Retourne JSON Format des machines #######
#################################################
@app.route("/machine", methods=["GET"])
def getAllMachine():
    res = ""
    for key, value in p.allmachine.items():
        res+=json.dumps(value.__dict__)
    return res


#################################################
############### Ajoute une Machine ##############
#################################################
@app.route("/machine", methods=["POST"])
def AddMachine():
    nb_param = 0
    msg = "rien ok ? "
    
    dico = {'nom':'','ip':'','cpu':'','ram':'','disk':'','s_disk':'','os':'','vers':''}
    if request.form:
        if request.form.get("nom"):
            dico['nom'] = request.form.get("nom")
        if request.form.get('ip'):
            ip = request.form.get('ip')
            if (p.checkip(ip)):
                dico['ip'] = ip
        if request.form.get('nb_cpu'):
            dico['nb_cpu'] = request.form.get('nb_cpu')
        else :
            dico['nb_cpu'] =1
        if request.form.get('ram'):
            dico['ram'] = request.form.get('ram')
        if request.form.get('nb_disk'):
            dico['nb_disk'] = request.form.get('nb_disk')
        else : 
            dico['nb_disk'] = 1
        if request.form.get('size_disk'):
            dico['size_disk'] = request.form.get('size_disk')
        if request.form.get('os'):
            dico['os'] = request.form.get('os')
        if request.form.get('version'):
            dico['version'] = request.form.get('version')
        res = p.add2(dico)
    return res


#################################################
############## Supprime une Machine #############
#################################################
@app.route("/machine/<hostname>", methods=["DELETE"])
def delMachine(hostname):
    try: 
        p.deleteAPI(hostname)
        return "{} deleted".format(hostname)
    except KeyError:
        return "HostName not found"



#################################################
############### Ajoute une Machine ##############
#################################################
@app.route("/machine/<hostname>", methods=["PUT"])
def UpDateMachine(hostname):
    nb_param = 0
    msg = "rien ok ? "
    try:
        if request.form.get('ip'):
            ip = request.form.get('ip')
            if (p.checkip(ip)):
                p.allmachine[hostname].ip = ip
            else : 
                return "ip invalide"
        if request.form.get('nb_cpu'):
            p.allmachine[hostname].nb_cpu = request.form.get('nb_cpu')
        if request.form.get('ram'):
            p.allmachine[hostname].ram = request.form.get('ram')
        if request.form.get('nb_disk'):
            p.allmachine[hostname].nb_disk = request.form.get('nb_disk')
        if request.form.get('size_disk'):
            p.allmachine[hostname].size_disk = request.form.get('size_disk')
        if request.form.get('os'):
            p.allmachine[hostname].os = request.form.get('os')
        if request.form.get('version'):
            p.allmachine[hostname].version = request.form.get('version')
        
        p.save()
        return "Update " + hostname + " Done !"
    except KeyError:
        return "HostName not foud" 


app.run()