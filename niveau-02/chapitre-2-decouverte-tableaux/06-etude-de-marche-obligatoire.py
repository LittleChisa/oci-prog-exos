##################################
# fichier 06-etude-de-marche-obligatoire.py
# nom de l'exercice : Étude de marché
# url : http://www.france-ioi.org/algo/task.php?idChapter=651&idTask=0&sTab=task&iOrder=9
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

nbProduits = int(input())
nbPersonnes = int(input())

produits = [0] * nbProduits

for loop in range(nbPersonnes):
   prefere = int(input())
   produits[prefere] = produits[prefere] + 1

for prefere in range(nbProduits):
   print(produits[prefere])
