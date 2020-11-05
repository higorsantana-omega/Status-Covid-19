from tkinter import *

root = Tk()

class Application:
    def __init__(self, master=None):
        self.root = root
        self.window()
        self.frames()
        self.labels()
        root.mainloop()

    def window(self):
        self.root.title("")
        self.root.resizable(width = FALSE, height = FALSE)
        self.root.geometry("829x360")
        self.root.configure(bg='#DCDCDC')

    def frames(self):
        self.fr_infected = Frame(self.root, width=220, height=100, bg="#ffffff", relief='flat')
        self.fr_infected.grid(row=0, column=0, sticky=NW, pady=50, padx=5)

        self.fr_recovered = Frame(self.root, width=220, height=100, bg="#ffffff", relief='flat')
        self.fr_recovered.grid(row=0, column=1, sticky=NW, pady=50, padx=5)

        self.fr_deaths = Frame(self.root, width=220, height=100, bg="#ffffff", relief='flat')
        self.fr_deaths.grid(row=0, column=2, sticky=NW, pady=50, padx=5)

        self.select_box = Frame(self.root, width=835, height=50, bg="#6A5ACD", relief='flat')
        self.select_box.grid(row=1, column=0, columnspan=3, sticky=NSEW)

    def labels(self):
        # INFECTED
        self.label_infected = Label(self.fr_infected, text='Infected', width=20, height=1,
                                    pady=7, padx=0, relief="flat", anchor=CENTER, 
                                    font='Helvetica 15 bold', bg="#ffffff", fg="#000000")
        self.label_infected.grid(row=0, column=0, pady=1, padx=13)

        self.number_infected = Label(self.fr_infected, text='32103712', width=12, height=1,
                                    pady=7, padx=0, relief="flat", anchor=CENTER, 
                                    font='Helvetica 25 bold', bg="#ffffff", fg="#000000")
        self.number_infected.grid(row=1, column=0, pady=1)

        self.info_infected = Label(self.fr_infected, text='Quarta-feira 22/11/2020', 
                                    width=33, height=1,
                                    pady=7, padx=0, relief="flat", anchor=CENTER, 
                                    font='Helvetica 9 bold', bg="#ffffff", fg="#000000")
        self.info_infected.grid(row=2, column=0, pady=1)

        self.detail_infected = Label(self.fr_infected, text='', 
                                    width=19, height=1,
                                    pady=1, padx=0, relief="flat", anchor=NW, 
                                    font='Helvetica 1 bold', bg="#FF0000", fg="#000000")
        self.detail_infected.grid(row=3, column=0, sticky=NSEW)

        # RECOVERED
        self.label_recovered = Label(self.fr_recovered, text='Recovered', width=20, height=1,
                                    pady=7, padx=0, relief="flat", anchor=CENTER, 
                                    font='Helvetica 15 bold', bg="#ffffff", fg="#000000")
        self.label_recovered.grid(row=0, column=0, pady=1, padx=13)

        self.number_recovered = Label(self.fr_recovered, text='32103712', width=12, height=1,
                                    pady=7, padx=0, relief="flat", anchor=CENTER, 
                                    font='Helvetica 25 bold', bg="#ffffff", fg="#000000")
        self.number_recovered.grid(row=1, column=0, pady=1)

        self.info_recovered = Label(self.fr_recovered, text='Quarta-feira 22/11/2020', 
                                    width=33, height=1,
                                    pady=7, padx=0, relief="flat", anchor=CENTER, 
                                    font='Helvetica 9 bold', bg="#ffffff", fg="#000000")
        self.info_recovered.grid(row=2, column=0, pady=1)

        self.detail_recovered = Label(self.fr_recovered, text='', 
                                    width=19, height=1,
                                    pady=1, padx=0, relief="flat", anchor=NW, 
                                    font='Helvetica 1 bold', bg="#FF0000", fg="#000000")
        self.detail_recovered.grid(row=3, column=0, sticky=NSEW)

        # DEATHS
        self.label_deaths = Label(self.fr_deaths, text='Deaths', width=20, height=1,
                                    pady=7, padx=0, relief="flat", anchor=CENTER, 
                                    font='Helvetica 15 bold', bg="#ffffff", fg="#000000")
        self.label_deaths.grid(row=0, column=0, pady=1, padx=13)

        self.number_deaths = Label(self.fr_deaths, text='32103712', width=12, height=1,
                                    pady=7, padx=0, relief="flat", anchor=CENTER, 
                                    font='Helvetica 25 bold', bg="#ffffff", fg="#000000")
        self.number_deaths.grid(row=1, column=0, pady=1)

        self.info_deaths = Label(self.fr_deaths, text='Quarta-feira 22/11/2020', 
                                    width=33, height=1,
                                    pady=7, padx=0, relief="flat", anchor=CENTER, 
                                    font='Helvetica 9 bold', bg="#ffffff", fg="#000000")
        self.info_deaths.grid(row=2, column=0, pady=1)

        self.detail_deaths = Label(self.fr_deaths, text='', 
                                    width=19, height=1,
                                    pady=1, padx=0, relief="flat", anchor=NW, 
                                    font='Helvetica 1 bold', bg="#FF0000", fg="#000000")
        self.detail_deaths.grid(row=3, column=0, sticky=NSEW)
Application()