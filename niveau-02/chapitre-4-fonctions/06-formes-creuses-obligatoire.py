##################################
# fichier 06-formes-creuses-obligatoire.py
# nom de l'exercice : Formes creuses
# url : http://www.france-ioi.org/algo/task.php?idChapter=509&idTask=0&sTab=task&iOrder=13
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

nbX = int(input())
nbLignesR = int(input())
nbColonnesR = int(input())
nbLignesT = int(input())

def sauterLigne():
   print("")

def afficherLignesavecTrous(nbLignes, signe, trou):
   trouT = 0
   for loop in range(nbLignes - 2):
      print(signe, end="")
      
      if signe == "#":
         print(" " * trou, end="")
         if nbColonnesR > 1:
            print(signe)
         else:
            print("")

      else:
         print(" " * trouT, end="")
         print(signe)
         trouT += 1
      


print("X" * nbX, end="")
print("")

sauterLigne()

print("#" * nbColonnesR)
afficherLignesavecTrous(nbLignesR, "#", nbColonnesR - 2)
print("#" * nbColonnesR)

sauterLigne()

print("@")
trouT = 0
afficherLignesavecTrous(nbLignesT, "@", trouT)
print("@" * nbLignesT)
