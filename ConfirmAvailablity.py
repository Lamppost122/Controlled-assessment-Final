import json
import datetime
import tkinter as tk
from tkinter import font  as tkfont
from tkinter import messagebox
from tkinter import ttk
from Gui import *
import Config
from AddMatch import *
from SystemToolKit import *

class ConfirmAvailablity:

    def BackButtonRun(self):
            Config.PagesViewed.pop()
            self.controller.show_previous_frame(Config.PagesViewed[-1])

    def GetMyMatches(self):

        Players = SystemToolKit.readFile(Config.PlayerFile)
        team = SystemToolKit.readFile(Config.TeamFile)
        matches = SystemToolKit.readFile(Config.MatchFile)
        teamNumber = ""

        for k,i in enumerate(team):
            for j in team[i]:
                if team[i][j] == str(Config.CurrentUser):
                    teamNumber =team[i]["Team Number"]

        self.TeamID = AddMatch.getTeamId(teamNumber)
        MyMatches = self.AvailableMatches[self.TeamID]

        for j,Data in enumerate(MyMatches):

            Text =matches[self.TeamID][Data]["Date"]+" at "+matches[self.TeamID][Data]["Time"]+" against "+ matches[self.TeamID][Data]["Opposition"]+"\n The Location is " + matches[self.TeamID][Data]["Location"]

            """ Widget Declearations """

            self.lblText=tk.Label(self,text=Text)
            self.lblResponceStatus =tk.Label(self,text = "Responce Status")
            self.lblResponce =tk.Label(self,text=self.AvailableMatches[self.TeamID][Data][Config.CurrentUser])
            self.YesButton=tk.Button(self,text="Yes",command = lambda Data =Data:self.Yes(Data))
            self.NoButton = tk.Button(self,text="No",command = lambda Data =Data:self.No(Data))

            """ Widget Stylings """

            self.lblText.config(justify="right",fg = "black",background="#8ABFD9",font=("Arial", 10, 'bold'))
            self.lblResponceStatus.config(justify="right",fg = "black",background="#8ABFD9",font=("Arial", 10, 'bold'))
            self.lblResponce.config(justify="right",fg = "black",background="#8ABFD9",font=("Arial", 10, 'bold'))
            self.YesButton.config(compound="left",background="#307292",relief="flat",font=("Arial", 10, 'bold'),padx=5)
            self.NoButton.config(compound="left",background="#307292",relief="flat",font=("Arial", 10, 'bold'),padx=5)
            self.BackButton.config(compound="left",background="#307292",relief="flat",font=("Arial", 10, 'bold'),padx=5)
            self.GetMyMatchesButton.config(compound="left",background="#307292",relief="flat",font=("Arial", 10, 'bold'),padx=5)
            self.Title.config(background="#8ABFD9",fg = "#404040",pady="5")

            """ Widget Positions """

            self.lblText.grid(row=j+3,column=0)
            self.YesButton.grid(row=j+3,column=1)
            self.NoButton.grid(row=j+3,column=2)
            self.lblResponceStatus.grid(row=j+3,column=3)
            self.lblResponce.grid(row=j+3,column =4)

    def Yes(self,Data):
        self.AvailableMatches[self.TeamID][Data][Config.CurrentUser] = "Yes"
        with open(Config.MatchAvailablityFile,"w")as fp:
            json.dump(self.AvailableMatches,fp)
        self.GetMyMatches()

    def No(self,Data):
        self.AvailableMatches[self.TeamID][Data][Config.CurrentUser] = "No"
        with open(Config.MatchAvailablityFile,"w")as fp:
            json.dump(self.AvailableMatches,fp)
        self.GetMyMatches()

    def ClearMatches(self):
        present = datetime.datetime.now()
        NewDict = self.AvailableMatches
        for i in list(self.AvailableMatches):
            for j in list(self.AvailableMatches[i]):
                for k in self.AvailableMatches[i][j]:
                    if k =="Date":
                        if datetime.datetime.strptime(self.AvailableMatches[i][j][k], "%d/%m/%Y") < present:
                            del NewDict[i][j]

        with open(Config.MatchAvailablityFile,"w")as fp:
            json.dump(NewDict,fp)

