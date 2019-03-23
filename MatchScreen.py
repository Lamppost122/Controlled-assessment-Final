import json
import tkinter as tk
from tkinter import font  as tkfont
from tkinter import messagebox
from tkinter import ttk
from Gui import *
import Config

class MatchScreen:

    def BackButtonRun(self):
        Config.PagesViewed.pop()
        self.controller.show_previous_frame(Config.PagesViewed[-1])


    def get_Team_Matches(self):
         TeamNumber = self.txtTeamNumber.get()
         Data = SystemToolKit.readFile(Config.MatchFile)
         TeamID = self.GetTeamID(TeamNumber)
         MatchData = Data[TeamID]

         for i ,j in enumerate(MatchData):
            MatchText = "Oposition: "+MatchData[j]["Opposition"] +"    Data: "+ MatchData[j]['Date']+"   Time: "+ MatchData[j]["Time"]+"   Location: "+ MatchData[j]["Location"]
            j = tk.Label(self,text = MatchText)
            j.grid(row = i+2 ,column = 0 ,columnspan=5)

    @staticmethod
    def GetTeamID(TeamNumber):
        Teams = SystemToolKit.readFile(Config.TeamFile)

        for i in Teams:
            if Teams[i]["Team Number"] == str(TeamNumber):

                return i

    def GetMyTeam(self):
        team = SystemToolKit.readFile(Config.TeamFile)

        for k,i in enumerate(team):
            for j in team[i]:
                if team[i][j] == str(Config.CurrentUser):
                    return i

    def GetMyMatches(self):
         TeamID = self.GetMyTeam()
         Data = SystemToolKit.readFile(Config.MatchFile)
         MatchData = Data[TeamID]

         for i ,j in enumerate(MatchData):
            MatchText = "Oposition: "+MatchData[j]["Opposition"] +"    Data: "+ MatchData[j]['Date']+"   Time: "+ MatchData[j]["Time"]+"   Location: "+ MatchData[j]["Location"]
            j = tk.Label(self,text = MatchText)
            j.grid(row = i+2 ,column = 0 ,columnspan=5)

class MatchScreenAdmin(tk.Frame,MatchScreen):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller

        """ Widget Declearations """

        self.Title = tk.Label(self,text = "Matchs" ,font = controller.title_font)
        self.lblTeam = tk.Label(self,text = "Team: ")
        self.txtTeamNumber = ttk.Entry(self)
        self.GetTeamMatchesButton = tk.Button(self,text = "Get Team Matches",command=self.get_Team_Matches)
        self.GetMyMatchesButton =tk.Button(self,text = "Get My Matches",command =lambda :self.GetMyMatches())
        self.ConfirmAvailablityButton =tk.Button(self,text = "Confirm Availablity",command = lambda:controller.show_frame("ConfirmAvailablity"))
        self.CheckAvailablityButton =tk.Button(self,text="Check Availablity",command = lambda:controller.show_frame("SendAvailablityCheck"))
        self.ViewAvailablityButton =tk.Button(self,text = "View Availability",command = lambda:controller.show_frame("ViewAvailablity"))
        self.BackButton= tk.Button(self, text="Back",command=lambda:self.BackButtonRun())
        self.MatchReportButton =tk.Button(self,text="Match Report",command = lambda:controller.show_frame("MatchReport") )

        """ Widget Stylings """

        self.lblTeam.config(justify="right",fg = "black",background="#8ABFD9",font=("Arial", 10, 'bold'))
        self.GetTeamMatchesButton.config(compound="left",background="#307292",relief="flat",font=("Arial", 12, 'bold'),padx=5)
        self.GetMyMatchesButton.config(compound="left",background="#307292",relief="flat",font=("Arial", 12, 'bold'),padx=5)
        self.ConfirmAvailablityButton.config(compound="left",background="#307292",relief="flat",font=("Arial", 12, 'bold'),padx=5)
        self.CheckAvailablityButton.config(compound="left",background="#307292",relief="flat",font=("Arial", 12, 'bold'),padx=5)
        self.ViewAvailablityButton.config(compound="left",background="#307292",relief="flat",font=("Arial", 12, 'bold'),padx=5)
        self.BackButton.config(compound="left",background="#307292",relief="flat",font=("Arial", 12, 'bold'),padx=5)
        self.MatchReportButton.config(compound="left",background="#307292",relief="flat",font=("Arial", 12, 'bold'),padx=5)
        self.Title.config(background="#8ABFD9",fg = "#404040",pady="5")

        """ Widget Positions """

        self.Title.grid(row = 0,column  =0)
        self.lblTeam.grid(row = 1,column  =0)
        self.txtTeamNumber.grid(row = 1,column  =1)
        self.GetTeamMatchesButton.grid(row = 1,column  =2)
        self.GetMyMatchesButton.grid(row = 1,column  =3)
        self.MatchReportButton.grid(row=1,column=4)
        self.BackButton.grid(row =1 ,column = 6)
        self.ConfirmAvailablityButton.grid(row=1,column = 5)
        self.CheckAvailablityButton.grid(row=2,column = 5)
        self.ViewAvailablityButton.grid(row=3,column =5)

