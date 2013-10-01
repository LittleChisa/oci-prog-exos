##################################
# fichier maison-de-l-espion-entrainement.py
# nom de l'exercice :  Maison de l'espion
# url : http://www.france-ioi.org/algo/task.php?idChapter=648&idTask=0&sTab=task&iOrder=2
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

Xmin = int(input())
Xmax = int(input())
Ymin = int(input())
Ymax = int(input())

totalMaisons = int(input())
nbMaisons = 0

for loop in range(totalMaisons):
    x = int(input())
    y = int(input())

    if (x >= Xmin) and (x <= Xmax)and (y >= Ymin) and (y <= Ymax):
        nbMaisons = nbMaisons + 1

print(nbMaisons)
