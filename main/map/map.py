import tkinter as tk
from tkinter import*

window = tk.Tk()

#Fenetre d'options
fenetre = tk.Frame()
#Interface de jeu
interface = tk.Frame()

button = tk.Button(
    master=fenetre,
    text="Infos map"
)

button.pack()

ArrierePlan = tk.Canvas( 
    master=interface,
    background="green", #gris par défaut : #333333
    width=700,
    height=500
)
ArrierePlan.pack()

Background_import = tk.PhotoImage(file="main/map/assets/grass_background.png")
Background = ArrierePlan.create_image(0,0, anchor=NW, image=Background_import)

Routes_import = tk.PhotoImage(file="main/map/assets/routes.png")
Routes = ArrierePlan.create_image(0,0, anchor=NW, image=Routes_import)

Entrepots_import = tk.PhotoImage(file="main/map/assets/entrepots.png")
Entrepots = ArrierePlan.create_image(0,0, anchor=NW, image=Entrepots_import)

Magasins_import = tk.PhotoImage(file="main/map/assets/magasins.png")
Magasins = ArrierePlan.create_image(0,0, anchor=NW, image=Magasins_import)

Recharge_import = tk.PhotoImage(file="main/map/assets/stations_de_recharge.png")
Recharge = ArrierePlan.create_image(0,0, anchor=NW, image=Recharge_import)

Stockage_import = tk.PhotoImage(file="main/map/assets/stockage.png")
Stockage = ArrierePlan.create_image(0,0, anchor=NW, image=Stockage_import)

Decor_import = tk.PhotoImage(file="main/map/assets/decor.png")
Decor = ArrierePlan.create_image(0,0, anchor=NW, image=Decor_import)


fenetre.pack()
interface.pack()
window.mainloop()