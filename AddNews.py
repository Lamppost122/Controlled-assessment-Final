import json
import tkinter as tk
from tkinter import font  as tkfont
from tkinter import messagebox
from tkinter import ttk
from Gui import *
from SystemToolKit import *
import Config
from Validation import *

class AddNews:

    def BackButtonRun(self):
            Config.PagesViewed.pop()
            self.controller.show_previous_frame(Config.PagesViewed[-1])


    def AddUpdate(self):
        if Validation.PresentsCheck( self.txtAddUpdate.get("1.0",'end-1c')) == True:
            updates = SystemToolKit.readFile(Config.UpdatesFile)
            index = 0
            for i,j in enumerate(list(((updates).keys()))):
                if index <= int(j):
                    index =int(j) + 1
            updates[index] = {"Data":self.txtAddUpdate.get("1.0",'end-1c'),"Date":str(datetime.date.today())}
            with open(Config.UpdatesFile,"w") as fp:
                    json.dump(updates,fp)
            self.controller.show_frame("Home")


class AddNewsAdmin(tk.Frame,AddNews):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller

        """ Widget Declearations """

        self.addUpdateButton =tk.Button(self,text = "Add update",command = self.AddUpdate)
        self.lblAddUpdate = tk.Label(self,text = "Enter News/Update bellow",font=controller.title_font)
        self.txtAddUpdate =tk.Text(self,width="50",height = "10")
        self.BackButton= tk.Button(self, text="Back",command=lambda:self.BackButtonRun())

        """ Widget Stylings """

        self.lblAddUpdate.config(background="#8ABFD9",fg = "#404040",pady="5")
        self.txtAddUpdate.config(background="white",padx="10")
        self.BackButton.config(compound="left",background="#307292",relief="flat",font=("Arial", 12, 'bold'),padx=5)
        self.addUpdateButton.config(compound="left",background="#307292",relief="flat",font=("Arial", 12, 'bold'),padx=5)

        """ Widget Positons """

        self.lblAddUpdate.grid(row = 0,column =0 )
        self.txtAddUpdate.grid(row = 1,column = 0)
        self.addUpdateButton.grid(row=1,column =1)
        self.BackButton.grid(row =1,column = 2)

class AddNewsPlayer(tk.Frame,AddNews):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller

        """ Widget Declearations """

        """ Widget Stlyings """

        """ Widget Positions """


class AddNewsCoach(tk.Frame,AddNews):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller

        """ Widget Declearations """

        """ Widget Stlyings """

        """ Widget Positions """