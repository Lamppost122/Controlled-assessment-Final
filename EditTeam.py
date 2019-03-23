import json
import tkinter as tk
from tkinter import font  as tkfont
from tkinter import messagebox
from tkinter import ttk
from SystemToolKit import *
from Gui import *
import Validation
import Config
class EditTeam:

        def BackButtonRun(self):
            Config.PagesViewed.pop()
            self.controller.show_previous_frame(Config.PagesViewed[-1])

        def SaveTeam(self):
            Team = SystemToolKit.readFile(Config.TeamFile)

            TeamId = uuid.uuid4()
            Data = {}
            for i ,j in enumerate(self.TeamPlayers):
                Data[i] = j
            Data["Team Number"] = self.txtTeamNumber.get()
            Team[str(TeamId)] = Data

            with open(Config.TeamFile,"w") as fp:
                json.dump(Team,fp)

        def GetPlayer(self):
            self.PlayerList.delete(0,tk.END)
            data =self.txtPlayer.get()
            if Validation.PresentsCheck(data) == True:
                data = data.lower()
                for i,j in enumerate(self.allPlayers):
                    if self.allPlayers[j]["First name"].lower() == data or self.allPlayers[j]["Last name"].lower() == data or self.allPlayers[j]["First name"].lower() + " " + self.allPlayers[j]["Last name"].lower() == data:

                        self.orderedList.append(j)
                        text = str(self.allPlayers[j]["First name"]) + " " + str(self.allPlayers[j]["Last name"])
                        self.PlayerList.insert(tk.END,text)

        def GetTeam(self):
            if Validation.TeamNumber(self.txtTeamNumber.get()) ==True:
                for i, j in enumerate(self.team):
                    if self.team[j]["Team Number"] == self.txtTeamNumber.get():
                        for k,l in enumerate(self.allPlayers):
                            self.TeamPlayers.append(self.team[j][str(k)])
                            text = str(self.allPlayers[self.team[j][str(k)]]["First name"]) + " " + str(self.allPlayers[self.team[j][str(k)]]["Last name"])
                            self.TeamList.insert(tk.END,text)


        def MovePlayer(self):
            if self.PlayerList.index(tk.ANCHOR) < len(self.orderedList):
                j = self.orderedList[self.PlayerList.index(tk.ANCHOR)]
                text = str(self.allPlayers[j]["First name"]) + " " + str(self.allPlayers[j]["Last name"])
                self.TeamPlayers.append(j)
                self.orderedList.pop()
                self.TeamList.insert(tk.END,text)
                self.PlayerList.delete(tk.ANCHOR)

        def RemovePlayer(self):
            if self.TeamList.index(tk.ANCHOR) < len(self.TeamPlayers):
                j = self.TeamPlayers[self.TeamList.index(tk.ANCHOR)]
                text = str(self.allPlayers[j]["First name"]) + " " + str(self.allPlayers[j]["Last name"])
                self.orderedList.append(j)
                self.TeamPlayers.pop()
                self.PlayerList.insert(tk.END,text)
                self.TeamList.delete(tk.ANCHOR)

class EditTeamAdmin(tk.Frame,EditTeam):

        def __init__(self, parent, controller):
            tk.Frame.__init__(self, parent)
            self.controller = controller
            self.TeamPlayers = []
            self.orderedList = []

            """ Widget Declearations """

            self.Title = tk.Label(self,text = "Edit Team" ,font = controller.title_font)
            self.lblPlayerName = tk.Label(self,text = "Player Name: ")
            self.lblPlayer = tk.Label(self,text = "Players ")
            self.lblTeam = tk.Label(self,text="Team")
            self.txtTeamNumber = ttk.Entry(self)
            self.lblTeamNumber = tk.Label(self,text="Team Number: ")
            self.txtPlayer = ttk.Entry(self)
            self.GetTeamButton = tk.Button(self,text = "Get Team",command = self.GetTeam)
            self.getPlayerButton = tk.Button(self,text = "Get Player",command = self.GetPlayer)
            self.PlayerList = tk.Listbox(self)
            self.TeamList = tk.Listbox(self)
            b = tk.Button(self, text="Move Player",command=self.MovePlayer )
            self.BackButton= tk.Button(self, text="Back",command=lambda:self.BackButtonRun())
            self.RemovePlayerButton = tk.Button(self,text= "Remove Player",command = self.RemovePlayer)
            self.SaveButton = tk.Button(self,text = "Save",command = self.SaveTeam)

            """ Widget Stylings """

            self.Title.config(background="#8ABFD9",fg = "#404040",pady="5")
            self.lblPlayerName.config(justify="right",fg = "black",background="#8ABFD9",font=("Arial", 10, 'bold'))
            self.lblPlayer.config(justify="right",fg = "black",background="#8ABFD9",font=("Arial", 10, 'bold'))
            self.lblTeam.config(justify="right",fg = "black",background="#8ABFD9",font=("Arial", 10, 'bold'))
            self.lblTeamNumber.config(justify="right",fg = "black",background="#8ABFD9",font=("Arial", 10, 'bold'))
            self.GetTeamButton.config(compound="left",background="#307292",relief="flat",font=("Arial", 12, 'bold'),padx=5)
            self.getPlayerButton.config(compound="left",background="#307292",relief="flat",font=("Arial", 12, 'bold'),padx=5)
            b.config(compound="left",background="#307292",relief="flat",font=("Arial", 12, 'bold'),padx=5)
            self.BackButton.config(compound="left",background="#307292",relief="flat",font=("Arial", 12, 'bold'),padx=5)
            self.RemovePlayerButton.config(compound="left",background="#307292",relief="flat",font=("Arial", 12, 'bold'),padx=5)
            self.SaveButton.config(compound="left",background="#307292",relief="flat",font=("Arial", 12, 'bold'),padx=5)

            """ Widget Positions """

            self.Title.grid(row = 0,column = 0,columnspan = 3)
            self.lblPlayerName.grid(row = 1,column = 0)
            self.txtPlayer.grid(row = 1,column = 1 )
            self.getPlayerButton.grid(row= 1 , column = 2)
            self.lblTeamNumber.grid(row= 1,column = 4)
            self.txtTeamNumber.grid(row= 1 ,column =5)
            self.GetTeamButton.grid(row=1,column =6)
            self.lblPlayer.grid(row = 2,column = 1)
            self.lblTeam.grid(row= 2,column = 3)
            self.PlayerList.grid(row = 3,column = 1)
            b.grid(row = 3,column = 2)
            self.TeamList.grid(row = 3 ,column = 3 )
            self.RemovePlayerButton.grid(row =3,column = 4)
            self.SaveButton.grid(row = 3,column = 5)
            self.BackButton.grid(row =1,column = 3)
            self.team = SystemToolKit.readFile(Config.TeamFile)
            self.allPlayers = SystemToolKit.readFile(Config.PlayerFile)

