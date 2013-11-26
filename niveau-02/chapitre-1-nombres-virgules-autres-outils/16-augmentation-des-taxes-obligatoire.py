##################################
# fichier 16-augmentation-des-taxes-obligatoire.py
# nom de l'exercice : Augmentation des taxes
# url : http://www.france-ioi.org/algo/task.php?idChapter=650&idTask=0&sTab=task&iOrder=20
# type : obligatoire
#
# Chapitre : chapitre-1-nombres-virgules-autres-outils
#
# Compétence développée : 
#
# auteur : 
##################################

# chargement des modules


# mettre votre code ici

taxeActuelle = float(input())

taxeNouvelle = float(input())

prixActuel = float(input())


prixHorsTaxe = prixActuel / (1 + taxeActuelle / 100)

prixFinal = prixHorsTaxe * (1 + taxeNouvelle / 100)
prixFinaal = round(prixFinal, 2)
print(prixFinaal)
