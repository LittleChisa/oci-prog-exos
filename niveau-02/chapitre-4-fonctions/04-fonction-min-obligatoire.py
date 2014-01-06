##################################
# fichier 04-fonction-min-obligatoire.py
# nom de l'exercice : Fonction min
# url : http://www.france-ioi.org/algo/task.php?idChapter=509&idTask=0&sTab=task&iOrder=7
# type : obligatoire
#
# Chapitre : chapitre-4-fonctions
#
# Compétence développée : 
#
# auteur : 
##################################

# chargement des modules


# mettre votre code ici

def min(entier1, entier2):
   if entier1 < entier2:
        return entier1
   else:
        return entier2

liste = [0] * 10
for i in range(10):
   liste[i] = int(input())


#Pour garder le plus petit des entiers, je le stocke dans la variable "intermediaire"...;;;   
#Je mets un nombre très grand dans minimum pour que intermediaire soit de toute façon plus petit...mais...Nope. |'DDD

minimum = 2 ** 20
for i in range(10):
   intermediaire = min(liste[0], liste[i])
   if intermediaire < minimum:
      minimum = intermediaire
print(minimum)
