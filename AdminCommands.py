import json
import tkinter as tk
from tkinter import font  as tkfont
from tkinter import messagebox
from tkinter import ttk
from Gui import *
import Config

class AdminCommands:

    def BackButtonRun(self):
            Config.PagesViewed.pop()
            self.controller.show_previous_frame(Config.PagesViewed[-1])

class AdminCommandsAdmin(tk.Frame,AdminCommands):

        def __init__(self, parent, controller):
            tk.Frame.__init__(self, parent)
            self.controller = controller

            """ Widget Declearations """

            self.Title =tk.Label(self,text="Admins commands",font = controller.title_font)
            self.lblplayer = tk.Label(self,text = "Player tools")
            self.lblMatches =tk.Label(self,text = "Match tools")
            self.lblTeam =tk.Label(self,text = "Team tools")
            self.lblUpdates = tk.Label(self,text = "Update/news tools")
            self.lblBackUp = tk.Label(self,text = "Back Ups")
            self.RemovePlayerButton = tk.Button(self,text="Remove player",command = lambda: controller.show_frame("RemovePlayer"))
            self.EditPlayerButton = tk.Button(self,text="Edit player",command = lambda: controller.show_frame("EditPlayer"))
            self.AddMatchButton = tk.Button(self,text="Add Match",command = lambda: controller.show_frame("AddMatch"))
            self.RemoveMatchButton = tk.Button(self,text="Remove Match",command = lambda: controller.show_frame("RemoveMatch"))
            self.EditMatchButton = tk.Button(self,text="Edit Match",command = lambda: controller.show_frame("EditMatch"))
            self.AddTeamButton = tk.Button(self,text="Add Team",command = lambda: controller.show_frame("AddTeam"))
            self.RemoveTeamButton = tk.Button(self,text="Remove Team",command = lambda: controller.show_frame("RemoveTeam"))
            self.EditTeamButton = tk.Button(self,text="Edit Team",command = lambda: controller.show_frame("EditTeam"))
            self.AddUpdateButton = tk.Button(self,text="Add Update",command = lambda: controller.show_frame("AddNews"))
            self.BackUpButton = tk.Button(self,text="BackUp",command = lambda: controller.show_frame("BackUp"))
            self.BackButton= tk.Button(self, text="Back",command=lambda:self.BackButtonRun())
            self.ImportDataButton = tk.Button(self,text="Import Data",command = lambda: controller.show_frame("ImportData"))
            self.lblImportData = tk.Label(self,text="Import Data")

            """ Widget Stlyings """

            self.Title.config(background="#8ABFD9",fg = "#404040",pady="5")
            self.lblplayer.config(justify="right",fg = "black",background="#8ABFD9",font=("Arial", 10, 'bold'))
            self.lblMatches.config(justify="right",fg = "black",background="#8ABFD9",font=("Arial", 10, 'bold'))
            self.lblTeam.config(justify="right",fg = "black",background="#8ABFD9",font=("Arial", 10, 'bold'))
            self.lblUpdates.config(justify="right",fg = "black",background="#8ABFD9",font=("Arial", 10, 'bold'))
            self.RemovePlayerButton.config(width="15",compound="left",background="#307292",relief="flat",font=("Arial", 10, 'bold'),padx=5)
            self.EditPlayerButton.config(width="15",compound="left",background="#307292",relief="flat",font=("Arial", 10, 'bold'),padx=5)
            self.AddMatchButton.config(width="15",compound="left",background="#307292",relief="flat",font=("Arial", 10, 'bold'),padx=5)
            self.RemoveMatchButton.config(width="15",compound="left",background="#307292",relief="flat",font=("Arial", 10, 'bold'),padx=5)
            self.EditMatchButton.config(width="15",compound="left",background="#307292",relief="flat",font=("Arial", 10, 'bold'),padx=5)
            self.AddTeamButton.config(width="15",compound="left",background="#307292",relief="flat",font=("Arial", 10, 'bold'),padx=5)
            self.RemoveTeamButton.config(width="15",compound="left",background="#307292",relief="flat",font=("Arial", 10, 'bold'),padx=5)
            self.EditTeamButton.config(width="15",compound="left",background="#307292",relief="flat",font=("Arial", 10, 'bold'),padx=5)
            self.AddUpdateButton.config(width="15",compound="left",background="#307292",relief="flat",font=("Arial", 10, 'bold'),padx=5)
            self.BackUpButton.config(width="15",compound="left",background="#307292",relief="flat",font=("Arial", 10, 'bold'),padx=5)
            self.BackButton.config(width="15",compound="left",background="#307292",relief="flat",font=("Arial", 10, 'bold'),padx=5)
            self.lblBackUp.config(justify="right",fg = "black",background="#8ABFD9",font=("Arial", 10, 'bold'))
            self.ImportDataButton.config(width="15",compound="left",background="#307292",relief="flat",font=("Arial", 10, 'bold'),padx=5)
            self.lblImportData.config(justify="right",fg = "black",background="#8ABFD9",font=("Arial", 10, 'bold'))

            """ Widget Positions """

            self.Title.grid(row=0,column = 0,columnspan = 4)
            self.lblplayer.grid(row=1,column = 0)
            self.lblMatches.grid(row=1,column = 1)
            self.lblTeam .grid(row=1,column = 2)
            self.lblUpdates.grid(row=1,column = 3)
            self.lblBackUp.grid(row=1,column=4)
            self.RemovePlayerButton.grid(row=2,column = 0)
            self.EditPlayerButton.grid(row=3,column = 0)
            self.AddMatchButton.grid(row=2,column = 1)
            self.RemoveMatchButton.grid(row=3,column = 1)
            self.EditMatchButton.grid(row=4,column = 1)
            self.AddTeamButton.grid(row=2,column = 2)
            self.RemoveTeamButton.grid(row=3,column = 2)
            self.EditTeamButton.grid(row=4,column = 2)
            self.AddUpdateButton.grid(row=2,column = 3)
            self.BackUpButton.grid(row=2,column =4)
            self.BackButton.grid(row =1,column = 6)
            self.ImportDataButton.grid(row=2,column= 5)
            self.lblImportData.grid(row=1,column= 5)

