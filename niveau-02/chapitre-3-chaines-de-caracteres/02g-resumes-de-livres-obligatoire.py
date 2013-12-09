##################################
# fichier 02g-resumes-de-livres-obligatoire.py
# nom de l'exercice : Résumés de livres
# url : http://www.france-ioi.org/algo/task.php?idChapter=595&idTask=0&sTab=task&iOrder=9
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

nbLivres = int(input())
longueurMinimale = int(input())

for loop in range(nbLivres):
   titre = input()
   resume = input()
   
   longueur = len(resume)
   if longueur < longueurMinimale:
      print(titre)
      
#ah, en fait, longueur est une variable inutile orz;;;
