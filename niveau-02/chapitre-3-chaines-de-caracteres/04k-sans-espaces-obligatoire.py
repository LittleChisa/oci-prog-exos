##################################
# fichier 04k-sans-espaces-obligatoire.py
# nom de l'exercice : Sans espaces
# url : http://www.france-ioi.org/algo/task.php?idChapter=595&idTask=0&sTab=task&iOrder=28
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

texte = input()

caracteres = list(texte)

for i in range(len(texte)):
   if caracteres[i] == " ":
      caracteres[i] = "_"

texte = "".join(caracteres)
print(texte)
