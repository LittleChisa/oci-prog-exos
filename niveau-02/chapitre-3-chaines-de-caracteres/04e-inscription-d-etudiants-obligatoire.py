##################################
# fichier 04e-inscription-d-etudiants-obligatoire.py
# nom de l'exercice : Inscription d’étudiants
# url : http://www.france-ioi.org/algo/task.php?idChapter=595&idTask=0&sTab=task&iOrder=22
# type : obligatoire
#
# Chapitre : chapitre-3-chaines-de-caracteres
#
# Compétence développée : 
#
# auteur : 
##################################

# chargement des modules


# mettre votre code ici

nom = input()

if nom[0] <= "F":
   print(1)

elif nom[0] <= "P":
   print(2)

else:
   print(3)
