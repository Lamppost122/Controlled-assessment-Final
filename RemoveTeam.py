import json
import tkinter as tk
from tkinter import font  as tkfont
from tkinter import messagebox
from tkinter import ttk
from Gui import *
import Config

class RemoveTeam:
    def BackButtonRun(self):
        Config.PagesViewed.pop()
        self.controller.show_previous_frame(Config.PagesViewed[-1])

    def GetTeam(self):
        self.TeamList.delete(0,tk.END)
        self.teams = SystemToolKit.readFile(Config.TeamFile)
        self.orderedList = []
        for item in self.teams:
            self.orderedList.append(item)
            text = self.teams[item]["Team Number"]
            self.TeamList.insert(tk.END,text)

    def RemoveTeam(self):
        if len(self.teams) != 0:
            del self.teams[self.orderedList[self.TeamList.index(tk.ANCHOR)]]
            self.orderedList.pop(self.TeamList.index(tk.ANCHOR))
            self.TeamList.delete(tk.ANCHOR)
            with open(Config.TeamFile,"w+")as fp:
                json.dump(self.teams,fp)

class RemoveTeamAdmin(tk.Frame,RemoveTeam):

        def __init__(self, parent, controller):
            tk.Frame.__init__(self, parent)
            self.controller = controller

            """ Widget Declearations """

            self.Title = tk.Label(self,text = "Remove Team" ,font = controller.title_font)
            self.getTeamButton = tk.Button(self,text = "Get Teams",command = self.GetTeam)
            self.TeamList = tk.Listbox(self)
            b = tk.Button(self, text="Remove Team",command=self.RemoveTeam )
            self.BackButton= tk.Button(self, text="Back",command=lambda:SystemToolKit.BackButtonRun(controller))

            """ Widget Styings """

            self.getTeamButton.config(compound="left",background="#307292",relief="flat",font=("Arial", 12, 'bold'),padx=5)
            b.config(compound="left",background="#307292",relief="flat",font=("Arial", 12, 'bold'),padx=5)
            self.BackButton.config(compound="left",background="#307292",relief="flat",font=("Arial", 12, 'bold'),padx=5)
            self.Title.config(background="#8ABFD9",fg = "#404040",pady="5")

            """ Widget Positions """

            b.grid(row = 2,column = 1)
            self.Title.grid(row = 0,column = 0,columnspan = 2)
            self.getTeamButton.grid(row= 1 , column = 0)
            self.TeamList.grid(row = 2,column = 0)
            self.BackButton.grid(row =2,column = 2)

class RemoveTeamCoach(tk.Frame,RemoveTeam):

        def __init__(self, parent, controller):
            tk.Frame.__init__(self, parent)
            self.controller = controller

            """ Widget Declearations """

            self.Title = tk.Label(self,text = "Remove Team" ,font = controller.title_font)
            self.getTeamButton = tk.Button(self,text = "Get Teams",command = self.GetTeam)
            self.TeamList = tk.Listbox(self)
            b = tk.Button(self, text="Remove Team",command=self.RemoveTeam )
            self.BackButton= tk.Button(self, text="Back",command=lambda:SystemToolKit.BackButtonRun(controller))

            """ Widget Stylings """

            self.getTeamButton.config(compound="left",background="#307292",relief="flat",font=("Arial", 12, 'bold'),padx=5)
            b.config(compound="left",background="#307292",relief="flat",font=("Arial", 12, 'bold'),padx=5)
            self.BackButton.config(compound="left",background="#307292",relief="flat",font=("Arial", 12, 'bold'),padx=5)
            self.Title.config(background="#8ABFD9",fg = "#404040",pady="5")

            """ Widget Positions """

            b.grid(row = 2,column = 1)
            self.Title.grid(row = 0,column = 0,columnspan = 2)
            self.getTeamButton.grid(row= 1 , column = 0)
            self.TeamList.grid(row = 2,column = 0)
            self.BackButton.grid(row =2,column = 2)


class RemoveTeamPlayer(tk.Frame,RemoveTeam):

        def __init__(self, parent, controller):
            tk.Frame.__init__(self, parent)
            self.controller = controller

            """ Widget Declearations """

            """ Widget Stylings """

            """ Widget Positions """