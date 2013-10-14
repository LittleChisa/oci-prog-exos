##################################
# fichier departement-d-architecture--construction-d-une-pyramide-validation.py
# nom de l'exercice :  Département d'architecture : construction d'une pyramide
# url : http://www.france-ioi.org/algo/task.php?idChapter=649&idTask=0&sTab=task&iOrder=6
# type : validation
#
# Nom du chapitre : 
#
# Compétence développée : 
#
# auteur : 
##################################

# chargement des modules


# mettre votre code ici

pierresMax = int(input())

nbPierres = 0
largeurCote = 0
hauteur = 0

while pierresMax > nbPierres:
   largeurCote = largeurCote + 1
   hauteur = hauteur + 1
   
   nbPierres = nbPierres + largeurCote ** 2

if pierresMax < nbPierres:
   hauteur = hauteur - 1
   nbPierres = nbPierres - largeurCote ** 2

print(hauteur)
print(nbPierres)
