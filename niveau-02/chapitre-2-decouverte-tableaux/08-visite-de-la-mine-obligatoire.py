##################################
# fichier 08-visite-de-la-mine-obligatoire.py
# nom de l'exercice : Visite de la mine
# url : http://www.france-ioi.org/algo/task.php?idChapter=651&idTask=0&sTab=task&iOrder=11
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

nbDeplacements = int(input())
tableau = [0] * nbDeplacements
rang = 0

for loop in range(nbDeplacements):
   deplacement = int(input())
   tableau[rang] = deplacement
   rang = rang + 1
   
rang = nbDeplacements - 1
for loop in range(nbDeplacements):
   if tableau[rang] == 1:
      print(2)
   elif tableau [rang] == 2:
      print(1)
   elif tableau[rang] == 3:
      print(3)
   elif tableau[rang] == 4:
      print(5)
   elif tableau[rang] == 5:
      print(4)
   
   rang = rang - 1
     
