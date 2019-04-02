import json
import tkinter as tk
from tkinter import font  as tkfont
from tkinter import messagebox
from tkinter import ttk
from Gui import *
import Config
from SystemToolKit import *
from SystemToolKit import *

class PlayerStats:
    """
    Methods:
        GetPlayersStats
        GetPlayerName
    Variables:
        lblPlayerName - Player Names Label Widget
        lblLifeTimeGoals - Life time Goal Label Widget
        lblLifeTimeGreenCards - Life time Green Card Label Widget
        lblLifeTimeYellowCards - Life time Yellow Cards Label Widget
        lblLifeTimeRedCards - Life time Red Cards Label Widget
        lblLifeTimeGames - Life time Games Label Widget
        lblSeasonGoals - Season Goals Label Widget
        lblSeasonGames - Season Games Label Widget
        lblSeasonGreenCards - Season Green Cards Label Widget
        lblSeasonYellowCards - Season Yellow Cards Label Widget
        lblSeasonRedCards - Season Red Cards Label Widget

    """

    def GetPlayersStats(self):
        """ Adds player Stats to the screen """
        Data = SystemToolKit.readFile(Config.PlayerStatsFile)
        TeamID =SystemToolKit.getTeamId(self.txtTeamNumber.get())
        TeamData = Data[TeamID]

        """ Widget Declearations """

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

        """ Widget Stylings """

        self.lblPlayerName.config(justify="right",fg = "black",background="#8ABFD9",font=("Arial", 10, 'bold'))
        self.lblLifeTimeGoals.config(justify="right",fg = "black",background="#8ABFD9",font=("Arial", 10, 'bold'))
        self.lblLifeTimeGreenCards.config(justify="right",fg = "black",background="#8ABFD9",font=("Arial", 10, 'bold'))
        self.lblLifeTimeYellowCards.config(justify="right",fg = "black",background="#8ABFD9",font=("Arial", 10, 'bold'))
        self.lblLifeTimeRedCards.config(justify="right",fg = "black",background="#8ABFD9",font=("Arial", 10, 'bold'))
        self.lblLifeTimeGames.config(justify="right",fg = "black",background="#8ABFD9",font=("Arial", 10, 'bold'))
        self.lblSeasonGoals.config(justify="right",fg = "black",background="#8ABFD9",font=("Arial", 10, 'bold'))
        self.lblSeasonGames.config(justify="right",fg = "black",background="#8ABFD9",font=("Arial", 10, 'bold'))
        self.lblSeasonGreenCards.config(justify="right",fg = "black",background="#8ABFD9",font=("Arial", 10, 'bold'))
        self.lblSeasonYellowCards.config(justify="right",fg = "black",background="#8ABFD9",font=("Arial", 10, 'bold'))
        self.lblSeasonRedCards.config(justify="right",fg = "black",background="#8ABFD9",font=("Arial", 10, 'bold'))

        """ Widget Positions """

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

            """ Widget Declearations """

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

            """ Widget Stylings """

            self.lblPlayerName.config(justify="right",fg = "black",background="#8ABFD9",font=("Arial", 10, 'bold'))
            self.lblLifeTimeGoals.config(justify="right",fg = "black",background="#8ABFD9",font=("Arial", 10, 'bold'))
            self.lblLifeTimeGreenCards.config(justify="right",fg = "black",background="#8ABFD9",font=("Arial", 10, 'bold'))
            self.lblLifeTimeYellowCards.config(justify="right",fg = "black",background="#8ABFD9",font=("Arial", 10, 'bold'))
            self.lblLifeTimeRedCards.config(justify="right",fg = "black",background="#8ABFD9",font=("Arial", 10, 'bold'))
            self.lblLifeTimeGames.config(justify="right",fg = "black",background="#8ABFD9",font=("Arial", 10, 'bold'))
            self.lblSeasonGoals.config(justify="right",fg = "black",background="#8ABFD9",font=("Arial", 10, 'bold'))
            self.lblSeasonGames.config(justify="right",fg = "black",background="#8ABFD9",font=("Arial", 10, 'bold'))
            self.lblSeasonGreenCards.config(justify="right",fg = "black",background="#8ABFD9",font=("Arial", 10, 'bold'))
            self.lblSeasonYellowCards.config(justify="right",fg = "black",background="#8ABFD9",font=("Arial", 10, 'bold'))
            self.lblSeasonRedCards.config(justify="right",fg = "black",background="#8ABFD9",font=("Arial", 10, 'bold'))

            """ Widget Positions """

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
        """ returns player name(String)"""
        Players =SystemToolKit.readFile(Config.PlayerFile)
        return Players[PlayerID]["First name"]+" "+Players[PlayerID]["Last name"]

