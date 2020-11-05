from tkinter import *

root = Tk()

class Application:
    def __init__(self, master=None):
        self.root = root
        self.window()
        self.frames()
        root.mainloop()

    def window(self):
        self.root.title("")
        self.root.resizable(width = FALSE, height = FALSE)
        self.root.geometry("835x360")
        self.root.configure(bg='#DCDCDC')

    def frames(self):
        self.fr_infected = Frame(self.root, width=220, height=100, bg="#6A5ACD", relief='flat')
        self.fr_infected.grid(row=0, column=0, sticky=NW, pady=50, padx=20)

        self.fr_recovered = Frame(self.root, width=220, height=100, bg="#6A5ACD", relief='flat')
        self.fr_recovered.grid(row=0, column=1, sticky=NW, pady=50, padx=20)

        self.fr_deaths = Frame(self.root, width=220, height=100, bg="#6A5ACD", relief='flat')
        self.fr_deaths.grid(row=0, column=2, sticky=NW, pady=50, padx=20)

        self.select_box = Frame(self.root, width=835, height=50, bg="#6A5ACD", relief='flat')
        self.select_box.grid(row=1, column=0, columnspan=3, sticky=NSEW)

Application()