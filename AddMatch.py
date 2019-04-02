import json
import tkinter as tk
from tkinter import font  as tkfont
from tkinter import messagebox
from tkinter import ttk
from Gui import *
import Config
from Validation import *
from SystemToolKit import *

class AddMatch:
    """
    Methods:
        AddMatch
        getTeamMatches
        getMatchData
    Variables:
        Team - Contains a team number
        Location - Contains a location
        Time- Contains a time
        Date - Contains a Date
        Opposition - Contains a opposition
    """


    def AddMatch(self):

        """
        Adds the current match on the screen to the Match File.
        Validates the following fields:
            Team Number
            Location
            Time
            Date
            Opposition
        Calls the Home Frame
        """

        self.getMatchData()
        data = {}

        if Validation.TeamNumber(self.Team)==True and Validation.Address(self.Location)==True and Validation.Time(self.Time) == True and Validation.Date(self.Date,"Future")== True and Validation.Opposition(self.Opposition)==True:

            match = SystemToolKit.readFile(Config.MatchFile)
            TeamId = SystemToolKit.getTeamId(self.Team)
            teamMatches = self.getTeamMatches(match,TeamId)
            matchID = str(uuid.uuid4())
            data["Opposition"] = self.Opposition
            data["Location"] = self.Location
            data["Time"] = self.Time
            data["Date"] = self.Date
            teamMatches[matchID] = data
            match[TeamId] = teamMatches

            with open(Config.MatchFile, 'w+') as fp:
                json.dump(match, fp)
            self.controller.show_frame("Home")



    def getTeamMatches(self,match,TeamId):
        """Searches a Match File for a teams matches and returns a Dict """
        for i in match :
            if i == TeamId :
                return match[TeamId]
        return {}

    def getMatchData(self):
        """
        Declares/Updates the Class Variables:
            Team
            Location
            Time
            Date
            Opposition
        To be equal to there on screen textboxes
             """
        self.Team =self.txtTeam.get()
        self.Location = self.txtLocation.get()
        self.Time = self.txtTime.get()
        self.Date = self.txtDate.get()
        self.Opposition = self.txtOpposition.get()



class AddMatchCoach(tk.Frame,AddMatch):
    """
    Methods:
        __init__
    Variables:
        controller
        Title - Title Label Widget
        lblTeam - Team Number Label Widget
        lblLocation - Location Label Widget
        lblTime - Time Label Widget
        lblDay - Day Label Widget
        lblOpposition - Opposition Label Widget
        txtTeam - Team Entry Widget
        txtLocation - Location Entry Widget
        txtTime - Time Entry Widget
        txtDate - Date Entry Widget
        txtOpposition - Opposition Entry Widget
        AddMatchButton - AddMatch Button Widget
        BackButton - Back Button Widget
        """
    def __init__(self, parent, controller):
        """
        Initalises a frame instance of Add Match At Coach Access Level
        """
        tk.Frame.__init__(self, parent)
        self.controller = controller

        """ Widget Declearations """

        self.Title = tk.Label(self,text = "Add Match" ,font = controller.title_font)
        self.lblTeam= tk.Label(self,text="Team: ")
        self.lblLocation =tk.Label(self,text="Location: ")
        self.lblTime = tk.Label(self,text="Time: ")
        self.lblDay = tk.Label(self,text="Day: ")
        self.lblOpposition = tk.Label(self,text="Opposition: ")
        self.txtTeam = ttk.Entry(self)
        self.txtLocation = ttk.Entry(self)
        self.txtTime = ttk.Entry(self)
        self.txtDate = ttk.Entry(self)
        self.txtOpposition = ttk.Entry(self)
        self.AddMatchButton = tk.Button(self,text="Add Match",command = lambda:self.AddMatch())
        self.BackButton= tk.Button(self, text="Back",command=lambda:SystemToolKit.BackButtonRun(controller))

        """ Widget Stylings """

        self.Title.config(background="#f4f8ff",fg = "#485e82",pady="5")
        self.Title.config(background="#8ABFD9",fg = "#404040",pady="5")
        self.lblTeam.config(justify="right",fg = "black",background="#8ABFD9",font=("Arial", 10, 'bold'))
        self.lblLocation.config(justify="right",fg = "black",background="#8ABFD9",font=("Arial", 10, 'bold'))
        self.lblTime.config(justify="right",fg = "black",background="#8ABFD9",font=("Arial", 10, 'bold'))
        self.lblDay.config(justify="right",fg = "black",background="#8ABFD9",font=("Arial", 10, 'bold'))
        self.lblOpposition.config(justify="right",fg = "black",background="#8ABFD9",font=("Arial", 10, 'bold'))
        self.AddMatchButton.config(compound="left",background="#307292",relief="flat",font=("Arial", 12, 'bold'),padx=5)
        self.BackButton.config(compound="left",background="#307292",relief="flat",font=("Arial", 12, 'bold'),padx=5)

        """ Widget Positions """

        self.Title.grid(row=0,column =0,columnspan = 2)
        self.lblTeam.grid(row=1,column=0)
        self.lblLocation.grid(row=2,column=0)
        self.lblTime.grid(row=3,column=0)
        self.lblDay.grid(row=4,column=0)
        self.lblOpposition.grid(row=5,column=0)
        self.txtTeam.grid(row = 1,column = 1)
        self.txtLocation.grid(row = 2,column = 1)
        self.txtTime.grid(row = 3,column = 1)
        self.txtDate.grid(row = 4,column = 1)
        self.txtOpposition.grid(row = 5,column = 1)
        self.AddMatchButton.grid(row = 6,column = 1 ,columnspan = 1 )
        self.BackButton.grid(row = 6,column = 0)