class PlayerStatsAdmin(tk.Frame,PlayerStats):
    """
    Methods:
        __init__
    Variables:
        controller
        Title - Title Label Widget
        lblTeamNumber -Team Number Label widget
        txtTeamNumber - Team Number Entry Widget
        GetPlayersButton - Get Player Button Widget
        BackButton - Back Button Label Widget

    """



    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller

        """ Widget Declearations """

        self.Title=tk.Label(self,text="Players Stats",font=controller.title_font)
        self.lblTeamNumber = tk.Label(self,text="Team Number: ")
        self.txtTeamNumber = tk.Entry(self)
        self.GetPlayersButton =tk.Button(self,text="Get Player Stats",command=lambda:self.GetPlayersStats())
        self.BackButton= tk.Button(self, text="Back",command=lambda:SystemToolKit.BackButtonRun(controller))

        """ Widget Stylings """

        self.Title.config(background="#8ABFD9",fg = "#404040",pady="5")
        self.lblTeamNumber.config(justify="right",fg = "black",background="#8ABFD9",font=("Arial", 10, 'bold'))
        self.GetPlayersButton.config(compound="left",background="#307292",relief="flat",font=("Arial", 12, 'bold'),padx=5)
        self.BackButton.config(compound="left",background="#307292",relief="flat",font=("Arial", 12, 'bold'),padx=5)

        """ Widget Positions """

        self.Title.grid(row=0,column =0)
        self.lblTeamNumber.grid(row=1,column=0)
        self.txtTeamNumber.grid(row=1,column =1)
        self.GetPlayersButton.grid(row=1,column =2)
        self.BackButton.grid(row=1,column=3)

class PlayerStatsPlayer(tk.Frame,PlayerStats):

    """
    Methods:
        __init__
    Variables:
        controller
        Title - Title Label Widget
        lblTeamNumber -Team Number Label widget
        txtTeamNumber - Team Number Entry Widget
        GetPlayersButton - Get Player Button Widget
        BackButton - Back Button Label Widget

    """
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller

        """ Widget Declearations """

        self.Title=tk.Label(self,text="Players Stats",font=controller.title_font)
        self.lblTeamNumber = tk.Label(self,text="Team Number: ")
        self.txtTeamNumber = tk.Entry(self)
        self.GetPlayersButton =tk.Button(self,text="Get Player Stats",command=lambda:self.GetPlayersStats())
        self.BackButton= tk.Button(self, text="Back",command=lambda:SystemToolKit.BackButtonRun(controller))

        """ Widget Stylings """

        self.Title.config(background="#8ABFD9",fg = "#404040",pady="5")
        self.lblTeamNumber.config(justify="right",fg = "black",background="#8ABFD9",font=("Arial", 10, 'bold'))
        self.GetPlayersButton.config(compound="left",background="#307292",relief="flat",font=("Arial", 12, 'bold'),padx=5)
        self.BackButton.config(compound="left",background="#307292",relief="flat",font=("Arial", 12, 'bold'),padx=5)

        """ Widget Positions """

        self.Title.grid(row=0,column =0)
        self.lblTeamNumber.grid(row=1,column=0)
        self.txtTeamNumber.grid(row=1,column =1)
        self.GetPlayersButton.grid(row=1,column =2)
        self.BackButton.grid(row=1,column=3)


class PlayerStatsCoach(tk.Frame,PlayerStats):
    """
    Methods:
        __init__
    Variables:
        controller
        Title - Title Label Widget
        lblTeamNumber -Team Number Label widget
        txtTeamNumber - Team Number Entry Widget
        GetPlayersButton - Get Player Button Widget
        BackButton - Back Button Label Widget

    """

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller

        """ Widget Declearations """

        self.Title=tk.Label(self,text="Players Stats",font=controller.title_font)
        self.lblTeamNumber = tk.Label(self,text="Team Number: ")
        self.txtTeamNumber = tk.Entry(self)
        self.GetPlayersButton =tk.Button(self,text="Get Player Stats",command=lambda:self.GetPlayersStats())
        self.BackButton= tk.Button(self, text="Back",command=lambda:SystemToolKit.BackButtonRun(controller))

        """ Widget Stylings """

        self.Title.config(background="#8ABFD9",fg = "#404040",pady="5")
        self.lblTeamNumber.config(justify="right",fg = "black",background="#8ABFD9",font=("Arial", 10, 'bold'))
        self.GetPlayersButton.config(compound="left",background="#307292",relief="flat",font=("Arial", 12, 'bold'),padx=5)
        self.BackButton.config(compound="left",background="#307292",relief="flat",font=("Arial", 12, 'bold'),padx=5)

        """ Widget Positions """

        self.Title.grid(row=0,column =0)
        self.lblTeamNumber.grid(row=1,column=0)
        self.txtTeamNumber.grid(row=1,column =1)
        self.GetPlayersButton.grid(row=1,column =2)
        self.BackButton.grid(row=1,column=3)