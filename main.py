from tkinter import *
from tkinter import ttk
import requests
import json
import datetime

root = Tk()

class Application:
    def __init__(self, master=None):
        self.root = root
        self.api()
        self.window()
        self.frames()
        self.labels()
        root.mainloop()

    def window(self):
        self.root.title("")
        self.root.resizable(width = FALSE, height = FALSE)
        self.root.geometry("835x270")
        self.root.configure(bg='#DCDCDC')
    
    def api(self):
        self.response = requests.get('https://covid19.mathdro.id/api')
        self.info = self.response
        self.info = json.loads(self.info.text)

        self.d_infected = self.info['confirmed']['value']
        self.d_recovered = self.info['recovered']['value']
        self.d_deaths = self.info['deaths']['value']
        self.d_update = self.info['lastUpdate']

        self.d_update = datetime.datetime.strptime(self.d_update, "%Y-%m-%dT%H:%M:%S.000Z")

    def frames(self):
        self.fr_update = Frame(self.root, width=835, height=50, bg="#ffffff", relief='flat')
        self.fr_update.grid(row=0, column=0, columnspan=3, sticky=E, pady=1)
        
        self.fr_infected = Frame(self.root, width=220, height=100, bg="#ffffff", relief='flat')
        self.fr_infected.grid(row=1, column=0, sticky=NW, pady=25, padx=15)

        self.fr_recovered = Frame(self.root, width=220, height=100, bg="#ffffff", relief='flat')
        self.fr_recovered.grid(row=1, column=1, sticky=NW, pady=25, padx=15)

        self.fr_deaths = Frame(self.root, width=220, height=100, bg="#ffffff", relief='flat')
        self.fr_deaths.grid(row=1, column=2, sticky=NW, pady=25, padx=15)

        self.select_box = Frame(self.root, width=835, height=50, bg="#DCDCDC", relief='flat')
        self.select_box.grid(row=2, column=0, columnspan=3, sticky=N)

    def labels(self):
        # UPDATE
        self.label_update = Label(self.fr_update, text="Update in: " + str(self.d_update), width=30, height=1, 
                                  pady=7, padx=0, relief="flat", anchor=CENTER,
                                  font='Helvetica 8 bold', bg="#DCDCDC", fg="#000000")
        self.label_update.grid(row=0, column=0, pady=1, padx=13)

        # INFECTED
        self.label_infected = Label(self.fr_infected, text='Infected', width=20, height=1,
                                    pady=7, padx=0, relief="flat", anchor=CENTER, 
                                    font='Helvetica 15 bold', bg="#ffffff", fg="#000000")
        self.label_infected.grid(row=0, column=0, pady=1, padx=13)

        self.number_infected = Label(self.fr_infected, text=self.d_infected, width=12, height=1,
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

        self.number_recovered = Label(self.fr_recovered, text=self.d_recovered, width=12, height=1,
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

        self.number_deaths = Label(self.fr_deaths, text=self.d_deaths, width=12, height=1,
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

        # COMBOBOX
        self.label_coutry = Label(self.select_box, text='Select Country:', width=13, height=1,
                                    pady=7, padx=0, relief="flat", anchor=NW, 
                                    font='Helvetica 12 bold', bg="#DCDCDC", fg="#000000")
        self.label_coutry.grid(row=0, column=0, pady=1, padx=0)

        self.coutry_combo = ['Brazil', 'EUA', 'Chile']

        self.select_combo = ttk.Combobox(self.select_box, width=20, font='Arial 12 bold')
        self.select_combo.grid(row=0, column=1, padx=0, pady=1)
        self.select_combo['values'] = self.coutry_combo

        self.select_combo.bind("<<ComboboxSelected>>", self.api_country())

    def api_country(self):
        self.sel_country = self.select_combo.get()
        self.response = requests.get(
            'https://covid19.mathdro.id/api/countries/{}'.format(self.sel_country))
        self.info = self.response
        self.info = json.loads(self.info.text)

        self.d_infected = self.info["confirmed"]["value"]
        self.d_recovered = self.info['recovered']['value']
        self.d_deaths = self.info['deaths']['value']
        self.d_update = self.info['lastUpdate']

        self.d_update = datetime.datetime.strptime(self.d_update, "%Y-%m-%dT%H:%M:%S.000Z")

        print(self.d_infected)

        self.number_infected.configure(text=self.d_infected)
        self.number_recovered.configure(text=self.d_recovered)
        self.number_deaths.configure(text=self.d_deaths)

Application()
