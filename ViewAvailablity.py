import json
import tkinter as tk
from tkinter import font  as tkfont
from tkinter import messagebox
from tkinter import ttk
from Gui import *
from Config import *
from SystemToolKit import *
from SystemToolKit import *

class ViewAvailablity:

        def BackButtonRun(self):
            Config.PagesViewed.pop()
            self.controller.show_previous_frame(Config.PagesViewed[-1])

        def GetPlayers(self):
            if Validation.TeamNumber(self.txtTeamNumber.get()) == True:
                matchPlayers = SystemToolKit.readFile(Config.MatchAvailablityFile)
                players = SystemToolKit.readFile(Config.PlayerFile)
                match =SystemToolKit.readFile(Config.MatchFile)


                TeamID = SystemToolKit.getTeamId(self.txtTeamNumber.get())
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

            """ Widget Declearations """

            self.Title=tk.Label(self,text="Player Availablity",font=controller.title_font)
            self.lblTeamNumber = tk.Label(self,text="Team Number: ")
            self.txtTeamNumber = ttk.Entry(self)
            self.GetPlayersButton =tk.Button(self,text="Get Player Status",command=lambda:self.GetPlayers())
            self.BackButton= tk.Button(self, text="Back",command=lambda:SystemToolKit.BackButtonRun(controller))

            """ Widget Stylings """

            self.lblTeamNumber.config(justify="right",fg = "black",background="#8ABFD9",font=("Arial", 10, 'bold'))
            self.GetPlayersButton.config(compound="left",background="#307292",relief="flat",font=("Arial", 10, 'bold'),padx=5)
            self.Title.config(background="#8ABFD9",fg = "#404040",pady="5")
            self.BackButton.config(compound="left",background="#307292",relief="flat",font=("Arial", 10, 'bold'),padx=5)

            """ Widget Positions """

            self.Title.grid(row=0,column =0)
            self.lblTeamNumber.grid(row=1,column=0)
            self.txtTeamNumber.grid(row=1,column =1)
            self.GetPlayersButton.grid(row=1,column =2)
            self.BackButton.grid(row=1,column=3)

class ViewAvailablityCoach(tk.Frame,ViewAvailablity):

        def __init__(self, parent, controller):
            tk.Frame.__init__(self, parent)
            self.controller = controller

            """ Widget Declearations """

            self.Title=tk.Label(self,text="Player Availablity",font=controller.title_font)
            self.lblTeamNumber = tk.Label(self,text="Team Number: ")
            self.txtTeamNumber = ttk.Entry(self)
            self.GetPlayersButton =tk.Button(self,text="Get Player Status",command=lambda:self.GetPlayers())
            self.BackButton= tk.Button(self, text="Back",command=lambda:SystemToolKit.BackButtonRun(controller))

            """ Widget Stylings """

            self.lblTeamNumber.config(justify="right",fg = "black",background="#8ABFD9",font=("Arial", 10, 'bold'))
            self.GetPlayersButton.config(compound="left",background="#307292",relief="flat",font=("Arial", 10, 'bold'),padx=5)
            self.Title.config(background="#8ABFD9",fg = "#404040",pady="5")
            self.BackButton.config(compound="left",background="#307292",relief="flat",font=("Arial", 10, 'bold'),padx=5)

            """ Widget Positions """

            self.Title.grid(row=0,column =0)
            self.lblTeamNumber.grid(row=1,column=0)
            self.txtTeamNumber.grid(row=1,column =1)
            self.GetPlayersButton.grid(row=1,column =2)
            self.BackButton.grid(row=1,column=3)

class ViewAvailablityPlayer(tk.Frame,ViewAvailablity):

        def __init__(self, parent, controller):
            tk.Frame.__init__(self, parent)
            self.controller = controller

            """ Widget Declearations """

            """ Widget Stylings """

            """ Widget Positions """
