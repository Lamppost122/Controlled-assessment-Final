import json
import tkinter as tk
from tkinter import font  as tkfont
from tkinter import messagebox
from tkinter import ttk
from Gui import *
import Config

class AddTeam :
    """
    Method:
        SaveTeam
        GetPlayer
        updateListboxes
        MovePlayer
        RemovePlayer

    Variables:
        allPlayers - Contains a instance of the player file
        orderedList - Contains player instances to be loaded into the PlayerList
        TeamPlayer - Contains player instances to be loaded into the TeamList

    """

    def SaveTeam(self):
        """
        Adds the current team to the Team File
        Validates the Team Number
        Calls the Home Frame
        """
        Team = SystemToolKit.readFile(Config.TeamFile)

        TeamId = uuid.uuid4()
        if Validation.newTeam(self.txtTeamNumber.get()) == True:
            Data = {}
            for i ,j in enumerate(self.TeamPlayers):
                Data[i] = j
            Data["Team Number"] = self.txtTeamNumber.get()
            Team[str(TeamId)] = Data

            with open(Config.TeamFile,"w") as fp:
                json.dump(Team,fp)
            self.controller.show_frame("Home")

    def GetPlayer(self):
        """
        Searchs for players in the player file by First Name, Last Name and (First Name + Last Name)
        If Not a duplicate will add these results to the orderedList Class Variable
        Calls a Listbox Update
        """

        data =self.txtPlayer.get()
        if Validation.PresentsCheck(data) == True:
            data = data.lower()
            self.allPlayers = SystemToolKit.readFile(Config.PlayerFile)
            for i,j in enumerate(self.allPlayers):
                if self.allPlayers[j]["First name"].lower() == data or self.allPlayers[j]["Last name"].lower() == data or self.allPlayers[j]["First name"].lower() + " " + self.allPlayers[j]["Last name"].lower() == data:
                    if j not in self.orderedList and j not in self.TeamPlayers:
                        self.orderedList.append(j)

                    else:
                        Duplicates = False

        self.updateListboxes()



    def updateListboxes(self):
        """
        Updates the TeamList and PlayerList with the current contents of orderedList and TeamPlayers respectively
        """
        self.TeamList.delete(0, tk.END)
        self.PlayerList.delete(0, tk.END)
        for i in self.orderedList:
            text = str(self.allPlayers[i]["First name"]) + " " + str(self.allPlayers[i]["Last name"])
            self.PlayerList.insert(tk.END,text)
        for j in self.TeamPlayers:
            text = str(self.allPlayers[j]["First name"]) + " " + str(self.allPlayers[j]["Last name"])
            self.TeamList.insert(tk.END,text)


    def MovePlayer(self):
        """
        Switches a player instance from orderedList to TeamPlayer
        Calls a Listbox Update
        """
        if self.PlayerList.index(tk.ANCHOR) < len(self.orderedList):
            j = self.orderedList[self.PlayerList.index(tk.ANCHOR)]
            self.TeamPlayers.append(j)
            self.orderedList.remove(j)
            self.updateListboxes()


    def RemovePlayer(self):
        """
        Switches a player instance from TeamPlayer to orderedList
        Calls a Listbox Update
        """
        if self.TeamList.index(tk.ANCHOR) < len(self.TeamPlayers):
            j = self.TeamPlayers[self.TeamList.index(tk.ANCHOR)]
            self.orderedList.append(j)
            self.TeamPlayers.remove(j)
            self.updateListboxes()



