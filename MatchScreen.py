import json
import tkinter as tk
from tkinter import font  as tkfont
from tkinter import messagebox
from tkinter import ttk
from Gui import *
import Config
from Validation import *

class MatchScreen:
    """
    Methods:
        get_Team_Matches
        GetMyTeam
        GetMyMatches
    Variables:
         lblOpposition - Oppositon Label Widget
         lblDate - Date Label Widget
         lblTime - Time Label Widget
         lblLocation - Locatin Label Widget



    """

    def get_Team_Matches(self):
         """
         Adds a teams Matches to the screen
         """

         TeamNumber = self.txtTeamNumber.get()
         if Validation.TeamNumber(TeamNumber)==True:
             Data = SystemToolKit.readFile(Config.MatchFile)
             TeamID = SystemToolKit.getTeamId(TeamNumber)
             MatchData = Data[TeamID]
             try:

                 self.lblOpposition.grid_forget()
                 self.lblDate.grid_forget()
                 self.lblTime.grid_forget()
                 self.lblLocation.grid_forget()
             except AttributeError:
                pass

             """ Widget Declearations """


             self.lblOpposition = tk.Label(self,text="Opposition")
             self.lblDate =tk.Label(self,text="Date")
             self.lblTime =tk.Label(self,text="Time")
             self.lblLocation =tk.Label(self,text="Location")

             """ Widget Stylings """

             self.lblOpposition.config(justify="right",fg = "black",background="#8ABFD9",font=("Arial", 10, 'bold'))
             self.lblDate.config(justify="right",fg = "black",background="#8ABFD9",font=("Arial", 10, 'bold'))
             self.lblTime.config(justify="right",fg = "black",background="#8ABFD9",font=("Arial", 10, 'bold'))
             self.lblLocation.config(justify="right",fg = "black",background="#8ABFD9",font=("Arial", 10, 'bold'))

             """ Widget Positions """

             self.lblOpposition.grid(row = self.StartCount, column  =0 )
             self.lblDate.grid(row = self.StartCount, column  =1 )
             self.lblTime.grid(row = self.StartCount, column  =2 )
             self.lblLocation.grid(row = self.StartCount, column  =3 )

             for i ,j in enumerate(MatchData):

                """ Widget Declearations """


                self.lblOpposition = tk.Label(self,text="Opposition")
                self.lblDate =tk.Label(self,text="Date")
                self.lblTime =tk.Label(self,text="Time")
                self.lblLocation =tk.Label(self,text="Location")

                """ Widget Stylings """

                self.lblOpposition.config(justify="right",fg = "black",background="#8ABFD9",font=("Arial", 10, 'bold'),text=MatchData[j]["Opposition"])
                self.lblDate.config(justify="right",fg = "black",background="#8ABFD9",font=("Arial", 10, 'bold'),text=MatchData[j]['Date'])
                self.lblTime.config(justify="right",fg = "black",background="#8ABFD9",font=("Arial", 10, 'bold'),text=MatchData[j]["Time"])
                self.lblLocation.config(justify="right",fg = "black",background="#8ABFD9",font=("Arial", 10, 'bold'),text=MatchData[j]["Location"])

                """ Widget Positions """

                self.lblOpposition.grid(row = self.StartCount+i+1, column  =0 )
                self.lblDate.grid(row = self.StartCount+i+1, column  =1 )
                self.lblTime.grid(row = self.StartCount+i+1, column  =2 )
                self.lblLocation.grid(row = self.StartCount+i+1, column  =3 )





    def GetMyTeam(self):
        """returns the currrent users team id """
        team = SystemToolKit.readFile(Config.TeamFile)

        for k,i in enumerate(team):
            for j in team[i]:
                if team[i][j] == str(Config.CurrentUser):
                    return i

    def GetMyMatches(self):
         """
         Adds the current users Matches to the screen
         """
         TeamID = self.GetMyTeam()
         Data = SystemToolKit.readFile(Config.MatchFile)
         MatchData = Data[TeamID]

         try:
             self.lblOpposition.grid_forget()
             self.lblDate.grid_forget()
             self.lblTime.grid_forget()
             self.lblLocation.grid_forget()
         except AttributeError:
            pass

         """ Widget Declearations """


         self.lblOpposition = tk.Label(self,text="Opposition")
         self.lblDate =tk.Label(self,text="Date")
         self.lblTime =tk.Label(self,text="Time")
         self.lblLocation =tk.Label(self,text="Location")

         """ Widget Stylings """

         self.lblOpposition.config(justify="right",fg = "black",background="#8ABFD9",font=("Arial", 10, 'bold'))
         self.lblDate.config(justify="right",fg = "black",background="#8ABFD9",font=("Arial", 10, 'bold'))
         self.lblTime.config(justify="right",fg = "black",background="#8ABFD9",font=("Arial", 10, 'bold'))
         self.lblLocation.config(justify="right",fg = "black",background="#8ABFD9",font=("Arial", 10, 'bold'))

         """ Widget Positions """

         self.lblOpposition.grid(row = self.StartCount, column  =0 )
         self.lblDate.grid(row = self.StartCount, column  =1 )
         self.lblTime.grid(row = self.StartCount, column  =2 )
         self.lblLocation.grid(row = self.StartCount, column  =3 )

         for i ,j in enumerate(MatchData):

            """ Widget Declearations """


            self.lblOpposition = tk.Label(self,text="Opposition")
            self.lblDate =tk.Label(self,text="Date")
            self.lblTime =tk.Label(self,text="Time")
            self.lblLocation =tk.Label(self,text="Location")

            """ Widget Stylings """

            self.lblOpposition.config(justify="right",fg = "black",background="#8ABFD9",font=("Arial", 10, 'bold'),text=MatchData[j]["Opposition"])
            self.lblDate.config(justify="right",fg = "black",background="#8ABFD9",font=("Arial", 10, 'bold'),text=MatchData[j]['Date'])
            self.lblTime.config(justify="right",fg = "black",background="#8ABFD9",font=("Arial", 10, 'bold'),text=MatchData[j]["Time"])
            self.lblLocation.config(justify="right",fg = "black",background="#8ABFD9",font=("Arial", 10, 'bold'),text=MatchData[j]["Location"])

            """ Widget Positions """

            self.lblOpposition.grid(row = self.StartCount+i+1, column  =0 )
            self.lblDate.grid(row = self.StartCount+i+1, column  =1 )
            self.lblTime.grid(row = self.StartCount+i+1, column  =2 )
            self.lblLocation.grid(row = self.StartCount+i+1, column  =3 )






