##################################
# fichier departement-de-chimie--melange-explosif-validation.py
# nom de l'exercice :  Département de chimie : mélange explosif
# url : http://www.france-ioi.org/algo/task.php?idChapter=649&idTask=0&sTab=task&iOrder=7
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

# ...J'aurais dû utiliser while...-u-;;

mesuresTotales = int(input())
temperatureMin = int(input())
temperatureMax = int(input())


pasDanger = True
for loop in range(mesuresTotales):
   temperature = int(input())

   if pasDanger:
      if temperature >= temperatureMin and temperature <= temperatureMax:
         print("Rien à signaler")
    
      else:
         print("Alerte !!")
         pasDanger = False
