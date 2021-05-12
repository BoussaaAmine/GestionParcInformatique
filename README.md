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

###End