class AddTeamCoach(tk.Frame,AddTeam):
    """
    Methods:
        __init__
    Variables:
        controller
        orderedList - Contains player instances to be loaded into the PlayerList
        TeamPlayer - Contains player instances to be loaded into the TeamList
        Title - Title Label Widget
        lblPlayerName - Player Name Label Widget
        lblPlayer - Player Heading Label Widget
        lblTeam - Team Heading Label Widget
        txtTeamNumber - Team Number Entry Widget
        lblTeamNumber - Team Number Label Widget
        txtPlayer - Player Entry Widget
        getPlayerButton - Get Player Button Widget
        PlayerList - Player List Listbox Widget
        TeamList -Team List Listbo Widget
        BackButton - Back Button Widget
        RemovePlayerButton - Remove Player Button Widget
        SaveButton - Save Button Widget

    """

    def __init__(self, parent, controller):
        """
        Initalises a frame instance of Add Team At Coach Access Level
        """
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.TeamPlayers = []
        self.orderedList = []

        """ Widget Declearations """

        self.Title = tk.Label(self,text = "Create Team" ,font = controller.title_font)
        self.lblPlayerName = tk.Label(self,text = "Player Name: ")
        self.lblPlayer = tk.Label(self,text = "Players ")
        self.lblTeam = tk.Label(self,text="Team")
        self.txtTeamNumber = ttk.Entry(self)
        self.lblTeamNumber = tk.Label(self,text="Team Number: ")
        self.txtPlayer = ttk.Entry(self)
        self.getPlayerButton = tk.Button(self,text = "Get Player",command = self.GetPlayer)
        self.PlayerList = tk.Listbox(self)
        self.TeamList = tk.Listbox(self)
        b = tk.Button(self, text="Move Player",command=self.MovePlayer )
        self.BackButton= tk.Button(self, text="Back",command=lambda:SystemToolKit.BackButtonRun(controller))
        self.RemovePlayerButton = tk.Button(self,text= "Remove Player",command = self.RemovePlayer)
        self.SaveButton = tk.Button(self,text = "Save",command = self.SaveTeam)

        """ Widget Stylings """

        self.lblPlayerName.config(justify="right",fg = "black",background="#8ABFD9",font=("Arial", 10, 'bold'))
        self.lblPlayer.config(justify="right",fg = "black",background="#8ABFD9",font=("Arial", 10, 'bold'))
        self.lblTeam.config(justify="right",fg = "black",background="#8ABFD9",font=("Arial", 10, 'bold'))
        self.lblTeamNumber.config(justify="right",fg = "black",background="#8ABFD9",font=("Arial", 10, 'bold'))
        self.getPlayerButton.config(compound="left",background="#307292",relief="flat",font=("Arial", 12, 'bold'),padx=5)
        b.config(compound="left",background="#307292",relief="flat",font=("Arial", 12, 'bold'),padx=5)
        self.BackButton.config(compound="left",background="#307292",relief="flat",font=("Arial", 12, 'bold'),padx=5)
        self.RemovePlayerButton.config(compound="left",background="#307292",relief="flat",font=("Arial", 12, 'bold'),padx=5)
        self.SaveButton.config(compound="left",background="#307292",relief="flat",font=("Arial", 12, 'bold'),padx=5)
        self.Title.config(background="#8ABFD9",fg = "#404040",pady="5")

        """ Widget Positions """

        self.Title.grid(row = 0,column = 0,columnspan = 3)
        self.lblPlayerName.grid(row = 1,column = 0)
        self.txtPlayer.grid(row = 1,column = 1 )
        self.getPlayerButton.grid(row= 1 , column = 2)
        self.lblTeamNumber.grid(row= 1,column = 4)
        self.txtTeamNumber.grid(row= 1 ,column =5)
        self.lblPlayer.grid(row = 2,column = 1)
        self.lblTeam.grid(row= 2,column = 3)
        self.PlayerList.grid(row = 3,column = 1)
        b.grid(row = 3,column = 2)
        self.TeamList.grid(row = 3 ,column = 3 )
        self.RemovePlayerButton.grid(row =3,column = 4)
        self.SaveButton.grid(row = 3,column = 5)
        self.BackButton.grid(row =1,column = 3)


