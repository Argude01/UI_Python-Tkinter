from tkinter import *
from tkinter import ttk

window = Tk()
f_home = Frame(window, width=400, height=800, bg="#d5d8de")
f_home.pack()

title = Label(f_home, text="Casa")
title.grid(row=0, column=3)
title = Label(f_home, text="Hola, Nicolas")
title.grid(row=2, column=0)
title = Label(f_home, text="¿Qué Necesitas?")
title.grid(row=3, column=0)

f_item = Frame(f_home, width=300, height=300, bg="#6a93e6")
f_item.grid(row=5, column=1)

window.mainloop()