##################################
# fichier bonus--casernes-de-pompiers-validation.py
# nom de l'exercice :  Bonus : Casernes de pompiers
# url : http://www.france-ioi.org/algo/task.php?idChapter=648&idTask=0&sTab=task&iOrder=7
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


nbPaires = int(input())

for loop in range(nbPaires):
    xMin1 = int(input())
    xMax1 = int(input())
    yMin1 = int(input())
    yMax1 = int(input())

    xMin2 = int(input())
    xMax2 = int(input())
    yMin2 = int(input())
    yMax2 = int(input())

    if xMax1 <= xMin2:
       print("NON")
    else:
       if xMin1 >= xMax2:
          print("NON")
       else:   
          if yMax1 <= yMin2:
             print("NON")
          else:
             if yMin1 >= yMax2:
                print("NON")
             else:
                print("OUI")
