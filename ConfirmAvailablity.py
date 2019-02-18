import json
import datetime
import tkinter as tk
from tkinter import font  as tkfont
from tkinter import messagebox
from tkinter import ttk
from Gui import *
from Config import *
from AddMatch import *
from SystemToolKit import *

class ConfirmAvailablity(tk.Frame):

        def __init__(self, parent, controller):
            tk.Frame.__init__(self, parent)
            self.controller = controller
            self.Title =tk.Label(self,text="Confirm Availablity",font=controller.title_font)
            self.GetMyMatchesButton = tk.Button(self,text="Get My Matches",command = lambda:self.GetMyMatches())
            self.BackButton = tk.Button(self,text="Back",command=lambda:self.BackButtonRun())
            self.Title.grid(row=0,column =0)
            self.GetMyMatchesButton.grid(row=1,column=0)
            self.BackButton.grid(row=1,column=1)
            self.AvailableMatches = SystemToolKit.readFile("matchAvailablity.json")
            self.ClearMatches()

        def BackButtonRun(self):
            global PagesViewed
            PagesViewed.pop()
            self.controller.show_frame(PagesViewed[-1])

        def GetMyMatches(self):
            Players = SystemToolKit.readFile("players.json")
            team = SystemToolKit.readFile("team.json")
            matches = SystemToolKit.readFile("matches.json")
            teamNumber = ""
            for k,i in enumerate(team):
                for j in team[i]:
                    if team[i][j] == str(Config.CurrentUser):
                        teamNumber =team[i]["Team Number"]

            self.TeamID = AddMatch.getTeamId(teamNumber)




            MyMatches = self.AvailableMatches[self.TeamID]

            for j,Data in enumerate(MyMatches):

                Text =matches[self.TeamID][Data]["Date"]+" at "+matches[self.TeamID][Data]["Time"]+" against "+ matches[self.TeamID][Data]["Opposition"]+"\n The Location is " + matches[self.TeamID][Data]["Location"]
                self.lblText=tk.Label(self,text=Text)
                self.lblResponceStatus =tk.Label(self,text = "Responce Status")
                self.lblResponce =tk.Label(self,text=self.AvailableMatches[self.TeamID][Data][Config.CurrentUser])
                self.YesButton=tk.Button(self,text="Yes",command = lambda Data =Data:self.Yes(Data))
                self.NoButton = tk.Button(self,text="No",command = lambda Data =Data:self.No(Data))
                self.lblText.grid(row=j+3,column=0)
                self.YesButton.grid(row=j+3,column=1)
                self.NoButton.grid(row=j+3,column=2)
                self.lblResponceStatus.grid(row=j+3,column=3)
                self.lblResponce.grid(row=j+3,column =4)
        def Yes(self,Data):
            self.AvailableMatches[self.TeamID][Data][Config.CurrentUser] = "Yes"
            with open("matchAvailablity.json","w")as fp:

                json.dump(self.AvailableMatches,fp)
            self.GetMyMatches()
        def No(self,Data):
            self.AvailableMatches[self.TeamID][Data][Config.CurrentUser] = "No"
            with open("matchAvailablity.json","w")as fp:

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
            with open("matchAvailablity.json","w")as fp:

                json.dump(NewDict,fp)






