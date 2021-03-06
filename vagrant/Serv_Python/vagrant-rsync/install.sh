#!/usr/bin/env bash
### MODE SECURE
set -u # en cas de variable non définit, arreter le script
set -e # en cas d'erreur (code de retour non-zero) arreter le script
# Vérifier que le script est lancé en tant que root
ps_assert_root(){
	REAL_ID="$(id -u)"
	if [ "$REAL_ID" -ne 0 ]; then
		1>&2 echo "ERREUR: Le script doit etre exécuté en tant que root"
		exit 1
	fi
}
ps_assert_root
apt update -y
# install python
apt install python3 python3-dev python3-pip git -q -y
apt remove -y python 
# positionnement de python3 et pip3 dans le profil
ln -s /usr/bin/python3 /usr/bin/python
echo "alias pip=pip3" > ~/.bashrc
#install utilitaire de test dont flask pour expostion de l'api
pip install flask pytest 
#pip install fastapi