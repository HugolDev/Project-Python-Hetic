"""
#1 - Ecrire un programme ayant une variable C, donner une valeur à C, calculer et afficher son carré

C = int(input()) # On crée une variable C qui prend des nombres entiers que l'utilisateur Tape
resultat = C*C # On crée Une variable résultat,puis on calcul 
print(resultat) # Puis, il affiche le résultat de l'utilisateur


# Explication du code 
# C (Variable)
# = (égal)
# int (un monbre entier)
# input (Entrée)
# resultat (Variable)
# C*C (Variable plus mutliplication)
# print (aficher)

Donc on vient de crée une variable qui permet de calculer son carré
# 2 - Ecrire un programme ayant deux variables A et B, donner des valeurs à A et B puis tenter de trouver un moyen d'intervertir les deux valeurs stockées dans A et B

A = 4 # On crée une variable A puis-on ajoute 4
B = 3 # On crée Une Varaible B puis-on ajoute 3

print(A) # Puis on affiche A
print(B) # Puis on Affiche B

inverse = A # On crée deux variable puis on inverse 4 qui devient 3
A = B # On dit A = B
B = inverse # On crée deux variable puis on inverse 3 qui devient 4

print(A) #Puis on affiche 
print(B) #Puis on affiche


"""

"""
# 3 - Ecrire un programme ayant une variable R correspondant au rayon d'un cercle, donner une valeur à R et calculer le périmètre du cercle de rayon R

import math #  Module time 

radius = float(input()) # Attributs d'intance puis stocker des nombre à virgule flottante puis demande au utilisateur d'entrée numéro
perimeter = 2 * math.pi * radius #  La fonction perimeter pour calculer périmètre fois deux puis 
print(perimeter) # On affiche le périmètre
"""

"""
# 4 - Ecrire un programme ayant 4 variables correspondant à 4 notes, donner des valeurs aux variables et écrire un algorithme permettant de calculer la moyenne de ces 4 notes

note1 = float(input()) # Affectation de la variable en demande à l'utilisateur des monbres flottant (un point virgule)
note2 = float(input()) # Affectation de la variable en demande à l'utilisateur des monbres flottant (un point virgule)
note3 = float(input()) # Affectation de la variable en demande à l'utilisateur des monbres flottant (un point virgule)
note4 = float(input()) # Affectation de la variable en demande à l'utilisateur des monbres flottant (un point virgule)

Campue = ( note1 + note2 + note3 + note4 ) /4 # affectation de la variable puis donne le calcul

print(Campue) # On affiche toutes les notes

"""
"""
#5 - Ecrire un programme ayant une variable S contenant des secondes. Afficher le nombre d'heures et de minutes correspondants.

S = 1000
H = S//3600
M = (S%3600)//60
S = S%60

print(H,"h",M,"min",S,"sec")
"""
