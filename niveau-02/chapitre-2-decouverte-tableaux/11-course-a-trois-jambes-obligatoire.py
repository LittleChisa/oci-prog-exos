##################################
# fichier 11-course-a-trois-jambes-obligatoire.py
# nom de l'exercice : Course à trois jambes
# url : http://www.france-ioi.org/algo/task.php?idChapter=651&idTask=0&sTab=task&iOrder=16
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

nbParticipants = int(input())
tableau = [0] * nbParticipants

rang = 0

for loop in range(nbParticipants):
   entier = int(input())
   tableau[rang] = entier
   rang = rang + 1

tableau.sort()
rang = 0

groupe = nbParticipants // 2

for loop in range(groupe):
   
   petitEntier = tableau[rang]
   grandEntier = tableau[nbParticipants -1]
   
   print("{} {}".format(petitEntier, grandEntier)) 
   rang = rang + 1
   nbParticipants = nbParticipants - 1
