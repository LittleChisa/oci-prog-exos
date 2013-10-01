##################################
# fichier espion-etranger-entrainement.py
# nom de l'exercice :  Espion étranger
# url : http://www.france-ioi.org/algo/task.php?idChapter=648&idTask=0&sTab=task&iOrder=1
# type : entrainement
#
# Nom du chapitre : 
#
# Compétence développée : 
#
# auteur : 
##################################

# chargement des modules


# mettre votre code ici

dateDebut = int(input())
dateFin = int(input())

suspects = 0

nbEntrees = int(input())

for loop in range(nbEntrees):
   dateEntree = int(input())

   if (dateEntree >= dateDebut) and (dateEntree <= dateFin):
      suspects = suspects + 1

print(suspects)
