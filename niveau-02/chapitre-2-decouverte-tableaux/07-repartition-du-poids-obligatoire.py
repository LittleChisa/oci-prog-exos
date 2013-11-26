##################################
# fichier 07-repartition-du-poids-obligatoire.py
# nom de l'exercice : Répartition du poids
# url : http://www.france-ioi.org/algo/task.php?idChapter=651&idTask=0&sTab=task&iOrder=10
# type : obligatoire
#
# Chapitre : chapitre-2-decouverte-tableaux
#
# Compétence développée : 
#
# auteur : 
##################################

# chargement des modules


# mettre votre code ici

nbCharrettes = int(input())
poidsTotal = 0
tableau = 0
charrettes = [0] * nbCharrettes

for loop in range(nbCharrettes):
   poidsCharrette = float(input())
   charrettes[tableau] = charrettes[tableau] + poidsCharrette
   
   poidsTotal = poidsTotal + poidsCharrette
   tableau = tableau + 1
   
poidsTotal = poidsTotal / nbCharrettes
tableau = 0

for loop in range(nbCharrettes):
   charrettes[tableau] = charrettes[tableau] - poidsTotal
   charrettes[tableau] = charrettes[tableau] * -1
   print(charrettes[tableau])
   tableau = tableau + 1
