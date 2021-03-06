import json
import tkinter as tk
from tkinter import font  as tkfont
from tkinter import messagebox
from tkinter import ttk
from SystemToolKit import *
from Gui import *
from Validation import *
import Config
class EditTeam:
    """
    Methods:
        SaveTeam
        GetTeam
        GetPlayer
        updateListboxes
        MovePlayer
        RemovePlayer

    Variables:
        controller
        team - Contains a instance of the Team File
        allPlayers - Contains a instance of the Player File
        orderedList - Contains Player instances to be loaded into the player list box
        TeamPlayers - Contains Player instances to be loaded into the team list box

    """

    def SaveTeam(self):
        """
        Updates the team file with the new team
        """
        Team = SystemToolKit.readFile(Config.TeamFile)
        Data = {}
        for i ,j in enumerate(self.TeamPlayers):
            Data[i] = j
        Data["Team Number"] = self.txtTeamNumber.get()

        for k in Team:
            if Team[k]["Team Number"]==self.txtTeamNumber.get():
                Team[k] = Data
                break
            if k ==len(Team):
                TeamId = uuid.uuid4()
                Team[str(TeamId)] = Data


        with open(Config.TeamFile,"w") as fp:
            json.dump(Team,fp)
        self.controller.show_frame("Home")




    def GetTeam(self):
        """
        Searches through the team file and appends these into the team player List
        Will ignore duplicates
        Calls a updateListbox
        """

        if Validation.TeamNumber(self.txtTeamNumber.get()) ==True:
            for i, j in enumerate(self.team):
                if self.team[j]["Team Number"] == self.txtTeamNumber.get():
                    for k,l in enumerate(self.team[j]):
                        if self.team[j][l] in self.allPlayers.keys():
                            if self.team[j][l] not in self.TeamPlayers and self.team[j][l] not in self.orderedList:
                                self.TeamPlayers.append(self.team[j][l])


        self.updateListboxes()



    def GetPlayer(self):
        """
        Searches through the player file and appends these into the player List
        Will ignore duplicates
        Calls a updateListbox
        """


        data =self.txtPlayer.get()
        if Validation.PresentsCheck(data) == True:
            data = data.lower()
            self.allPlayers = SystemToolKit.readFile(Config.PlayerFile)
            for i,j in enumerate(self.allPlayers):
                if self.allPlayers[j]["First name"].lower() == data or self.allPlayers[j]["Last name"].lower() == data or self.allPlayers[j]["First name"].lower() + " " + self.allPlayers[j]["Last name"].lower() == data:

                    if j not in self.orderedList and j not in self.TeamPlayers:
                        self.orderedList.append(j)



        self.updateListboxes()



    def updateListboxes(self):
        """Updates the PlayerList Listbox and the TeamList Listbox with the contents of orderedList and the TeamPlayer respectively """
        self.TeamList.delete(0, tk.END)
        self.PlayerList.delete(0, tk.END)
        for i in self.orderedList:
            text = str(self.allPlayers[i]["First name"]) + " " + str(self.allPlayers[i]["Last name"])
            self.PlayerList.insert(tk.END,text)
        for j in self.TeamPlayers:
            text = str(self.allPlayers[j]["First name"]) + " " + str(self.allPlayers[j]["Last name"])
            self.TeamList.insert(tk.END,text)


    def MovePlayer(self):
        """Moves a player instance from the orderedList list to the TeamPlayers List """
        if self.PlayerList.index(tk.ANCHOR) < len(self.orderedList):
            j = self.orderedList[self.PlayerList.index(tk.ANCHOR)]
            self.TeamPlayers.append(j)
            self.orderedList.remove(j)
            self.updateListboxes()


    def RemovePlayer(self):
        """Moves a player instance from the TeamPlayers list to the orderedList List """
        if self.TeamList.index(tk.ANCHOR) < len(self.TeamPlayers):
            j = self.TeamPlayers[self.TeamList.index(tk.ANCHOR)]
            self.orderedList.append(j)
            self.TeamPlayers.remove(j)
            self.updateListboxes()


