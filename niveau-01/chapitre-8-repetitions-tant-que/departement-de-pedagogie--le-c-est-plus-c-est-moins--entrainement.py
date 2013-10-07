##################################
# fichier departement-de-pedagogie--le-c-est-plus-c-est-moins--entrainement.py
# nom de l'exercice :  Département de pédagogie : le c'est plus, c'est moins !
# url : http://www.france-ioi.org/algo/task.php?idChapter=649&idTask=0&sTab=task&iOrder=5
# type : entrainement
#
# Nom du chapitre : 
#
# Compétence développée : 
#
# auteur : 
##################################

# chargement des modules


# mettre votre code ici

nombre = int(input())
proposition = 0
essais = 0

while nombre != proposition:
   proposition = int(input())
   if proposition > nombre:
      print("c'est moins")
   if proposition < nombre:
      print("c'est plus")
   essais = essais + 1

print("Nombre d'essais nécessaires : ")
print(essais)