class AddTeamAdmin(tk.Frame,AddTeam):
    """
    Methods:
        __init__
    Variables:
        controller
        orderedList - Contains player instances to be loaded into the PlayerList
        TeamPlayer - Contains player instances to be loaded into the TeamList
        Title - Title Label Widget
        lblPlayerName - Player Name Label Widget
        lblPlayer - Player Heading Label Widget
        lblTeam - Team Heading Label Widget
        txtTeamNumber - Team Number Entry Widget
        lblTeamNumber - Team Number Label Widget
        txtPlayer - Player Entry Widget
        getPlayerButton - Get Player Button Widget
        PlayerList - Player List Listbox Widget
        TeamList -Team List Listbo Widget
        BackButton - Back Button Widget
        RemovePlayerButton - Remove Player Button Widget
        SaveButton - Save Button Widget

    """

    def __init__(self, parent, controller):
        """
        Initalises a frame instance of Add Team At Admin Access Level
        """
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.TeamPlayers = []
        self.orderedList = []

        """ Widget Declearations """

        self.Title = tk.Label(self,text = "Create Team" ,font = controller.title_font)
        self.lblPlayerName = tk.Label(self,text = "Player Name: ")
        self.lblPlayer = tk.Label(self,text = "Players ")
        self.lblTeam = tk.Label(self,text="Team")
        self.txtTeamNumber = ttk.Entry(self)
        self.lblTeamNumber = tk.Label(self,text="Team Number: ")
        self.txtPlayer = ttk.Entry(self)
        self.getPlayerButton = tk.Button(self,text = "Get Player",command = self.GetPlayer)
        self.PlayerList = tk.Listbox(self)
        self.TeamList = tk.Listbox(self)
        b = tk.Button(self, text="Move Player",command=self.MovePlayer )
        self.BackButton= tk.Button(self, text="Back",command=lambda:SystemToolKit.BackButtonRun(controller))
        self.RemovePlayerButton = tk.Button(self,text= "Remove Player",command = self.RemovePlayer)
        self.SaveButton = tk.Button(self,text = "Save",command = self.SaveTeam)

        """ Widget Stylings """

        self.lblPlayerName.config(justify="right",fg = "black",background="#8ABFD9",font=("Arial", 10, 'bold'))
        self.lblPlayer.config(justify="right",fg = "black",background="#8ABFD9",font=("Arial", 10, 'bold'))
        self.lblTeam.config(justify="right",fg = "black",background="#8ABFD9",font=("Arial", 10, 'bold'))
        self.lblTeamNumber.config(justify="right",fg = "black",background="#8ABFD9",font=("Arial", 10, 'bold'))
        self.getPlayerButton.config(compound="left",background="#307292",relief="flat",font=("Arial", 12, 'bold'),padx=5)
        b.config(compound="left",background="#307292",relief="flat",font=("Arial", 12, 'bold'),padx=5)
        self.BackButton.config(compound="left",background="#307292",relief="flat",font=("Arial", 12, 'bold'),padx=5)
        self.RemovePlayerButton.config(compound="left",background="#307292",relief="flat",font=("Arial", 12, 'bold'),padx=5)
        self.SaveButton.config(compound="left",background="#307292",relief="flat",font=("Arial", 12, 'bold'),padx=5)
        self.Title.config(background="#8ABFD9",fg = "#404040",pady="5")

        """ Widget Positions """

        self.Title.grid(row = 0,column = 0,columnspan = 3)
        self.lblPlayerName.grid(row = 1,column = 0)
        self.txtPlayer.grid(row = 1,column = 1 )
        self.getPlayerButton.grid(row= 1 , column = 2)
        self.lblTeamNumber.grid(row= 1,column = 4)
        self.txtTeamNumber.grid(row= 1 ,column =5)
        self.lblPlayer.grid(row = 2,column = 1)
        self.lblTeam.grid(row= 2,column = 3)
        self.PlayerList.grid(row = 3,column = 1)
        b.grid(row = 3,column = 2)
        self.TeamList.grid(row = 3 ,column = 3 )
        self.RemovePlayerButton.grid(row =3,column = 4)
        self.SaveButton.grid(row = 3,column = 5)
        self.BackButton.grid(row =1,column = 3)

class AddTeamPlayer(tk.Frame,AddTeam):
    """
    Methods:
        __init__
    Variables:
        controller

    """

    def __init__(self, parent, controller):
        """
        Initalises a frame instance of Add Team At Player Access Level
        """
        tk.Frame.__init__(self, parent)
        self.controller = controller

        """ Widget Declearations """

        """ Widget Stylings """

        """ Widget Positions """