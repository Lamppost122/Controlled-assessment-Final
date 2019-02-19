import json
import tkinter as tk
from tkinter import font  as tkfont
from tkinter import messagebox
from tkinter import ttk
from Gui import *
from Config import *
from AddMatch import *
from SystemToolKit import *

class ViewAvailablity:

        def BackButtonRun(self):
            global PagesViewed
            PagesViewed.pop()
            self.controller.show_frame(PagesViewed[-1])

        def GetPlayers(self):
            matchPlayers = SystemToolKit.readFile("matchAvailablity.json")
            players = SystemToolKit.readFile("players.json")
            match =SystemToolKit.readFile("matches.json")


            TeamID = AddMatch.getTeamId(self.txtTeamNumber.get())
            matches = matchPlayers[TeamID]
            count = 0
            for Data in matches:
                MatchText =match[TeamID][Data]["Date"]+" at "+match[TeamID][Data]["Time"]+" against "+ match[TeamID][Data]["Opposition"]+"\n The Location is " + match[TeamID][Data]["Location"]
                self.lblMatchTitle = tk.Label(self,text="Match: ")
                self.lblMatchData= tk.Label(self,text=MatchText)
                self.lblMatchData.grid(row=count+2,column=1)
                self.lblMatchTitle.grid(row=count+2,column=0)
                count+=1

                for j,i in enumerate(matches[Data]):
                    if i != "Date":
                        playerText = players[i]["First name"]+" "+players[i]["Last name"] +": "+ matches[Data][i]

                        self.lblPlayer =tk.Label(self,text =playerText)
                        self.lblPlayer.grid(row=count+2,column = 0)
                        count+=1

class ViewAvailablityAdmin(tk.Frame,ViewAvailablity):

        def __init__(self, parent, controller):
            tk.Frame.__init__(self, parent)
            self.controller = controller
            self.Title=tk.Label(self,text="Player Availablity",font=controller.title_font)
            self.lblTeamNumber = tk.Label(self,text="Team Number: ")
            self.txtTeamNumber = tk.Entry(self)
            self.GetPlayersButton =tk.Button(self,text="Get Player Status",command=lambda:self.GetPlayers())
            self.BackButton= tk.Button(self, text="Back",command=lambda:self.BackButtonRun())
            self.Title.grid(row=0,column =0)
            self.lblTeamNumber.grid(row=1,column=0)
            self.txtTeamNumber.grid(row=1,column =1)
            self.GetPlayersButton.grid(row=1,column =2)
            self.BackButton.grid(row=1,column=3)

class ViewAvailablityCoach(tk.Frame,ViewAvailablity):

        def __init__(self, parent, controller):
            tk.Frame.__init__(self, parent)
            self.controller = controller
            self.Title=tk.Label(self,text="Player Availablity",font=controller.title_font)
            self.lblTeamNumber = tk.Label(self,text="Team Number: ")
            self.txtTeamNumber = tk.Entry(self)
            self.GetPlayersButton =tk.Button(self,text="Get Player Status",command=lambda:self.GetPlayers())
            self.BackButton= tk.Button(self, text="Back",command=lambda:self.BackButtonRun())
            self.Title.grid(row=0,column =0)
            self.lblTeamNumber.grid(row=1,column=0)
            self.txtTeamNumber.grid(row=1,column =1)
            self.GetPlayersButton.grid(row=1,column =2)
            self.BackButton.grid(row=1,column=3)

class ViewAvailablityPlayer(tk.Frame,ViewAvailablity):

        def __init__(self, parent, controller):
            tk.Frame.__init__(self, parent)
            self.controller = controller
            self.Title=tk.Label(self,text="Player Availablity",font=controller.title_font)
            self.lblTeamNumber = tk.Label(self,text="Team Number: ")
            self.txtTeamNumber = tk.Entry(self)
            self.GetPlayersButton =tk.Button(self,text="Get Player Status",command=lambda:self.GetPlayers())
            self.BackButton= tk.Button(self, text="Back",command=lambda:self.BackButtonRun())
            self.Title.grid(row=0,column =0)
            self.lblTeamNumber.grid(row=1,column=0)
            self.txtTeamNumber.grid(row=1,column =1)
            self.GetPlayersButton.grid(row=1,column =2)
            self.BackButton.grid(row=1,column=3)

