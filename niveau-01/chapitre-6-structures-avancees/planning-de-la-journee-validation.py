##################################
# fichier planning-de-la-journee-validation.py
# nom de l'exercice :  Planning de la journée
# url : http://www.france-ioi.org/algo/task.php?idChapter=647&idTask=0&sTab=task&iOrder=2
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

positionActuelle = int(input())
nbVillages = int(input())

distance = 0
final = 0

for loop in range(nbVillages):
    positionVillage = int(input())

    if positionVillage >= positionActuelle:
        distance = positionVillage - positionActuelle

    if positionActuelle >= positionVillage:
        distance = positionActuelle - positionVillage

    if distance <= 50:
        final = final + 1
   
print(final)
