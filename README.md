# GestionParcInformatique
TP python gestion parc informatique
### Post Developpeur

- Depuis le repertoire /vagrant/Serv_Python
```
vagrant up
```
- Installation des pré-requis :
```
cd /home/rsync
sudo bash install.sh
```
- Depuis Windows : Copiez le Repertoire PYTHON dans le vagrant-rsync
- Depuis Votre terminal Vagrant : Placez vous dans le répertoire de l'application
1.  Pour tester l'application sur console 
```
python main.py
```
2.  Pour lancer les tests existant
```
python test_IP.py
```
3. Pour passer l'application a une version suppérieur 
```
python Vesrion.py
```
4. Pour lancer l'application via l'API

    1. Executer Flask  
    ```
    python ConnectAPI.py
    ```
    2.  Importer le  fichier 'machine.postman_collection.json' sur PostMan
    3. Les méthodes PostMan :
        1. ADD : Ajoute une machine 
        ```
        curl --location --request POST 'http://127.0.0.1:5000/machine' --form 'nom="blavla"'  --form 'ip="1.1.1.1"' --form 'nb_cpu=""' --form 'ram=""' --form 'nb_disk=""' --form 'size_disk=""' --form 'os=""' --form 'version=""'
        ```
        2. GetAll : Liste les machines (Format JSON)

        ```
        curl --location --request GET 'http://127.0.0.1:5000/machine'
        ``` 
        3. Get1 : Recupère les informations d'une machine (Format JSON)

        ```
        curl --location --request GET 'http://127.0.0.1:5000/machine/MachineName'
        ```
        4. Delete : Supprime la machine
        ```
        curl --location --request DELETE 'http://127.0.0.1:5000/machine/MachineName'
        ```
        5. Met à jour la machine
        ```
        curl --location --request PUT 'http://127.0.0.1:5000/machine/Host_Name2' --form 'ip="127.0.0.3"' --form 'nb_cpu=""' --form 'ram=""' --form 'nb_disk=""' --form 'size_disk=""' --form 'os=""' --form 'version=""'
        ```

<<<<<<< HEAD
### Serveur Nexus
- Pour démmarer le serveur Nexus, lancer la commande:
```
vagrant up nexus
```
-  Se connecter au serveur Nexus 
```
vagrant ssh nexus
```
- récupérer le mot de passe du serveur Nexsus 
```
sudo cat /opt/nexus/sonatype-work/nexus3/admin.password
```
- Ouvrir votre navigateur web, taper l'adress suivante 
```
http://192.168.1.21:8081/
```
- l'interface suivante s'affiche 


![image interface Nexsus1.](/capture/Nexus1.PNG "image interface Nexsus1.")

- Aller à Sing in, s'identifier avec login : admin et mot de passe récupérer dans l'étape présédente, puis Next


![image interface Nexsus2.](/capture/Nexus2.PNG "image interface Nexsus2.")

- Modifer le mot de passe, puis Next 

![image interface Nexsus3.](/capture/Nexus3.PNG "image interface Nexsus3.")

- Choisir l'option Enable anonymous access, puis Next

![image interface Nexsus4.](/capture/Nexus4.PNG "image interface Nexsus4.")

- Choisir create repository

![image interface Nexsus5.](/capture/Nexus5.PNG "image interface Nexsus5.")

- Choisir l'option  raw(hosted)

![image interface Nexsus6.](/capture/Nexus6.PNG "image interface Nexsus6.")

- Dans le champs Name, taper Nexus-Python

![image interface Nexsus7.](/capture/Nexus7.PNG "image interface Nexsus7.")

- Vérifier que le repository est bien crée 

![image interface Nexsus8.](/capture/Nexus8.PNG "image interface Nexsus8.")



### Serveur Jenkins
- Pour démmarer le serveur Jenkins, lancer la commande:
```
vagrant up jenkins
```
-  Se connecter au serveur Jenkins 
 ```
vagrant ssh jenkins
```
- suivre les commandes suivante pour la configuration du webhooks
```
cd /usr/local/bin/
sudo curl -O  https://storage.googleapis.com/webhookrelay/downloads/relay-linux-amd64
sudo mv relay-linux-amd64  relay
sudo chmod +wx /usr/local/bin/relay

```
- Récuprer le mot de passe de Jenkins
```
sudo cat /var/lib/jenkins/secrets/initialAdminPassword

```

- Ouvrir votre navigateur web, taper l'adress suivante 

```
http://192.168.1.20:8080/

```
- S'identifier avec login : admin et mot de passe récupérer dans l'étape présédente, puis Next

![image interface Jenkins1.](/capture/Jenkins1.png "image interface jenkins1.")

- Modifer le mot de passe, puis Next 


![image interface Jenkins2.](/capture/jenkins2.png "image interface jenkins2.")


- Aller dans Configuration globale des outils


![image interface Jenkins9.](/capture/jenkins9.png "image interface jenkins9.")

- Dans la Gradle, renseigner les élements suivants 


![image interface Jenkins10.](/capture/jenkins10.png "image interface jenkins10.")

- Cree un nouveau build, avec le nom ProjetPython, choisir un projet free-style


![image interface Jenkins5.](/capture/jenkins5.png "image interface jenkins5.")

- Cocher la case GitHub project, renseigner l'url du github

![image interface Jenkins6.](/capture/jenkins6.png "image interface jenkins6.")

- Renseigner l'url du github, et */main

![image interface Jenkins7.](/capture/jenkins7.png "image interface jenkins7.")

- Cocher la case GitHub hook triguer for GitSCM poling, dans build mettre le task up et choisir la version gradle

![image interface Jenkins14.](/capture/jenkins14.png "image interface jenkins14.")

- lancer le build manuellement et vérifier qu'il s'exécute correctement
![image interface Jenkins15.](/capture/jenkins15.png "image interface jenkins15.")

- Aller dans l'interface Nexus, et vérifier que le paquage est bien uploder 

![image interface Nexsus9.](/capture/Nexus9.PNG "image interface Nexsus9.")



##End