class EditTeamAdmin(tk.Frame,EditTeam):
    """
    Methods:
        __init__
    Variables:
        controller
        orderedList - Contains Player instances to be loaded into the player list box
        TeamPlayers - Contains Player instances to be loaded into the team list box
        Title - Title Label Widget
        lblPlayerName - Player Name Label Widget
        lblPlayer - Player Listbox Heading Label Widget
        lblTeam - Team Listbox Heading Label Widget
        txtTeamNumber - Team Number Entry Widget
        lblTeamNumber - Team Number Label Widet
        txtPlayer - Player Entry Widget
        GetTeamButton - Get Team Button Widget
        getPlayerButton - Get Player Button Widget
        PlayerList - Player Listbox Widget
        TeamList - Team Listbox Widget
        BackButton - Back Button Widget
        MovePlayerButton - Move Player Button Widget
        RemovePlayerButton - Remove Player Button Widget
        SaveButton - Save Button Widget
    """

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
        self.MovePlayerButton = tk.Button(self, text="Move Player",command=self.MovePlayer )
        self.BackButton= tk.Button(self, text="Back",command=lambda:SystemToolKit.BackButtonRun(controller))
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
        self.MovePlayerButton.config(compound="left",background="#307292",relief="flat",font=("Arial", 12, 'bold'),padx=5)
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
        self.MovePlayerButton.grid(row = 3,column = 2)
        self.TeamList.grid(row = 3 ,column = 3 )
        self.RemovePlayerButton.grid(row =3,column = 4)
        self.SaveButton.grid(row = 3,column = 5)
        self.BackButton.grid(row =1,column = 3)
        self.team = SystemToolKit.readFile(Config.TeamFile)
        self.allPlayers = SystemToolKit.readFile(Config.PlayerFile)

class EditTeamCoach(tk.Frame,EditTeam):
    """
    Methods:
        __init__
    Variables:
        controller
        orderedList - Contains Player instances to be loaded into the player list box
        TeamPlayers - Contains Player instances to be loaded into the team list box
        Title - Title Label Widget
        lblPlayerName - Player Name Label Widget
        lblPlayer - Player Listbox Heading Label Widget
        lblTeam - Team Listbox Heading Label Widget
        txtTeamNumber - Team Number Entry Widget
        lblTeamNumber - Team Number Label Widet
        txtPlayer - Player Entry Widget
        GetTeamButton - Get Team Button Widget
        getPlayerButton - Get Player Button Widget
        PlayerList - Player Listbox Widget
        TeamList - Team Listbox Widget
        BackButton - Back Button Widget
        MovePlayerButton - Move Player Button Widget
        RemovePlayerButton - Remove Player Button Widget
        SaveButton - Save Button Widget
    """

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
        self.MovePlayerButton = tk.Button(self, text="Move Player",command=self.MovePlayer )
        self.BackButton= tk.Button(self, text="Back",command=lambda:SystemToolKit.BackButtonRun(controller))
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
        self.MovePlayerButton.config(compound="left",background="#307292",relief="flat",font=("Arial", 12, 'bold'),padx=5)
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
        self.MovePlayerButton.grid(row = 3,column = 2)
        self.TeamList.grid(row = 3 ,column = 3 )
        self.RemovePlayerButton.grid(row =3,column = 4)
        self.SaveButton.grid(row = 3,column = 5)
        self.BackButton.grid(row =1,column = 3)
        self.team = SystemToolKit.readFile(Config.TeamFile)
        self.allPlayers = SystemToolKit.readFile(Config.PlayerFile)

class EditTeamPlayer(tk.Frame,EditTeam):
    """
    Methods:
        __init__
    Variables:
        controller

    """

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller

        """ Widget Declearations """

        """ Widget Stylings """

        """ Widget Positions """