class AdminCommandsCoach(tk.Frame,AdminCommands):

        def __init__(self, parent, controller):
            tk.Frame.__init__(self, parent)
            self.controller = controller

            """ Widget Declearations """

            self.Title =tk.Label(self,text="Admins commands",font = controller.title_font)
            self.lblplayer = tk.Label(self,text = "Player tools")
            self.lblMatches =tk.Label(self,text = "Match tools")
            self.lblTeam =tk.Label(self,text = "Team tools")
            self.RemovePlayerButton = tk.Button(self,text="Remove player",command = lambda: controller.show_frame("RemovePlayer"))
            self.EditPlayerButton = tk.Button(self,text="Edit player",command = lambda: controller.show_frame("EditPlayer"))
            self.AddMatchButton = tk.Button(self,text="Add Match",command = lambda: controller.show_frame("AddMatch"))
            self.RemoveMatchButton = tk.Button(self,text="Remove Match",command = lambda: controller.show_frame("RemoveMatch"))
            self.EditMatchButton = tk.Button(self,text="Edit Match",command = lambda: controller.show_frame("EditMatch"))
            self.AddTeamButton = tk.Button(self,text="Add Team",command = lambda: controller.show_frame("AddTeam"))
            self.RemoveTeamButton = tk.Button(self,text="Remove Team",command = lambda: controller.show_frame("RemoveTeam"))
            self.EditTeamButton = tk.Button(self,text="Edit Team",command = lambda: controller.show_frame("EditTeam"))
            self.BackButton= tk.Button(self, text="Back",command=lambda:self.BackButtonRun())

            """ Widget Stylings """

            self.Title.config(background="#8ABFD9",fg = "#404040",pady="5")
            self.lblplayer.config(justify="right",fg = "black",background="#8ABFD9",font=("Arial", 10, 'bold'))
            self.lblMatches.config(justify="right",fg = "black",background="#8ABFD9",font=("Arial", 10, 'bold'))
            self.lblTeam.config(justify="right",fg = "black",background="#8ABFD9",font=("Arial", 10, 'bold'))
            self.RemovePlayerButton.config(width="15",compound="left",background="#307292",relief="flat",font=("Arial", 10, 'bold'),padx=5)
            self.EditPlayerButton.config(width="15",compound="left",background="#307292",relief="flat",font=("Arial", 10, 'bold'),padx=5)
            self.AddMatchButton.config(width="15",compound="left",background="#307292",relief="flat",font=("Arial", 10, 'bold'),padx=5)
            self.RemoveMatchButton.config(width="15",compound="left",background="#307292",relief="flat",font=("Arial", 10, 'bold'),padx=5)
            self.EditMatchButton.config(width="15",compound="left",background="#307292",relief="flat",font=("Arial", 10, 'bold'),padx=5)
            self.AddTeamButton.config(width="15",compound="left",background="#307292",relief="flat",font=("Arial", 10, 'bold'),padx=5)
            self.RemoveTeamButton.config(width="15",compound="left",background="#307292",relief="flat",font=("Arial", 10, 'bold'),padx=5)
            self.EditTeamButton.config(width="15",compound="left",background="#307292",relief="flat",font=("Arial", 10, 'bold'),padx=5)
            self.BackButton.config(width="15",compound="left",background="#307292",relief="flat",font=("Arial", 10, 'bold'),padx=5)

            """ Widget Positions """

            self.Title.grid(row=0,column = 0,columnspan = 4)
            self.lblplayer.grid(row=1,column = 0)
            self.lblMatches.grid(row=1,column = 1)
            self.lblTeam .grid(row=1,column = 2)
            self.RemovePlayerButton.grid(row=2,column = 0)
            self.EditPlayerButton.grid(row=3,column = 0)
            self.AddMatchButton.grid(row=2,column = 1)
            self.RemoveMatchButton.grid(row=3,column = 1)
            self.EditMatchButton.grid(row=4,column = 1)
            self.AddTeamButton.grid(row=2,column = 2)
            self.RemoveTeamButton.grid(row=3,column = 2)
            self.EditTeamButton.grid(row=4,column = 2)
            self.BackButton.grid(row =1,column = 6)

class AdminCommandsPlayer(tk.Frame,AdminCommands):

        def __init__(self, parent, controller):
            tk.Frame.__init__(self, parent)
            self.controller = controller

            """ Widget Declearations """

            """ Widget Stylings """

            """ Widget Positions """