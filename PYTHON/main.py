###############################################
##                                           ##
##                Classe main                ##
##               Version : 1.0               ##
##           Editeur : Omar & Amine          ##
##                                           ##
###############################################
from Parc import Parc

parcmachine = Parc()
choix=''
print("Ce programme permet de gerer votre parc \n")

while (choix !='q'):
    print('1) Afficher les machines du parc')
    print('2) Rechercher une machine')
    print('3) Supprimer une machine')
    print('4) Mettre a Jour une machine')
    print('5) Ajouter une machine')
    print('q) Quitter')
    choix=input("Votre choix : ")
    if(choix=='1'):
        print(parcmachine.all())
    elif(choix=='2'):
        print(parcmachine.rechercher())
    elif(choix=='3'):
        print(parcmachine.delete())
    elif(choix=='4'):
        print(parcmachine.updateMachine())
    elif(choix=='5'):
        print(parcmachine.add())
    elif(choix=='q'):
        print(parcmachine.save())
    else:
        print("Choix non connu ! ")

#parcmachine.allmachine['omar'].affiche()