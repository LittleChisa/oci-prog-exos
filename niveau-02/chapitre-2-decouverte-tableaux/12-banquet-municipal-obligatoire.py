##################################
# fichier 12-banquet-municipal-obligatoire.py
# nom de l'exercice : Banquet municipal
# url : http://www.france-ioi.org/algo/task.php?idChapter=651&idTask=0&sTab=task&iOrder=17
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

nbPositions = int(input())
nbChangements = int(input())
tableau = [0] * nbPositions
 
for loop in range(nbPositions):
   tableau[loop] = int(input())

for loop in range(nbChangements):
   position1 = int(input())
   position2 = int(input())
   avant = tableau[position1]
   
   tableau[position1] = tableau[position2]
   tableau[position2] = avant
   
 
for element in tableau:
   print(element)