class ConfirmAvailablityAdmin(tk.Frame,ConfirmAvailablity):

        def __init__(self, parent, controller):
            tk.Frame.__init__(self, parent)
            self.controller = controller

            """ Widget Declearations """

            self.Title =tk.Label(self,text="Confirm Availablity",font=controller.title_font)
            self.GetMyMatchesButton = tk.Button(self,text="Get My Matches",command = lambda:self.GetMyMatches())
            self.BackButton = tk.Button(self,text="Back",command=lambda:self.BackButtonRun())

            """ Widget Stylings """

            self.BackButton.config(compound="left",background="#307292",relief="flat",font=("Arial", 10, 'bold'),padx=5)
            self.GetMyMatchesButton.config(compound="left",background="#307292",relief="flat",font=("Arial", 10, 'bold'),padx=5)
            self.Title.config(background="#8ABFD9",fg = "#404040",pady="5")

            """ Widget Positions """

            self.Title.grid(row=0,column =0)
            self.GetMyMatchesButton.grid(row=1,column=0)
            self.BackButton.grid(row=1,column=1)
            self.AvailableMatches = SystemToolKit.readFile(Config.MatchAvailablityFile)
            self.ClearMatches()

class ConfirmAvailablityPlayer(tk.Frame,ConfirmAvailablity):

        def __init__(self, parent, controller):
            tk.Frame.__init__(self, parent)
            self.controller = controller

            """ Widget Declearations """

            self.Title =tk.Label(self,text="Confirm Availablity",font=controller.title_font)
            self.GetMyMatchesButton = tk.Button(self,text="Get My Matches",command = lambda:self.GetMyMatches())
            self.BackButton = tk.Button(self,text="Back",command=lambda:self.BackButtonRun())

            """ Widget Stylings """

            self.BackButton.config(compound="left",background="#307292",relief="flat",font=("Arial", 10, 'bold'),padx=5)
            self.GetMyMatchesButton.config(compound="left",background="#307292",relief="flat",font=("Arial", 10, 'bold'),padx=5)
            self.Title.config(background="#8ABFD9",fg = "#404040",pady="5")

            """ Widget Positions """

            self.Title.grid(row=0,column =0)
            self.GetMyMatchesButton.grid(row=1,column=0)
            self.BackButton.grid(row=1,column=1)
            self.AvailableMatches = SystemToolKit.readFile(Config.MatchAvailablityFile)
            self.ClearMatches()

class ConfirmAvailablityCoach(tk.Frame,ConfirmAvailablity):

        def __init__(self, parent, controller):
            tk.Frame.__init__(self, parent)
            self.controller = controller

            """ Widget Declearations """

            self.Title =tk.Label(self,text="Confirm Availablity",font=controller.title_font)
            self.GetMyMatchesButton = tk.Button(self,text="Get My Matches",command = lambda:self.GetMyMatches())
            self.BackButton = tk.Button(self,text="Back",command=lambda:self.BackButtonRun())

            """ Widget Stylings """

            self.BackButton.config(compound="left",background="#307292",relief="flat",font=("Arial", 10, 'bold'),padx=5)
            self.GetMyMatchesButton.config(compound="left",background="#307292",relief="flat",font=("Arial", 10, 'bold'),padx=5)
            self.Title.config(background="#8ABFD9",fg = "#404040",pady="5")

            """ Widget Positions """

            self.Title.grid(row=0,column =0)
            self.GetMyMatchesButton.grid(row=1,column=0)
            self.BackButton.grid(row=1,column=1)
            self.AvailableMatches = SystemToolKit.readFile(Config.MatchAvailablityFile)
            self.ClearMatches()



