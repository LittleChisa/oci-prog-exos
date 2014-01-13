##################################
# fichier 04f-ngms-sns-vlls-obligatoire.py
# nom de l'exercice : ngms sns vlls
# url : http://www.france-ioi.org/algo/task.php?idChapter=595&idTask=0&sTab=task&iOrder=23
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

titre = input().split(" ")
auteur = input().split(" ")

def sansVoyelle():
   lettre = 0
   for loop in range(len(liste)):
      if liste[lettre] != "A" and liste[lettre] != "E" and liste[lettre] != "I" and liste[lettre] != "O" and liste[lettre] != "U" and liste[lettre] != "Y":
         print(liste[lettre], end = "")
      lettre += 1
   lettre = 0

for i in range(len(titre)):
   liste = list(titre[i])
   sansVoyelle()

print("")

for i in range(len(auteur)):
   liste = list(auteur[i])
   sansVoyelle()