class MatchScreenCoach(tk.Frame,MatchScreen):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller

        """ Widget Declearations """

        self.Title = tk.Label(self,text = "Matchs" ,font = controller.title_font)
        self.lblTeam = tk.Label(self,text = "Team: ")
        self.txtTeamNumber = ttk.Entry(self)
        self.GetTeamMatchesButton = tk.Button(self,text = "Get Team Matches",command=self.get_Team_Matches)
        self.GetMyMatchesButton =tk.Button(self,text = "Get My Matches",command =lambda :self.GetMyMatches())
        self.ConfirmAvailablityButton =tk.Button(self,text = "Confirm Availablity",command = lambda:controller.show_frame("ConfirmAvailablity"))
        self.CheckAvailablityButton =tk.Button(self,text="Check Availablity",command = lambda:controller.show_frame("SendAvailablityCheck"))
        self.ViewAvailablityButton =tk.Button(self,text = "View Availability",command = lambda:controller.show_frame("ViewAvailablity"))
        self.BackButton= tk.Button(self, text="Back",command=lambda:self.BackButtonRun())
        self.MatchReportButton =tk.Button(self,text="Match Report",command = lambda:controller.show_frame("MatchReport") )

        """ Widget Stylings """

        self.lblTeam.config(justify="right",fg = "black",background="#8ABFD9",font=("Arial", 10, 'bold'))
        self.GetTeamMatchesButton.config(compound="left",background="#307292",relief="flat",font=("Arial", 12, 'bold'),padx=5)
        self.GetMyMatchesButton.config(compound="left",background="#307292",relief="flat",font=("Arial", 12, 'bold'),padx=5)
        self.ConfirmAvailablityButton.config(compound="left",background="#307292",relief="flat",font=("Arial", 12, 'bold'),padx=5)
        self.CheckAvailablityButton.config(compound="left",background="#307292",relief="flat",font=("Arial", 12, 'bold'),padx=5)
        self.ViewAvailablityButton.config(compound="left",background="#307292",relief="flat",font=("Arial", 12, 'bold'),padx=5)
        self.BackButton.config(compound="left",background="#307292",relief="flat",font=("Arial", 12, 'bold'),padx=5)
        self.MatchReportButton.config(compound="left",background="#307292",relief="flat",font=("Arial", 12, 'bold'),padx=5)
        self.Title.config(background="#8ABFD9",fg = "#404040",pady="5")

        """ Widget Positions """

        self.Title.grid(row = 0,column  =0,columnspan = 6 )
        self.lblTeam.grid(row = 1,column  =0)
        self.txtTeamNumber.grid(row = 1,column  =1)
        self.GetTeamMatchesButton.grid(row = 1,column  =2)
        self.GetMyMatchesButton.grid(row = 1,column  =3)
        self.MatchReportButton.grid(row=1,column=4)
        self.BackButton.grid(row =1 ,column = 6)
        self.ConfirmAvailablityButton.grid(row=1,column = 5)
        self.CheckAvailablityButton.grid(row=2,column = 5)
        self.ViewAvailablityButton.grid(row=3,column =5)

class MatchScreenPlayer(tk.Frame,MatchScreen):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller

        """ Widget Declearations """

        self.Title = tk.Label(self,text = "Matchs" ,font = controller.title_font)
        self.lblTeam = tk.Label(self,text = "Team: ")
        self.txtTeamNumber = ttk.Entry(self)
        self.GetTeamMatchesButton = tk.Button(self,text = "Get Team Matches",command=self.get_Team_Matches)
        self.GetMyMatchesButton =tk.Button(self,text = "Get My Matches",command =lambda :self.GetMyMatches())
        self.ConfirmAvailablityButton =tk.Button(self,text = "Confirm Availablity",command = lambda:controller.show_frame("ConfirmAvailablity"))
        self.BackButton= tk.Button(self, text="Back",command=lambda:self.BackButtonRun())

        """ Widget Stylings """

        self.lblTeam.config(justify="right",fg = "black",background="#8ABFD9",font=("Arial", 10, 'bold'))
        self.GetTeamMatchesButton.config(compound="left",background="#307292",relief="flat",font=("Arial", 12, 'bold'),padx=5)
        self.GetMyMatchesButton.config(compound="left",background="#307292",relief="flat",font=("Arial", 12, 'bold'),padx=5)
        self.ConfirmAvailablityButton.config(compound="left",background="#307292",relief="flat",font=("Arial", 12, 'bold'),padx=5)
        self.CheckAvailablityButton.config(compound="left",background="#307292",relief="flat",font=("Arial", 12, 'bold'),padx=5)
        self.ViewAvailablityButton.config(compound="left",background="#307292",relief="flat",font=("Arial", 12, 'bold'),padx=5)
        self.BackButton.config(compound="left",background="#307292",relief="flat",font=("Arial", 12, 'bold'),padx=5)
        self.MatchReportButton.config(compound="left",background="#307292",relief="flat",font=("Arial", 12, 'bold'),padx=5)
        self.Title.config(background="#8ABFD9",fg = "#404040",pady="5")

        """ Widget Positions """

        self.Title.grid(row = 0,column  =0,columnspan = 6)
        self.lblTeam.grid(row = 1,column  =0)
        self.txtTeamNumber.grid(row = 1,column  =1)
        self.GetTeamMatchesButton.grid(row = 1,column  =2)
        self.GetMyMatchesButton.grid(row = 1,column  =3)
        self.MatchReportButton.grid(row=1,column=4)
        self.BackButton.grid(row =1 ,column = 6)
        self.ConfirmAvailablityButton.grid(row=1,column = 5)
        self.CheckAvailablityButton.grid(row=2,column = 5)
        self.ViewAvailablityButton.grid(row=3,column =5)
