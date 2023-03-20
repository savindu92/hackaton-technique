import tkinter as tk
import random

class Rectangle():
    def __init__(self, canvas, x, y, width, height):
        self.canvas = canvas
        self.rect = canvas.create_rectangle(x, y, x+width, y+height, fill="blue")
    
    def move(self):
        # calculer le nouvel emplacement aléatoire du rectangle
        new_x = random.randint(0, self.canvas.winfo_width())
        new_y = random.randint(0, self.canvas.winfo_height())
        # déplacer le rectangle vers le nouvel emplacement
        self.canvas.move(self.rect, new_x - self.canvas.coords(self.rect)[0], new_y - self.canvas.coords(self.rect)[1])
    
class App():
    def __init__(self):
        self.root = tk.Tk()
        self.canvas = tk.Canvas(self.root, width=500, height=500)
        self.canvas.pack()
        self.rect = Rectangle(self.canvas, 0, 0, 50, 50)
        self.root.after(0, self.animation)
        self.root.mainloop()
    
    def animation(self):
        self.rect.move()
        self.root.after(1000, self.animation)

if __name__ == "__main__":
    app = App()