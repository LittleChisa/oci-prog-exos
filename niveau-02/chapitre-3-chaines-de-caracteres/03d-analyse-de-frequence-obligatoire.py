##################################
# fichier 03d-analyse-de-frequence-obligatoire.py
# nom de l'exercice : Analyse de fréquence
# url : http://www.france-ioi.org/algo/task.php?idChapter=595&idTask=0&sTab=task&iOrder=16
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

nb = input(). split(" ")
nbLignes = nb[0]
nbMots = nb[1]
tableau = [0] * 101

for loop in range(int(nbLignes)):
   texte = input().split(" ")
   
   for i in range(int(nbMots)):
      texte[i] = len(texte[i]) 
      tableau[texte[i]] += 1
      
for i in range(101):
   if tableau[i] > 0:
      print(i, " : ", tableau[i])
