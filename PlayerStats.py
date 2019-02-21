import json
import tkinter as tk
from tkinter import font  as tkfont
from tkinter import messagebox
from tkinter import ttk
from Gui import *
import Config
from AddMatch import *
from SystemToolKit import *

class PlayerStats:
    def BackButtonRun(self):
        global PagesViewed
        PagesViewed.pop()
        self.controller.show_frame(PagesViewed[-1])

    def GetPlayersStats(self):
        Data = SystemToolKit.readFile(Config.PlayerStatsFile)
        TeamID =AddMatch.getTeamId(self.txtTeamNumber.get())
        TeamData = Data[TeamID]
        self.lblPlayerName =tk.Label(self,text="Player Name")
        self.lblLifeTimeGoals =tk.Label(self,text="Life time goals")
        self.lblLifeTimeGreenCards =tk.Label(self,text="Life time green cards")
        self.lblLifeTimeYellowCards =tk.Label(self,text="Life time yellow cards")
        self.lblLifeTimeRedCards =tk.Label(self,text="Life time red cards")
        self.lblLifeTimeGames =tk.Label(self,text="Life time Games")
        self.lblSeasonGoals =tk.Label(self,text="Season goals")
        self.lblSeasonGames =tk.Label(self,text="Season games")
        self.lblSeasonGreenCards =tk.Label(self,text="Season green cards")
        self.lblSeasonYellowCards =tk.Label(self,text="Season yellow cards")
        self.lblSeasonRedCards =tk.Label(self,text="Season red cards")
        self.lblPlayerName.grid(row=3, column =0)
        self.lblSeasonGoals.grid(row=3, column =1)
        self.lblLifeTimeGoals.grid(row=3, column =2)
        self.lblSeasonGames.grid(row=3, column =3)
        self.lblLifeTimeGames.grid(row=3, column =4)
        self.lblSeasonGreenCards.grid(row=3, column =5)
        self.lblSeasonYellowCards.grid(row=3, column =6)
        self.lblSeasonRedCards.grid(row=3, column =7)
        self.lblLifeTimeGreenCards.grid(row=3, column =8)
        self.lblLifeTimeYellowCards.grid(row=3, column =9)
        self.lblLifeTimeRedCards.grid(row=3, column =10)

        for j,i in enumerate(TeamData):
            self.lblPlayerName =tk.Label(self,text=self.GetPlayerName(i))
            self.lblLifeTimeGoals =tk.Label(self,text=TeamData[i]["Life time goals"])
            self.lblLifeTimeGreenCards =tk.Label(self,text=TeamData[i]["Life time green cards"])
            self.lblLifeTimeYellowCards =tk.Label(self,text=TeamData[i]["Life time yellow cards"])
            self.lblLifeTimeRedCards =tk.Label(self,text=TeamData[i]["Life time red cards"])
            self.lblLifeTimeGames =tk.Label(self,text=TeamData[i]["Life time Games"])
            self.lblSeasonGoals =tk.Label(self,text=TeamData[i]["Season goals"])
            self.lblSeasonGames =tk.Label(self,text=TeamData[i]["Season games"])
            self.lblSeasonGreenCards =tk.Label(self,text=TeamData[i]["Season green cards"])
            self.lblSeasonYellowCards =tk.Label(self,text=TeamData[i]["Season yellow cards"])
            self.lblSeasonRedCards =tk.Label(self,text=TeamData[i]["Season red cards"])
            self.lblPlayerName.grid(row=j+4, column =0)
            self.lblSeasonGoals.grid(row=j+4, column =1)
            self.lblLifeTimeGoals.grid(row=j+4, column =2)
            self.lblSeasonGames.grid(row=j+4, column =3)
            self.lblLifeTimeGames.grid(row=j+4, column =4)
            self.lblSeasonGreenCards.grid(row=j+4, column =5)
            self.lblSeasonYellowCards.grid(row=j+4, column =6)
            self.lblSeasonRedCards.grid(row=j+4, column =7)
            self.lblLifeTimeGreenCards.grid(row=j+4, column =8)
            self.lblLifeTimeYellowCards.grid(row=j+4, column =9)
            self.lblLifeTimeRedCards.grid(row=j+4, column =10)


    def GetPlayerName(self,PlayerID):
        Players =SystemToolKit.readFile(Config.PlayerFile)
        return Players[PlayerID]["First name"]+" "+Players[PlayerID]["Last name"]

class PlayerStatsAdmin(tk.Frame,PlayerStats):

        def __init__(self, parent, controller):
            tk.Frame.__init__(self, parent)
            self.controller = controller
            self.Title=tk.Label(self,text="Players Stats",font=controller.title_font)
            self.lblTeamNumber = tk.Label(self,text="Team Number: ")
            self.txtTeamNumber = tk.Entry(self)
            self.GetPlayersButton =tk.Button(self,text="Get Player Stats",command=lambda:self.GetPlayersStats())
            self.BackButton= tk.Button(self, text="Back",command=lambda:self.BackButtonRun())
            self.Title.grid(row=0,column =0)
            self.lblTeamNumber.grid(row=1,column=0)
            self.txtTeamNumber.grid(row=1,column =1)
            self.GetPlayersButton.grid(row=1,column =2)
            self.BackButton.grid(row=1,column=3)

class PlayerStatsPlayer(tk.Frame,PlayerStats):

        def __init__(self, parent, controller):
            tk.Frame.__init__(self, parent)
            self.controller = controller
            self.Title=tk.Label(self,text="Players Stats",font=controller.title_font)
            self.lblTeamNumber = tk.Label(self,text="Team Number: ")
            self.txtTeamNumber = tk.Entry(self)
            self.GetPlayersButton =tk.Button(self,text="Get Player Stats",command=lambda:self.GetPlayersStats())
            self.BackButton= tk.Button(self, text="Back",command=lambda:self.BackButtonRun())
            self.Title.grid(row=0,column =0)
            self.lblTeamNumber.grid(row=1,column=0)
            self.txtTeamNumber.grid(row=1,column =1)
            self.GetPlayersButton.grid(row=1,column =2)
            self.BackButton.grid(row=1,column=3)


class PlayerStatsCoach(tk.Frame,PlayerStats):

        def __init__(self, parent, controller):
            tk.Frame.__init__(self, parent)
            self.controller = controller
            self.Title=tk.Label(self,text="Players Stats",font=controller.title_font)
            self.lblTeamNumber = tk.Label(self,text="Team Number: ")
            self.txtTeamNumber = tk.Entry(self)
            self.GetPlayersButton =tk.Button(self,text="Get Player Stats",command=lambda:self.GetPlayersStats())
            self.BackButton= tk.Button(self, text="Back",command=lambda:self.BackButtonRun())
            self.Title.grid(row=0,column =0)
            self.lblTeamNumber.grid(row=1,column=0)
            self.txtTeamNumber.grid(row=1,column =1)
            self.GetPlayersButton.grid(row=1,column =2)
            self.BackButton.grid(row=1,column=3)
