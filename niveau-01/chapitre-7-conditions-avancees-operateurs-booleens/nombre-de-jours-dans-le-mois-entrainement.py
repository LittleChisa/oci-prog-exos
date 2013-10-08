##################################
# fichier nombre-de-jours-dans-le-mois-entrainement.py
# nom de l'exercice :  Nombre de jours dans le mois
# url : http://www.france-ioi.org/algo/task.php?idChapter=648&idTask=0&sTab=task&iOrder=4
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

nbMois = int(input())

if ((nbMois >= 1) and (nbMois <= 3)) or ((nbMois >= 7) and (nbMois <= 9)):
   print(30)
if ((nbMois >= 4) and (nbMois <= 6)) or (nbMois == 10):
   print(31)
if nbMois == 11:
   print(29)
