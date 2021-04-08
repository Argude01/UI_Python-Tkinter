from tkinter import *
from tkinter import ttk

window = Tk()
f_app = Frame(window, width=400, height=800, bg="red")
f_app.pack()

# Widgets dentro del contender APP
f_navbar = Frame(f_app, width=400, height=100, bg="yellow")
f_navbar.grid(row=0, column=0)
f_title = Frame(f_app, width=400, height=100, bg="yellow")
f_title.grid(row=1, column=0)
f_options = Frame(f_app, width=400, height=400, bg="yellow")
f_options.grid(row=2, column=0)

# Widgets dentro del contender OPTIONS
f_food = Frame(f_options, width=400, height=200, bg="#d48df0")
f_food.grid(row=0, column=0)
f_drinks = Frame(f_options, width=400, height=200, bg="#d48df0")
f_drinks.grid(row=1, column=0)

# title = Label(f_app, text="Casa")
# title.grid(row=0, column=3)
# title = Label(f_app, text="Hola, Nicolas")
# title.grid(row=2, column=0)
# title = Label(f_app, text="¿Qué Necesitas?")
# title.grid(row=3, column=0)


window.mainloop()