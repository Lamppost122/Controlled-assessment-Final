import json
import tkinter as tk
from tkinter import font  as tkfont
from tkinter import messagebox
from tkinter import ttk
from Gui import *
import Config

class RemovePlayer:
    """
    Methods:
        GetPlayer
        RemovePlayer
    Variables:
        allPlayers - Contains a instance of the player file
        orderedList - contains player ids


    """

    def GetPlayer(self):
        """Adds players to the orderedList Lsit and the Player List onscreen """

        self.PlayerList.delete(0,tk.END)
        data =self.txtPlayer.get()
        data = data.lower()
        self.allPlayers = SystemToolKit.readFile(Config.PlayerFile)
        self.orderedList = []

        for i,j in enumerate(self.allPlayers):
            if self.allPlayers[j]["First name"].lower() == data or self.allPlayers[j]["Last name"].lower() == data or self.allPlayers[j]["First name"].lower() + " " + self.allPlayers[j]["Last name"].lower() == data:

                self.orderedList.append(j)
                text = str(self.allPlayers[j]["First name"]) + " " + str(self.allPlayers[j]["Last name"])
                self.PlayerList.insert(tk.END,text)

    def RemovePlayer(self):
        """ Remove a player from the system """
        self.allPlayers.pop(self.orderedList[self.PlayerList.index(tk.ANCHOR)], None)
        self.PlayerList.delete(tk.ANCHOR)

        with open(Config.PlayerFile,"w+")as fp:
            json.dump(self.allPlayers,fp)

class RemovePlayerAdmin(tk.Frame,RemovePlayer):
    """
    Methods:
        __init__

    Variables:
        controller
        Title - Title Label Widget
        lblPlayer - player Label Widget
        txtPlayer - Player Entry Widget
        getPlayerButton - Get Player button Widget
        PlayerList - Player Listbox Widget
        RemovePlayerButton - Remove Player Button Widget
        BackButton - Back Button Widget

    """

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller

        """ Widget Declearations """

        self.Title = tk.Label(self,text = "Remove Player" ,font = controller.title_font)
        self.lblPlayer = tk.Label(self,text = "Player Name: ")
        self.txtPlayer = ttk.Entry(self)
        self.getPlayerButton = tk.Button(self,text = "Get Player",command = self.GetPlayer)
        self.PlayerList = tk.Listbox(self)
        self.RemovePlayerButton= tk.Button(self, text="Remove  Player",command=self.RemovePlayer )
        self.BackButton= tk.Button(self, text="Back",command=lambda:SystemToolKit.BackButtonRun(controller))

        """ Widget Stylings """

        self.lblPlayer.config(justify="right",fg = "black",background="#8ABFD9",font=("Arial", 10, 'bold'))
        self.getPlayerButton.config(compound="left",background="#307292",relief="flat",font=("Arial", 12, 'bold'),padx=5)
        self.RemovePlayerButton.config(compound="left",background="#307292",relief="flat",font=("Arial", 12, 'bold'),padx=5)
        self.BackButton.config(compound="left",background="#307292",relief="flat",font=("Arial", 12, 'bold'),padx=5)
        self.Title.config(background="#8ABFD9",fg = "#404040",pady="5")

        """ Widget Positions """

        self.RemovePlayerButton.grid(row = 2,column = 4)
        self.Title.grid(row = 0,column = 0,columnspan = 3)
        self.lblPlayer.grid(row = 1,column = 0)
        self.txtPlayer.grid(row = 1,column = 1 )
        self.getPlayerButton.grid(row= 1 , column = 2)
        self.PlayerList.grid(row = 2,column = 0,columnspan = 3)
        self.BackButton.grid(row =2,column = 3)

class RemovePlayerPlayer(tk.Frame,RemovePlayer):
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

class RemovePlayerCoach(tk.Frame,RemovePlayer):
    """
    Methods:
        __init__

    Variables:
        controller
        Title - Title Label Widget
        lblPlayer - player Label Widget
        txtPlayer - Player Entry Widget
        getPlayerButton - Get Player button Widget
        PlayerList - Player Listbox Widget
        RemovePlayerButton - Remove Player Button Widget
        BackButton - Back Button Widget

    """


    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller

        """ Widget Declearations """

        self.Title = tk.Label(self,text = "Remove Player" ,font = controller.title_font)
        self.lblPlayer = tk.Label(self,text = "Player Name: ")
        self.txtPlayer = ttk.Entry(self)
        self.getPlayerButton = tk.Button(self,text = "Get Player",command = self.GetPlayer)
        self.PlayerList = tk.Listbox(self)
        self.RemovePlayerButton = tk.Button(self, text="Remove  Player",command=self.RemovePlayer )
        self.BackButton= tk.Button(self, text="Back",command=lambda:SystemToolKit.BackButtonRun(controller))

        """ Widget Stylings """

        self.lblPlayer.config(justify="right",fg = "black",background="#8ABFD9",font=("Arial", 10, 'bold'))
        self.getPlayerButton.config(compound="left",background="#307292",relief="flat",font=("Arial", 12, 'bold'),padx=5)
        self.RemovePlayerButton.config(compound="left",background="#307292",relief="flat",font=("Arial", 12, 'bold'),padx=5)
        self.BackButton.config(compound="left",background="#307292",relief="flat",font=("Arial", 12, 'bold'),padx=5)
        self.Title.config(background="#8ABFD9",fg = "#404040",pady="5")

        """ Widget Positons """

        self.RemovePlayerButton.grid(row = 2,column = 4)
        self.Title.grid(row = 0,column = 0,columnspan = 3)
        self.lblPlayer.grid(row = 1,column = 0)
        self.txtPlayer.grid(row = 1,column = 1 )
        self.getPlayerButton.grid(row= 1 , column = 2)
        self.PlayerList.grid(row = 2,column = 0,columnspan = 3)
        self.BackButton.grid(row =2,column = 3)