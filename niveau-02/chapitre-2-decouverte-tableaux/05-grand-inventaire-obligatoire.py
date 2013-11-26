##################################
# fichier 05-grand-inventaire-obligatoire.py
# nom de l'exercice : Grand inventaire
# url : http://www.france-ioi.org/algo/task.php?idChapter=651&idTask=0&sTab=task&iOrder=7
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

produits = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

nbOperations = int(input())

for loop in range(nbOperations):
   numeroIngredient = int(input())
   quantite = int(input())
   numeroIngredient = numeroIngredient - 1
   produits[numeroIngredient] = produits[numeroIngredient] + quantite
   
idProduit = 0
for loop in range(10):
   print(produits[idProduit])
   idProduit = idProduit + 1
