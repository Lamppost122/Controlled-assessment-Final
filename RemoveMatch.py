import json
import tkinter as tk
from tkinter import font  as tkfont
from tkinter import messagebox
from tkinter import ttk
from Gui import *
import Config
class RemoveMatch:
    def BackButtonRun(self):
        Config.PagesViewed.pop()
        self.controller.show_previous_frame(Config.PagesViewed[-1])


    def GetMatches(self):
        self.MatchList.delete(0,tk.END)

        self.teamMatches = SystemToolKit.readFile(Config.MatchFile)
        self.matches = self.teamMatches[self.txtTeam.get()]
        self.orderedList = []


        for item in self.matches:
            self.orderedList.append(item)
            text = str(self.txtTeam.get()) +" vs " +self.matches[item]["Opposition"]+" on " +self.matches[item]["Date"]
            self.MatchList.insert(tk.END,text)


    def RemoveMatch(self):
        self.matches.pop(self.orderedList[self.MatchList.index(tk.ANCHOR)], None)
        self.MatchList.delete(tk.ANCHOR)
        self.teamMatches[self.txtTeam.get() ] = self.matches
        with open(Config.MatchFile,"w+")as fp:
            json.dump(self.teamMatches,fp)

class RemoveMatchAdmin(tk.Frame,RemoveMatch):

        def __init__(self, parent, controller):
            tk.Frame.__init__(self, parent)
            self.controller = controller

            """ Widget Declearations """

            self.Title = tk.Label(self,text = "Remove Match" ,font = controller.title_font)
            self.lblTeam = tk.Label(self,text = "Team: ")
            self.txtTeam = ttk.Entry(self)
            self.getMatchesButton = tk.Button(self,text = "Get Matches",command = self.GetMatches)
            self.MatchList = tk.Listbox(self)
            b = tk.Button(self, text="Remove  Match",command=self.RemoveMatch )
            self.BackButton= tk.Button(self, text="Back",command=lambda:SystemToolKit.BackButtonRun(controller))

            """ Widget Stylings """

            self.Title.config(background="#8ABFD9",fg = "#404040",pady="5")
            self.lblTeam.config(justify="right",fg = "black",background="#8ABFD9",font=("Arial", 10, 'bold'))
            self.getMatchesButton.config(compound="left",background="#307292",relief="flat",font=("Arial", 12, 'bold'),padx=5)
            b.config(compound="left",background="#307292",relief="flat",font=("Arial", 12, 'bold'),padx=5)
            self.BackButton.config(compound="left",background="#307292",relief="flat",font=("Arial", 12, 'bold'),padx=5)

            """ Widget Positions """

            b.grid(row = 2,column = 1)
            self.Title.grid(row = 0,column = 0,columnspan = 3)
            self.lblTeam.grid(row = 1,column = 0)
            self.txtTeam.grid(row = 1,column = 1 )
            self.getMatchesButton.grid(row= 1 , column = 2)
            self.MatchList.grid(row = 2,column = 0)
            self.BackButton.grid(row =2,column = 2)

class RemoveMatchCoach(tk.Frame,RemoveMatch):

        def __init__(self, parent, controller):
            tk.Frame.__init__(self, parent)
            self.controller = controller

            """ Widget Declearations """

            self.Title = tk.Label(self,text = "Remove Match" ,font = controller.title_font)
            self.lblTeam = tk.Label(self,text = "Team: ")
            self.txtTeam = ttk.Entry(self)
            self.getMatchesButton = tk.Button(self,text = "Get Matches",command = self.GetMatches)
            self.MatchList = tk.Listbox(self)
            b = tk.Button(self, text="Remove  Match",command=self.RemoveMatch )
            self.BackButton= tk.Button(self, text="Back",command=lambda:SystemToolKit.BackButtonRun(controller))

            """ Widget Stylings """

            self.Title.config(background="#8ABFD9",fg = "#404040",pady="5")
            self.lblTeam.config(justify="right",fg = "black",background="#8ABFD9",font=("Arial", 10, 'bold'))
            self.getMatchesButton.config(compound="left",background="#307292",relief="flat",font=("Arial", 12, 'bold'),padx=5)
            b.config(compound="left",background="#307292",relief="flat",font=("Arial", 12, 'bold'),padx=5)
            self.BackButton.config(compound="left",background="#307292",relief="flat",font=("Arial", 12, 'bold'),padx=5)

            """ Widget Positions """

            b.grid(row = 2,column = 1)
            self.Title.grid(row = 0,column = 0,columnspan = 3)
            self.lblTeam.grid(row = 1,column = 0)
            self.txtTeam.grid(row = 1,column = 1 )
            self.getMatchesButton.grid(row= 1 , column = 2)
            self.MatchList.grid(row = 2,column = 0)
            self.BackButton.grid(row =2,column = 2)

class RemoveMatchPlayer(tk.Frame,RemoveMatch):

        def __init__(self, parent, controller):
            tk.Frame.__init__(self, parent)
            self.controller = controller

            """ Widget Declearations """

            """ Widget Stylings """

            """ Widget Positions """