class EditTeamCoach(tk.Frame,EditTeam):

        def __init__(self, parent, controller):
            tk.Frame.__init__(self, parent)
            self.controller = controller
            self.TeamPlayers = []
            self.orderedList = []

            """ Widget Declearations """

            self.Title = tk.Label(self,text = "Edit Team" ,font = controller.title_font)
            self.lblPlayerName = tk.Label(self,text = "Player Name: ")
            self.lblPlayer = tk.Label(self,text = "Players ")
            self.lblTeam = tk.Label(self,text="Team")
            self.txtTeamNumber = ttk.Entry(self)
            self.lblTeamNumber = tk.Label(self,text="Team Number: ")
            self.txtPlayer = ttk.Entry(self)
            self.GetTeamButton = tk.Button(self,text = "Get Team",command = self.GetTeam)
            self.getPlayerButton = tk.Button(self,text = "Get Player",command = self.GetPlayer)
            self.PlayerList = tk.Listbox(self)
            self.TeamList = tk.Listbox(self)
            b = tk.Button(self, text="Move Player",command=self.MovePlayer )
            self.BackButton= tk.Button(self, text="Back",command=lambda:self.BackButtonRun())
            self.RemovePlayerButton = tk.Button(self,text= "Remove Player",command = self.RemovePlayer)
            self.SaveButton = tk.Button(self,text = "Save",command = self.SaveTeam)

            """ Widget Stylings """

            self.Title.config(background="#8ABFD9",fg = "#404040",pady="5")
            self.lblPlayerName.config(justify="right",fg = "black",background="#8ABFD9",font=("Arial", 10, 'bold'))
            self.lblPlayer.config(justify="right",fg = "black",background="#8ABFD9",font=("Arial", 10, 'bold'))
            self.lblTeam.config(justify="right",fg = "black",background="#8ABFD9",font=("Arial", 10, 'bold'))
            self.lblTeamNumber.config(justify="right",fg = "black",background="#8ABFD9",font=("Arial", 10, 'bold'))
            self.GetTeamButton.config(compound="left",background="#307292",relief="flat",font=("Arial", 12, 'bold'),padx=5)
            self.getPlayerButton.config(compound="left",background="#307292",relief="flat",font=("Arial", 12, 'bold'),padx=5)
            b.config(compound="left",background="#307292",relief="flat",font=("Arial", 12, 'bold'),padx=5)
            self.BackButton.config(compound="left",background="#307292",relief="flat",font=("Arial", 12, 'bold'),padx=5)
            self.RemovePlayerButton.config(compound="left",background="#307292",relief="flat",font=("Arial", 12, 'bold'),padx=5)
            self.SaveButton.config(compound="left",background="#307292",relief="flat",font=("Arial", 12, 'bold'),padx=5)

            """ Widget Positions """

            self.Title.grid(row = 0,column = 0,columnspan = 3)
            self.lblPlayerName.grid(row = 1,column = 0)
            self.txtPlayer.grid(row = 1,column = 1 )
            self.getPlayerButton.grid(row= 1 , column = 2)
            self.lblTeamNumber.grid(row= 1,column = 4)
            self.txtTeamNumber.grid(row= 1 ,column =5)
            self.GetTeamButton.grid(row=1,column =6)
            self.lblPlayer.grid(row = 2,column = 1)
            self.lblTeam.grid(row= 2,column = 3)
            self.PlayerList.grid(row = 3,column = 1)
            b.grid(row = 3,column = 2)
            self.TeamList.grid(row = 3 ,column = 3 )
            self.RemovePlayerButton.grid(row =3,column = 4)
            self.SaveButton.grid(row = 3,column = 5)
            self.BackButton.grid(row =1,column = 3)
            self.team = SystemToolKit.readFile(Config.TeamFile)
            self.allPlayers = SystemToolKit.readFile(Config.PlayerFile)

class EditTeamPlayer(tk.Frame,EditTeam):

        def __init__(self, parent, controller):
            tk.Frame.__init__(self, parent)
            self.controller = controller

            """ Widget Declearations """

            """ Widget Stylings """

            """ Widget Positions """
