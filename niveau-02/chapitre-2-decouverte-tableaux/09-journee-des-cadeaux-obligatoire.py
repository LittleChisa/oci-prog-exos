##################################
# fichier 09-journee-des-cadeaux-obligatoire.py
# nom de l'exercice : Journée des cadeaux
# url : http://www.france-ioi.org/algo/task.php?idChapter=651&idTask=0&sTab=task&iOrder=14
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

nbHabitants = int(input())

tableau = [0] * nbHabitants
rang = 0

for loop in range(nbHabitants):
   fortune = int(input())
   tableau[rang] = fortune
   rang = rang + 1
   
tableau.sort()


if nbHabitants % 2 == 1 :
   nbHabitants = (nbHabitants - 1) // 2
   print(tableau[nbHabitants])

else :
   total = (tableau[nbHabitants // 2 - 1]) + (tableau[nbHabitants // 2])
   print(total / 2)
