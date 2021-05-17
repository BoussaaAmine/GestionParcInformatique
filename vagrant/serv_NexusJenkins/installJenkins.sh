#!/bin/bash

sudo apt-get update  
sudo apt-get -y install open-iscsi
sudo apt-get -y install lvm2


mkfs.ext4 /dev/sdb
mkdir -p /backup1
echo "/dev/sdb   /backup1  ext4   defaults    0   0">> /etc/fstab
mount /backup1

## java for jenkins
sudo apt -y update
sudo apt -y install ca-certificates
sudo apt -y install openjdk-11-jdk
sudo apt -y install openjdk-11-jdk

## Jenkins
sudo wget -q -O - https://pkg.jenkins.io/debian-stable/jenkins.io.key | sudo apt-key add -
sudo sh -c 'echo deb https://pkg.jenkins.io/debian-stable binary/ > \
    /etc/apt/sources.list.d/jenkins.list'
	
sudo apt-get update
sudo apt-get -y install jenkins

#start du service Jenkins
sudo service jenkins start
sleep 30
sudo cat /var/lib/jenkins/secrets/initialAdminPassword

#=============Installation Gradle 7 ========================

sudo apt-get -y remove gradle
sudo curl -O https://downloads.gradle-dn.com/distributions/gradle-7.0.1-bin.zip
sudo mkdir /opt/gradle
sudo apt install -y unzip 
sudo unzip -d /opt/gradle gradle-7.0.1-bin.zip

#=============Installation Python  ========================
sudo apt-get -y install python3-pip
#=============Installation git  ========================

sudo apt-get -y install git
