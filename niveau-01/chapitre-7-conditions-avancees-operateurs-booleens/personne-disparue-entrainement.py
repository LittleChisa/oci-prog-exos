##################################
# fichier personne-disparue-entrainement.py
# nom de l'exercice :  Personne disparue
# url : http://www.france-ioi.org/algo/task.php?idChapter=648&idTask=0&sTab=task&iOrder=9
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

recherche = int(input())
tailleListe = int(input())

dehors = 0

for loop in range(tailleListe):
   sortie = int(input())
   if sortie == recherche:
      dehors = 0 + 1
  
if dehors > 0:
   print("Sorti de la ville")
else:
   print("Encore dans la ville")
