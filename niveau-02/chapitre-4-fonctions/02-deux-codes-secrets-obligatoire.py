##################################
# fichier 02-deux-codes-secrets-obligatoire.py
# nom de l'exercice : Deux codes secrets
# url : http://www.france-ioi.org/algo/task.php?idChapter=509&idTask=0&sTab=task&iOrder=3
# type : obligatoire
#
# Chapitre : chapitre-4-fonctions
#
# Compétence développée : 
#
# auteur : 
##################################

# chargement des modules


# mettre votre code ici

def lireCode():
   tentative = 0
   while tentative != code:
      print("Entrez le code :")
      tentative = int(input())

code = 4242
lireCode()

print("Premier code bon.")

code = 2121
lireCode()

print("Bravo.")
