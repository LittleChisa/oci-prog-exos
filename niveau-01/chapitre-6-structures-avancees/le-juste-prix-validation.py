##################################
# fichier le-juste-prix-validation.py
# nom de l'exercice :  Le juste prix
# url : http://www.france-ioi.org/algo/task.php?idChapter=647&idTask=0&sTab=task&iOrder=8
# type : validation
#
# Nom du chapitre : 
#
# Compétence développée : 
#
# auteur : 
##################################

# chargement des modules


# mettre votre code ici

nbMarchands = int(input())
minimum = 1000000
position = 0
marchands = 0

for loop in range(nbMarchands):
      prix = int(input())
      position = position + 1
      if prix <= minimum:
         minimum = prix
         marchands = position
   
print(marchands)
