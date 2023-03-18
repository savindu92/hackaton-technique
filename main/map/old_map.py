'''import tkinter as tk
from tkinter import*

#---------------------------------------------Partie fonctions-----------------------------------------------------------------

def mirror_x(x):
    Fonction "mirroir" qui sert à séparer la map en 2 parties symétriques égales.
    mirroir=1400-x
    return mirroir

def mirror_y(y):
    Fonction "mirroir" qui sert à séparer la map en 2 parties symétriques égales.
    mirroir=700-y
    return mirroir

#--------------------------------------------Partie génération du terrain-------------------------------------------------------

#Base de l'équipe rouge
Canvas.create_rectangle(0, 175, 100, 525, fill='red')

#Base de l'équipe bleue
Canvas.create_rectangle(mirror_x(0), mirror_y(175), mirror_x(100), mirror_y(525), fill='blue')

#Création des 3 routes horizontales
Canvas.create_rectangle(100, 175, mirror_x(100), 225, fill='grey')
Canvas.create_rectangle(100, mirror_y(175), mirror_x(100), mirror_y(225), fill='grey')
Canvas.create_rectangle(100, 325, mirror_x(100), 375, fill='grey')

#Création des 3 routes verticales
Canvas.create_rectangle(100, 0, 150, mirror_y(0), fill='grey')
Canvas.create_rectangle(100, mirror_y(175), mirror_x(100), mirror_y(225), fill='grey')
Canvas.create_rectangle(100, 325, mirror_x(100), 375, fill='grey')'''