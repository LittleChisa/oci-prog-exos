##################################
# fichier 07-convertisseur-d-unites-obligatoire.py
# nom de l'exercice : Convertisseur d'unités
# url : http://www.france-ioi.org/algo/task.php?idChapter=509&idTask=0&sTab=task&iOrder=14
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

nbValeurs = int(input())

def metrePied():   
   return nombre / 0.3048

def grammeLivre():
   return nombre * 0.002205

def celsiusFarenh():
   return (nombre * 1.8) + 32

for loop in range(nbValeurs):
   entier = input().split(" ")
   nombre = float(entier[0])
   unite = entier[1]
   
   if unite == "m":
      print(metrePied(), "p")
   elif unite ==  "g":
      print(grammeLivre(), "l")
   elif unite == "c":
      print(celsiusFarenh(), "f")
