#!/bin/bash

FILE="plats.txt"

touch $FILE

while true
do
echo "======================="
echo "RESTAURANT MANAGEMENT"
echo "======================="

echo "1. Ajouter un plat"
echo "2. Afficher les plats"
echo "3. Rechercher un plat"
echo "4. Quitter"

read -p "Choix : " choix

case $choix in

1)
read -p "Nom du plat : " nom
read -p "Prix : " prix
read -p "Categorie : " categorie

echo "$nom | $prix | $categorie" >> $FILE

echo "Plat ajouté !"
;;

2)
cat $FILE
;;

3)
read -p "Nom du plat : " search
grep "$search" $FILE
;;

4)
echo "Au revoir"
exit
;;

*)
echo "Choix invalide"
;;

esac

done