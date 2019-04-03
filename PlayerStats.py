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
        try:
            TeamData = Data[TeamID]
        except KeyError:
            messagebox.showinfo("Error Message","No Stats available for that team")
            return None
        for i in self.grid_slaves():
            if int(i.grid_info()["row"]) >=3:
                i.grid_forget()


        """ Widget Declearations """

        self.lblPlayerName =tk.Label(self,text="Player\nName")
        self.lblLifeTimeGoals =tk.Label(self,text="Life time\ngoals")
        self.lblLifeTimeGreenCards =tk.Label(self,text="Life time\ngreen cards")
        self.lblLifeTimeYellowCards =tk.Label(self,text="Life time\nyellow cards")
        self.lblLifeTimeRedCards =tk.Label(self,text="Life time\nred cards")
        self.lblLifeTimeGames =tk.Label(self,text="Life time\nGames")
        self.lblSeasonGoals =tk.Label(self,text="Season\ngoals")
        self.lblSeasonGames =tk.Label(self,text="Season\n games")
        self.lblSeasonGreenCards =tk.Label(self,text="Season\ngreen cards")
        self.lblSeasonYellowCards =tk.Label(self,text="Season\nyellow cards")
        self.lblSeasonRedCards =tk.Label(self,text="Season\nred cards")

        """ Widget Stylings """

        self.lblPlayerName.config(justify="center",fg = "black",background="#8ABFD9",font=("Arial", 8, 'bold'))
        self.lblLifeTimeGoals.config(justify="center",fg = "black",background="#8ABFD9",font=("Arial", 8, 'bold'))
        self.lblLifeTimeGreenCards.config(justify="center",fg = "black",background="#8ABFD9",font=("Arial", 8, 'bold'))
        self.lblLifeTimeYellowCards.config(justify="center",fg = "black",background="#8ABFD9",font=("Arial", 8, 'bold'))
        self.lblLifeTimeRedCards.config(justify="center",fg = "black",background="#8ABFD9",font=("Arial", 8, 'bold'))
        self.lblLifeTimeGames.config(justify="center",fg = "black",background="#8ABFD9",font=("Arial", 8, 'bold'))
        self.lblSeasonGoals.config(justify="center",fg = "black",background="#8ABFD9",font=("Arial", 8, 'bold'))
        self.lblSeasonGames.config(justify="center",fg = "black",background="#8ABFD9",font=("Arial", 8, 'bold'))
        self.lblSeasonGreenCards.config(justify="center",fg = "black",background="#8ABFD9",font=("Arial", 8, 'bold'))
        self.lblSeasonYellowCards.config(justify="center",fg = "black",background="#8ABFD9",font=("Arial", 8, 'bold'))
        self.lblSeasonRedCards.config(justify="center",fg = "black",background="#8ABFD9",font=("Arial", 8, 'bold'))

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
        if self.var2.get() == "Highest":
            order = True
        else:
            order =False

        SortedTeamData=sorted(TeamData.items() ,  key=lambda x: x[1][self.var1.get()],reverse=order)

        for j,i in enumerate(SortedTeamData):


            playerID = i[0]

            """ Widget Declearations """

            self.lblPlayerName =tk.Label(self,text=self.GetPlayerName(playerID))
            self.lblLifeTimeGoals =tk.Label(self,text=TeamData[playerID]["Life time goals"])
            self.lblLifeTimeGreenCards =tk.Label(self,text=TeamData[playerID]["Life time green cards"])
            self.lblLifeTimeYellowCards =tk.Label(self,text=TeamData[playerID]["Life time yellow cards"])
            self.lblLifeTimeRedCards =tk.Label(self,text=TeamData[playerID]["Life time red cards"])
            self.lblLifeTimeGames =tk.Label(self,text=TeamData[playerID]["Life time Games"])
            self.lblSeasonGoals =tk.Label(self,text=TeamData[playerID]["Season goals"])
            self.lblSeasonGames =tk.Label(self,text=TeamData[playerID]["Season games"])
            self.lblSeasonGreenCards =tk.Label(self,text=TeamData[playerID]["Season green cards"])
            self.lblSeasonYellowCards =tk.Label(self,text=TeamData[playerID]["Season yellow cards"])
            self.lblSeasonRedCards =tk.Label(self,text=TeamData[playerID]["Season red cards"])

            """ Widget Stylings """

            self.lblPlayerName.config(justify="right",fg = "black",background="#8ABFD9",font=("Arial", 8, 'bold'))
            self.lblLifeTimeGoals.config(justify="right",fg = "black",background="#8ABFD9",font=("Arial", 8, 'bold'))
            self.lblLifeTimeGreenCards.config(justify="right",fg = "black",background="#8ABFD9",font=("Arial", 8, 'bold'))
            self.lblLifeTimeYellowCards.config(justify="right",fg = "black",background="#8ABFD9",font=("Arial", 8, 'bold'))
            self.lblLifeTimeRedCards.config(justify="right",fg = "black",background="#8ABFD9",font=("Arial", 8, 'bold'))
            self.lblLifeTimeGames.config(justify="right",fg = "black",background="#8ABFD9",font=("Arial", 8, 'bold'))
            self.lblSeasonGoals.config(justify="right",fg = "black",background="#8ABFD9",font=("Arial", 8, 'bold'))
            self.lblSeasonGames.config(justify="right",fg = "black",background="#8ABFD9",font=("Arial", 8, 'bold'))
            self.lblSeasonGreenCards.config(justify="right",fg = "black",background="#8ABFD9",font=("Arial", 8, 'bold'))
            self.lblSeasonYellowCards.config(justify="right",fg = "black",background="#8ABFD9",font=("Arial", 8, 'bold'))
            self.lblSeasonRedCards.config(justify="right",fg = "black",background="#8ABFD9",font=("Arial", 8, 'bold'))

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
        self.var1 = tk.StringVar()
        self.var2 = tk.StringVar()
        SortOptions = ["Life time goals","Life time green cards","Life time yellow cards","Life time red cards","Season goals","Season green cards","Season yellow cards","Season red cards"]
        OrderOpitons = ["Highest","Lowest"]
        self.var1.set(SortOptions[0])
        self.var2.set(OrderOpitons[0])
        self.cmbSort = tk.OptionMenu(self, self.var1,*SortOptions)
        self.cmbOrder = tk.OptionMenu(self, self.var2,*OrderOpitons)
        self.lblSort = tk.Label(self,text="Sort:")


        """ Widget Stylings """

        self.Title.config(background="#8ABFD9",fg = "#404040",pady="5")
        self.lblTeamNumber.config(justify="right",fg = "black",background="#8ABFD9",font=("Arial", 10, 'bold'))
        self.GetPlayersButton.config(compound="left",background="#307292",relief="flat",font=("Arial", 12, 'bold'),padx=5)
        self.BackButton.config(compound="left",background="#307292",relief="flat",font=("Arial", 12, 'bold'),padx=5)
        self.lblSort.config(justify="right",fg = "black",background="#8ABFD9",font=("Arial", 10, 'bold'))

        """ Widget Positions """

        self.Title.grid(row=0,column =0,columnspan = 6)
        self.cmbSort.grid(row=1,column=1)
        self.cmbOrder.grid(row=1,column=2)
        self.lblSort.grid(row=1,column=0)
        self.lblTeamNumber.grid(row=1,column=3)
        self.txtTeamNumber.grid(row=1,column =4)
        self.GetPlayersButton.grid(row=1,column =5)
        self.BackButton.grid(row=1,column=6)


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