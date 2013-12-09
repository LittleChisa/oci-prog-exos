##################################
# fichier 02e-une-ligne-sur-deux-obligatoire.py
# nom de l'exercice : Une ligne sur deux
# url : http://www.france-ioi.org/algo/task.php?idChapter=595&idTask=0&sTab=task&iOrder=7
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

nbLignes = int(input())
texte = [0] * nbLignes

for idLigne in range(nbLignes):
   texte[idLigne] = input()
   
   if idLigne % 2 == 0:
      print(texte[idLigne])