class MatchScreenAdmin(tk.Frame,MatchScreen):
    """
    Methods:
        __init__
    Variables:
        controller
        StartCount - Contains a integer that relates to the position of generated widgets during the run time
        Title - Title Label Widget
        lblTeam - Team Label Widget
        txtTeamNumber - Team Number Entry Widget
        GetTeamMatchesButton - Get Team Matches Button Widget
        GetMyMatchesButton  -  Get Current User Matches Button Widget
        ConfirmAvailablityButton - Confirm Availablity Button Widget
        CheckAvailablityButton - Check Availablity Button Widget
        ViewAvailablityButton  - View Availablity Button Widget
        BackButton - Back Button Widget
        MatchReportButton - Match Report Button Widget

    """

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.StartCount =2

        """ Widget Declearations """

        self.Title = tk.Label(self,text = "Matchs" ,font = controller.title_font)
        self.lblTeam = tk.Label(self,text = "Team: ")
        self.txtTeamNumber = ttk.Entry(self)
        self.GetTeamMatchesButton = tk.Button(self,text = "Get Team Matches",command=self.get_Team_Matches)
        self.GetMyMatchesButton =tk.Button(self,text = "Get My Matches",command =lambda :self.GetMyMatches())
        self.ConfirmAvailablityButton =tk.Button(self,text = "Confirm Availablity",command = lambda:controller.show_frame("ConfirmAvailablity"))
        self.CheckAvailablityButton =tk.Button(self,text="Check Availablity",command = lambda:controller.show_frame("SendAvailablityCheck"))
        self.ViewAvailablityButton =tk.Button(self,text = "View Availability",command = lambda:controller.show_frame("ViewAvailablity"))
        self.BackButton= tk.Button(self, text="Back",command=lambda:SystemToolKit.BackButtonRun(controller))
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
    """
    Methods:
        __init__
    Variables:
        controller
        StartCount - Contains a integer that relates to the position of generated widgets during the run time
        Title - Title Label Widget
        lblTeam - Team Label Widget
        txtTeamNumber - Team Number Entry Widget
        GetTeamMatchesButton - Get Team Matches Button Widget
        GetMyMatchesButton  -  Get Current User Matches Button Widget
        ConfirmAvailablityButton - Confirm Availablity Button Widget
        CheckAvailablityButton - Check Availablity Button Widget
        ViewAvailablityButton  - View Availablity Button Widget
        BackButton - Back Button Widget
        MatchReportButton - Match Report Button Widget

    """

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
        self.BackButton= tk.Button(self, text="Back",command=lambda:SystemToolKit.BackButtonRun(controller))
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
    """
    Methods:
        __init__
    Variables:
        controller
        StartCount - Contains a integer that relates to the position of generated widgets during the run time
        Title - Title Label Widget
        lblTeam - Team Label Widget
        txtTeamNumber - Team Number Entry Widget
        GetTeamMatchesButton - Get Team Matches Button Widget
        GetMyMatchesButton  -  Get Current User Matches Button Widget
        ConfirmAvailablityButton - Confirm Availablity Button Widget
        CheckAvailablityButton - Check Availablity Button Widget
        ViewAvailablityButton  - View Availablity Button Widget
        BackButton - Back Button Widget
        MatchReportButton - Match Report Button Widget

    """

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
        self.BackButton= tk.Button(self, text="Back",command=lambda:SystemToolKit.BackButtonRun(controller))

        """ Widget Stylings """

        self.lblTeam.config(justify="right",fg = "black",background="#8ABFD9",font=("Arial", 10, 'bold'))
        self.GetTeamMatchesButton.config(compound="left",background="#307292",relief="flat",font=("Arial", 12, 'bold'),padx=5)
        self.GetMyMatchesButton.config(compound="left",background="#307292",relief="flat",font=("Arial", 12, 'bold'),padx=5)
        self.ConfirmAvailablityButton.config(compound="left",background="#307292",relief="flat",font=("Arial", 12, 'bold'),padx=5)
        self.BackButton.config(compound="left",background="#307292",relief="flat",font=("Arial", 12, 'bold'),padx=5)
        self.Title.config(background="#8ABFD9",fg = "#404040",pady="5")

        """ Widget Positions """

        self.Title.grid(row = 0,column  =0,columnspan = 6)
        self.lblTeam.grid(row = 1,column  =0)
        self.txtTeamNumber.grid(row = 1,column  =1)
        self.GetTeamMatchesButton.grid(row = 1,column  =2)
        self.GetMyMatchesButton.grid(row = 1,column  =3)
        self.BackButton.grid(row =1 ,column = 6)
        self.ConfirmAvailablityButton.grid(row=1,column = 5)