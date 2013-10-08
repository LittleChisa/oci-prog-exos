##################################
# fichier nombre-de-personnes-a-la-fete-entrainement.py
# nom de l'exercice :  Nombre de personnes à la fête
# url : http://www.france-ioi.org/algo/task.php?idChapter=648&idTask=0&sTab=task&iOrder=6
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

nbPersonnes = int(input())
total = 0
maximum = 0

for loop in range(nbPersonnes * 2):
   dundundun = int(input())
   if dundundun > 0:
      total = total + 1
   else:
      total = total - 1
   if total > maximum:
      maximum = total
      
print(maximum)
