import tkinter as tk

window = tk.Tk()

label = tk.Label(
    text="Hello, Tkinter",
    foreground="white",  
    background="green",
    width=50,
    height=25
)
label.pack()

window.mainloop()