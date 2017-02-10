# PowerDroid-ScriptAnalyser

Cette partie du projet POWERDROID est celle qui va récupérer les données (en Watt) que le power monitor mesure sur son input et donc ce que le téléphone consomme comme énergie.

###Autres repos du projet :
Powerdroid : https://github.com/Soulk/PowerDroid 

PowerDroid-ScriptLauncher : https://github.com/Soulk/PowerDroid-ScriptLauncher

Le script collectData.py va créer un fichier csv (data.csv) lui même contenu dans un dossier caché (.powerdroid), dans le dossier User. Il utilise monsoon.py qui est l'API permettant d'utiliser le powermonitor (https://www.msoon.com/LabEquipment/PowerMonitor/).

## Installation

## Lancement du script
collectData.py va lancer la collecte des données depuis le power monitor.

Pour lancer collectData.py :
```sh
$ sudo python collectData.py <fichier csv> <fichier power monitor> <fréquence en seconde> <option -s> 
```
Exemple (pour initialiser le power monitor):
```sh
$ sudo python collectData.py data.csv /dev/ttyACM0 1 -s 
```
Exemple (pour lancer la collecte de données):
```sh
$ sudo python collectData.py data.csv /dev/ttyACM0 1 
```

## Traitement des donneés

Les données sont donc stockées dans ~/.powerdroid/data.csv
Elle sont de cette forme :

> tick (hz),Watt (W)
> 0,0.03201667060266392
> 1,0.023462962037591625
> 2,0.03255552551267791

Les valeurs de la 2e colonnes sont donc calculé avec les valeurs (en Ampère) données par le power monitor. 
Watt = Amp * Volt (set à 3.7, valeur max)