class AddMatchAdmin(tk.Frame,AddMatch):
    """
    Methods:
        __init__
    Variables:
        controller
        Title - Title Label Widget
        lblTeam - Team Number Label Widget
        lblLocation - Location Label Widget
        lblTime - Time Label Widget
        lblDay - Day Label Widget
        lblOpposition - Opposition Label Widget
        txtTeam - Team Entry Widget
        txtLocation - Location Entry Widget
        txtTime - Time Entry Widget
        txtDate - Date Entry Widget
        txtOpposition - Opposition Entry Widget
        AddMatchButton - AddMatch Button Widget
        BackButton - Back Button Widget
        """

    def __init__(self, parent, controller):
        """
        Initalises a frame instance of Add Match At Player Access Level
        """
        tk.Frame.__init__(self, parent)

        self.controller = controller

        """ Widget Declearations """

        self.Title = tk.Label(self,text = "Add Match" ,font = controller.title_font)
        self.lblTeam= tk.Label(self,text="Team: ")
        self.lblLocation =tk.Label(self,text="Location: ")
        self.lblTime = tk.Label(self,text="Time: ")
        self.lblDay = tk.Label(self,text="Day: ")
        self.lblOpposition = tk.Label(self,text="Opposition: ")
        self.txtTeam = ttk.Entry(self)
        self.txtLocation = ttk.Entry(self)
        self.txtTime = ttk.Entry(self)
        self.txtDate = ttk.Entry(self)
        self.txtOpposition = ttk.Entry(self)
        self.AddMatchButton = tk.Button(self,text="Add Match",command = lambda:self.AddMatch())
        self.BackButton= tk.Button(self, text="Back",command=lambda:SystemToolKit.BackButtonRun(controller))

        """ Widget Stylings """

        self.Title.config(background="#f4f8ff",fg = "#485e82",pady="5")
        self.Title.config(background="#8ABFD9",fg = "#404040",pady="5")
        self.lblTeam.config(justify="right",fg = "black",background="#8ABFD9",font=("Arial", 10, 'bold'))
        self.lblLocation.config(justify="right",fg = "black",background="#8ABFD9",font=("Arial", 10, 'bold'))
        self.lblTime.config(justify="right",fg = "black",background="#8ABFD9",font=("Arial", 10, 'bold'))
        self.lblDay.config(justify="right",fg = "black",background="#8ABFD9",font=("Arial", 10, 'bold'))
        self.lblOpposition.config(justify="right",fg = "black",background="#8ABFD9",font=("Arial", 10, 'bold'))
        self.AddMatchButton.config(compound="left",background="#307292",relief="flat",font=("Arial", 12, 'bold'),padx=5)
        self.BackButton.config(compound="left",background="#307292",relief="flat",font=("Arial", 12, 'bold'),padx=5)

        """ Widget Positions """

        self.Title.grid(row=0,column =0,columnspan = 2)
        self.lblTeam.grid(row=1,column=0)
        self.lblLocation.grid(row=2,column=0)
        self.lblTime.grid(row=3,column=0)
        self.lblDay.grid(row=4,column=0)
        self.lblOpposition.grid(row=5,column=0)
        self.txtTeam.grid(row = 1,column = 1)
        self.txtLocation.grid(row = 2,column = 1)
        self.txtTime.grid(row = 3,column = 1)
        self.txtDate.grid(row = 4,column = 1)
        self.txtOpposition.grid(row = 5,column = 1)
        self.AddMatchButton.grid(row = 6,column = 1 ,columnspan = 1 )
        self.BackButton.grid(row = 6,column = 0)

class AddMatchPlayer(tk.Frame,AddMatch):
    """
    Methods:
        __init__
    Variables:
        controller
        """

    def __init__(self, parent, controller):
        """
        Initalises a frame instance of Add Match At Player Access Level
        """
        tk.Frame.__init__(self, parent)

        self.controller = controller

        """ Widget Declearations """

        """ Widget Stylings """

        """ Widget Positions """