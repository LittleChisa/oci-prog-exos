##################################
# fichier l-espion-est-demasque--entrainement.py
# nom de l'exercice :  L'espion est démasqué !
# url : http://www.france-ioi.org/algo/task.php?idChapter=648&idTask=0&sTab=task&iOrder=14
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

for loop in range(nbPersonnes):
   criteresRemplis = 0
   
   taille = int(input())
   age = int(input())
   poids = int(input())
   cheval = int(input())
   cheveuxBruns = int(input())

   if (taille >= 178) and (taille <= 182):
      criteresRemplis = criteresRemplis + 1
   if age >= 34:
      criteresRemplis = criteresRemplis + 1
   if poids < 70:
      criteresRemplis = criteresRemplis + 1
   if cheval == 0:
      criteresRemplis = criteresRemplis + 1
   if cheveuxBruns == 1:
      criteresRemplis = criteresRemplis + 1

   if criteresRemplis == 5:
      print("Très probable")
   elif (criteresRemplis == 3) or (criteresRemplis == 4):
      print("Probable")
   elif criteresRemplis == 0:
      print("Impossible")
   else:
      print("Peu probable")
