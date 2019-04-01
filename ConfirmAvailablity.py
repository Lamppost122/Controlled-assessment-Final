import json
import datetime
import tkinter as tk
from tkinter import font  as tkfont
from tkinter import messagebox
from tkinter import ttk
from Gui import *
import Config
from SystemToolKit import *
from SystemToolKit import *

class ConfirmAvailablity:
    def DisplayMyMatches(self):
        """Displays a series of match to be discided on(Yes/No) to the user """
        MyMatches = self.GetMyMatches()
        self.writeToScreen(MyMatches)



    def GetMyMatches(self):
        """returns the current players matches to be confirmed(dict)"""

        self.Players = SystemToolKit.readFile(Config.PlayerFile)
        self.team = SystemToolKit.readFile(Config.TeamFile)
        self.matches = SystemToolKit.readFile(Config.MatchFile)
        self.AvailableMatches = SystemToolKit.readFile(Config.MatchAvailablityFile)
        teamNumber = ""

        for k,i in enumerate(self.team):
            for j in self.team[i]:
                if self.team[i][j] == str(Config.CurrentUser):
                    teamNumber =self.team[i]["Team Number"]

        self.TeamID = SystemToolKit.getTeamId(teamNumber)

        MyMatches = self.AvailableMatches[self.TeamID]
        return MyMatches

    def writeToScreen(self,MyMatches):
        """Displayer a series of match on the frame"""
        try:
            for i in self.grid_slaves():
                if int(i.grid_info()["row"]) >= self.StartCount:
                    i.grid_forget()

        except AttributeError:
            pass

        for j,Data in enumerate(MyMatches):




            Text =self.matches[self.TeamID][Data]["Date"]+" at "+self.matches[self.TeamID][Data]["Time"]+" against "+ self.matches[self.TeamID][Data]["Opposition"]+"\n The Location is " + self.matches[self.TeamID][Data]["Location"]

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

            self.lblText.grid(row=j+self.StartCount,column=0)
            self.YesButton.grid(row=j+self.StartCount,column=1)
            self.NoButton.grid(row=j+self.StartCount,column=2)
            self.lblResponceStatus.grid(row=j+self.StartCount,column=3)
            self.lblResponce.grid(row=j+self.StartCount,column =4)

    def Yes(self,Data):

        """Updates the MatchAvialablity file with the players responce in the affermative"""
        self.AvailableMatches[self.TeamID][Data][Config.CurrentUser] = "Yes"
        with open(Config.MatchAvailablityFile,"w")as fp:
            json.dump(self.AvailableMatches,fp)
        self.DisplayMyMatches()

    def No(self,Data):
        """Updates the MatchAvialablity file with the players responce in the Negative"""
        self.AvailableMatches[self.TeamID][Data][Config.CurrentUser] = "No"
        with open(Config.MatchAvailablityFile,"w")as fp:
            json.dump(self.AvailableMatches,fp)
        self.DisplayMyMatches()

    def ClearMatches(self):
        """Removes matches from the Match Availablity file that have already been played"""
        self.AvailableMatches = SystemToolKit.readFile(Config.MatchAvailablityFile)
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
            """
            Initalises a frame instance of ConfirmAvailablity At Admin Access Level

            """
            tk.Frame.__init__(self, parent)
            self.controller = controller
            self.StartCount = 3

            """ Widget Declearations """

            self.Title =tk.Label(self,text="Confirm Availablity",font=controller.title_font)
            self.GetMyMatchesButton = tk.Button(self,text="Get My Matches",command = lambda:self.DisplayMyMatches())
            self.BackButton = tk.Button(self,text="Back",command=lambda:SystemToolKit.BackButtonRun(controller))

            """ Widget Stylings """

            self.BackButton.config(compound="left",background="#307292",relief="flat",font=("Arial", 10, 'bold'),padx=5)
            self.GetMyMatchesButton.config(compound="left",background="#307292",relief="flat",font=("Arial", 10, 'bold'),padx=5)
            self.Title.config(background="#8ABFD9",fg = "#404040",pady="5")

            """ Widget Positions """

            self.Title.grid(row=0,column =0)
            self.GetMyMatchesButton.grid(row=1,column=0)
            self.BackButton.grid(row=1,column=1)

            self.ClearMatches()

class ConfirmAvailablityPlayer(tk.Frame,ConfirmAvailablity):

        def __init__(self, parent, controller):
            """
            Initalises a frame instance of ConfirmAvailablity At Player Access Level

            """
            tk.Frame.__init__(self, parent)
            self.controller = controller
            self.StartCount = 3

            """ Widget Declearations """

            self.Title =tk.Label(self,text="Confirm Availablity",font=controller.title_font)
            self.GetMyMatchesButton = tk.Button(self,text="Get My Matches",command = lambda:self.DisplayMyMatches())
            self.BackButton = tk.Button(self,text="Back",command=lambda:SystemToolKit.BackButtonRun(controller))

            """ Widget Stylings """

            self.BackButton.config(compound="left",background="#307292",relief="flat",font=("Arial", 10, 'bold'),padx=5)
            self.GetMyMatchesButton.config(compound="left",background="#307292",relief="flat",font=("Arial", 10, 'bold'),padx=5)
            self.Title.config(background="#8ABFD9",fg = "#404040",pady="5")

            """ Widget Positions """

            self.Title.grid(row=0,column =0)
            self.GetMyMatchesButton.grid(row=1,column=0)
            self.BackButton.grid(row=1,column=1)

            self.ClearMatches()

class ConfirmAvailablityCoach(tk.Frame,ConfirmAvailablity):

        def __init__(self, parent, controller):
            """
            Initalises a frame instance of ConfirmAvailablity At Coach Access Level

            """
            tk.Frame.__init__(self, parent)
            self.controller = controller
            self.StartCount = 3

            """ Widget Declearations """

            self.Title =tk.Label(self,text="Confirm Availablity",font=controller.title_font)
            self.GetMyMatchesButton = tk.Button(self,text="Get My Matches",command = lambda:self.DisplayMyMatches())
            self.BackButton = tk.Button(self,text="Back",command=lambda:SystemToolKit.BackButtonRun(controller))

            """ Widget Stylings """

            self.BackButton.config(compound="left",background="#307292",relief="flat",font=("Arial", 10, 'bold'),padx=5)
            self.GetMyMatchesButton.config(compound="left",background="#307292",relief="flat",font=("Arial", 10, 'bold'),padx=5)
            self.Title.config(background="#8ABFD9",fg = "#404040",pady="5")

            """ Widget Positions """

            self.Title.grid(row=0,column =0)
            self.GetMyMatchesButton.grid(row=1,column=0)
            self.BackButton.grid(row=1,column=1)

            self.ClearMatches()
