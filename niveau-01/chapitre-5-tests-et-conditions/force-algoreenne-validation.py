##################################
# fichier force-algoreenne-validation.py
# nom de l'exercice :  Force algoréenne
# url : http://www.france-ioi.org/algo/task.php?idChapter=646&idTask=0&sTab=task&iOrder=1
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

nbPersonnes = int(input())

totalEquipe1 = 0
totalEquipe2 = 0

for loop in range(nbPersonnes):
   poidsEquipe1 = int(input())
   totalEquipe1 = totalEquipe1 + poidsEquipe1
   poidsEquipe2 = int(input())
   totalEquipe2 = totalEquipe2 + poidsEquipe2
   
if totalEquipe1 > totalEquipe2:
    print("L'équipe 1 a un avantage")
else:
    print("L'équipe 2 a un avantage")

print("Poids total pour l'équipe 1 : ", end = "")
print(totalEquipe1)
print("Poids total pour l'équipe 2 : ", end = "")
print(totalEquipe2)
