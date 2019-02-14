import json
import tkinter as tk
from tkinter import font  as tkfont
from tkinter import messagebox
from tkinter import ttk
from Gui import *
from Config import *

class ConfirmAvailablity(tk.Frame):

        def __init__(self, parent, controller):
            tk.Frame.__init__(self, parent)
            self.controller = controller
            self.Title =tk.Label(self,text="Confirm Availablity",font=controller.title_font)
            self.GetMyMatchesButton = tk.Button(self,text="Get My Matches",command = lambda:self.GetMyMatches)

        def GetMyMatches(self):
            Players = SystemToolKit.readFile("players.json")
            Team = SystemToolKit.readFile("teams.json")
            TeamID = Team[Players[Config.CurrentUser]["Team"]]
            AvailableMatches = SystemToolKit.readFile("matchAvailablity.json")
            MyMatches = AvailableMatches[TeamID]

