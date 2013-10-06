##################################
# fichier amitie-entre-gardes-entrainement.py
# nom de l'exercice :  Amitié entre gardes
# url : http://www.france-ioi.org/algo/task.php?idChapter=648&idTask=0&sTab=task&iOrder=5
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

dateDebut1 = int(input())
dateFin1 = int(input())

dateDebut2 = int(input())
dateFin2 = int(input())

if dateFin1 < dateDebut2:
   print("Pas amis")
if dateFin1 >= dateDebut2:
   if dateDebut1 > dateFin2:
      print("Pas amis")
   else:
      print("Amis")
