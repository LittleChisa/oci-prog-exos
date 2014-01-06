##################################
# fichier 01-code-secret-deux-fois-obligatoire.py
# nom de l'exercice : Code secret deux fois
# url : http://www.france-ioi.org/algo/task.php?idChapter=509&idTask=0&sTab=task&iOrder=1
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

def lireCodesecret():
   code = 0
   while code!= 4242:
      print("Entrez le code :")
      code = int(input())

lireCodesecret()

print("Encore une fois.")


lireCodesecret()

print("Bravo.")
