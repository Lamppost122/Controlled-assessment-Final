import json
import tkinter as tk
from tkinter import font  as tkfont
from tkinter import messagebox
from tkinter import ttk
from Gui import *
from SystemToolKit import *
import datetime
from datetime import date
from SystemToolKit import *
import Config
class MatchReport:
    """
    Methods:
        AddPlayer
        RemovePlayers
        get_Match_Report_Data
        write_Match_Report
        getMatchID
        getPlayerID
        win_Status
        Match_Data
        Player_stats_update
        Player_Data
        seasonReset
        newSeason
        submit
        ImportTeam]
        get_Team
        Write_to_screen
    """


    def AddPlayer(self):
        """Adds a row to the match report """
        self.count +=1

        """ Widget Declearations """

        self.txtFirstName=ttk.Entry(self)
        self.txtLastName = ttk.Entry(self)
        self.txtGoal = ttk.Entry(self)
        self.txtGreen = ttk.Entry(self)
        self.txtYellow = ttk.Entry(self)
        self.txtRed = ttk.Entry(self)

        """ Widget Stylings """

        """ Widget Positions """

        self.txtFirstName.grid(row = self.count, column  =0 )
        self.txtLastName.grid(row = self.count,column = 1)
        self.txtGoal.grid(row = self.count, column  =2 )
        self.txtGreen.grid(row = self.count, column  =3 )
        self.txtYellow.grid(row = self.count, column  =4 )
        self.txtRed.grid(row = self.count, column  =5 )

    def RemovePlayer(self):
        """ Removes a row from the match report"""

        for label in self.grid_slaves():
            if int(label.grid_info()["row"]) > self.count-1 and self.count > self.StartCount :
                label.grid_forget()
        if self.count > self.StartCount:
            self.count-=1


    def get_Match_Report_Data(self):
        """ returns a matchReport(dict)"""
        data = []
        matchData = []
        matchReport = {}
        error = False

        for i,j in enumerate(self.grid_slaves()):
            if int(j.grid_info()["row"]) >= self.StartCount:

                try:

                    data.append(j.get())
                    if len(data) == 6 :


                        data =  list(reversed(data))
                        if Validation.Score(data[2]) ==True and Validation.FirstName(data[0])==True and Validation.LastName(data[1]) == True:

                            playerData = self.Player_Data(data[2],data[3],data[4],data[5])
                            player = self.getPlayerID(data[0],data[1])

                            matchReport[player] = playerData
                            data = []
                        else:
                            error = True


                except AttributeError:
                    pass
            else:
                try:

                    matchData.append(j.get())
                    if len(matchData) == 5:

                        if Validation.Date(matchData[3])==True and Validation.TeamNumber(matchData[4])==True and Validation.Score(matchData[2])==True and Validation.Score(matchData[1])==True:
                            matchID =self.getMatchID(matchData[3],matchData[4])
                            winStatus = self.win_Status(matchData[2],matchData[1])
                            matchData = self.Match_Data(matchID,matchData[2],matchData[1],winStatus)
                            matchReport["Match Data"] = matchData
                        else:
                            error =True

                except AttributeError:
                    pass
        if error == False:
            return matchReport
        else:
            return None

    def write_Match_Report(self,matchReport):
        """Writes a match report to the MatchReportFile """
        if matchReport != None:
            matchReportData = SystemToolKit.readFile(Config.MatchReportFile)
            matchReportID = str(uuid.uuid4())
            matchReportData[matchReportID] = matchReport
            with open(Config.MatchReportFile, 'w') as fp:
                    json.dump(matchReportData, fp)


    def getMatchID(self,Date,Team):
        """Returns a MatchId(string)"""

        matches = SystemToolKit.readFile(Config.MatchFile)

        TeamID =SystemToolKit.getTeamId(Team)
        for i in matches[TeamID]:
            if matches[TeamID][i]["Date"] ==  Date :
                return i

    def getPlayerID(self,FirstName,LastName):
        """Returns a PlayerId(string)"""

        players = SystemToolKit.readFile(Config.PlayerFile)
        for i in players:
            if players[i]["First name"] ==  FirstName and players[i]["Last name"] == LastName:
                return i

    def win_Status(self,ClubScore ,OppositonScore):
        """ Returns a MatchResult(string)"""
        if ClubScore > OppositonScore:
            return "Win"
        elif ClubScore == OppositonScore:
            return "Draw"
        else:
            return "Loss"

    def Match_Data( self,MatchID,ClubScore,OppositonScore,winStatus):
        """ returns Match Data(dict)"""

        matchData = {
        "matchID" : MatchID,
        "ClubScore" : ClubScore,
        "OppositionScore" : OppositonScore,
        "WinStatus" : winStatus
        }
        return matchData

    def Player_Data(self,Goal,GreenCards,YellowCards,RedCards):
        """returns player Data(dict)"""

        PlayerData = {
        "Goals": Goal,
        "Green cards": GreenCards,
        "Yellow cards": YellowCards,
        "Red Cards": RedCards
        }

        return PlayerData

    def Player_stats_update(self,matchReport):
        """Updates a player stats file """


        allPlayersData = SystemToolKit.readFile(Config.PlayerStatsFile)
        TeamID = SystemToolKit.getTeamId(self.txtTeam.get())
        try:
            playersData= allPlayersData[TeamID]

        except KeyError:
            playersData= {}
        if matchReport != None:
            for i in matchReport:
                if i!= "Match Data":
                    try:
                        playersData[i]["Life time goals"] += int(matchReport[i]["Goals"])
                        playersData[i]["Season goals"] += int(matchReport[i]["Goals"])
                        playersData[i]["Life time green cards"] += int(matchReport[i]["Green cards"])
                        playersData[i]["Season green cards"] += int(matchReport[i]["Green cards"])
                        playersData[i]["Life time yellow cards"] += int(matchReport[i]["Yellow cards"])
                        playersData[i]["Season yellow cards"] += int(matchReport[i]["Yellow cards"])
                        playersData[i]["Life time red cards"] += int(matchReport[i]["Red Cards"])
                        playersData[i]["Season red cards"] += int(matchReport[i]["Red Cards"])
                        playersData[i]["Life time Games"] +=1
                        playersData[i]["Season games"] += 1
                    except KeyError:
                        playersData[i] = {}
                        playersData[i]["Life time goals"] = int(matchReport[i]["Goals"])
                        playersData[i]["Season goals"] = int(matchReport[i]["Goals"])
                        playersData[i]["Life time green cards"] = int(matchReport[i]["Green cards"])
                        playersData[i]["Season green cards"] = int(matchReport[i]["Green cards"])
                        playersData[i]["Life time yellow cards"] = int(matchReport[i]["Yellow cards"])
                        playersData[i]["Season yellow cards"] = int(matchReport[i]["Yellow cards"])
                        playersData[i]["Life time red cards"] = int(matchReport[i]["Red Cards"])
                        playersData[i]["Season red cards"] = int(matchReport[i]["Red Cards"])
                        playersData[i]["Life time Games"] =1
                        playersData[i]["Season games"] = 1



            allPlayersData[TeamID] =playersData


            with open(Config.PlayerStatsFile, 'w+') as fp:
                        json.dump(allPlayersData, fp)

    def seasonReset(self):
        """resests all season records to 0 """

        playersData = SystemToolKit.readFile(Config.PlayerStatsFile)
        for data in playersData:
            data["Season goals"] = 0
            data["Season green cards"] = 0
            data["Season yellow cards"] = 0
            data["Season red cards"] = 0
            data["Season games"] = 0

        with open(Config.PlayerStatsFile, 'w+') as fp:
                    json.dump(playersData, fp)

    def newSeason(self):
        """Tests if a season reset is nessaccary """

        season = SystemToolKit.readFile(Config.SeasonFile)

        present =datetime.datetime.now()
        currentYear =present.year
        if datetime.datetime(currentYear,9,1) <present:
            self.seasonReset()
            currentYear +=1
        seasonData = "01/09/"+str(currentYear)
        with open(Config.SeasonFile, 'w+') as fp:
                    json.dump(seasonData, fp)


    def submit(self):
        """Calls newsseason,write_Match_Report,Player_stats_update """
        self.newSeason()
        matchReport = self.get_Match_Report_Data()
        if matchReport != None:
            self.write_Match_Report(matchReport)
            self.Player_stats_update(matchReport)
            messagebox.showinfo("","Match Report Submitted")
            self.controller.show_frame("Home")

    def ImportTeam(self):
        """Calls get_team and write_to_screen """
        teamNumber = self.txtImport.get()
        team = self.get_Team(teamNumber)
        self.Write_to_screen(team)


    def get_Team(self,teamNumber):
        """ returns a list of names"""
        team= SystemToolKit.readFile(Config.TeamFile)
        Players = SystemToolKit.readFile(Config.PlayerFile)

        Names = []
        for i, j in enumerate(team):
                if team[j]["Team Number"] == teamNumber:
                    for k,l in enumerate(team[j]):
                        if team[j][l] in Players:

                            Names.append([Players[team[j][l]]["First name"],Players[team[j][l]]["Last name"]])


        return Names

    def Write_to_screen(self,team):
        """Adds a team into the matchReport """

        Grid = []
        for i,j in enumerate(reversed(self.grid_slaves())):
            if int(j.grid_info()["row"]) >= self.StartCount and int(j.grid_info()["column"]) <=1 :
                if int(j.grid_info()["column"]) ==0:
                    FirstName = j
                else:
                    LastName = j
                    Grid.append([FirstName,LastName])

        FinalGrid = []
        for m,n in enumerate(Grid):
            if n[0].get() !="" or n[1].get() !="":
                pass
            else:
                FinalGrid.append(n)

        for q,p in enumerate(FinalGrid):
            if q < len(team):
                p[0].insert(0,team[q][0])
                p[1].insert(0,team[q][1])




class MatchReportAdmin(tk.Frame, MatchReport):
    """
    Methods:
        __init__
    Variables:
        controller
        count - Contains a integer that relates to the position of generated widgets during the run time
        StartCount - Contains a integer that relates to the position of generated widgets during the run time
        Title - Title Label Widget
        lblTeam - Team Label Widget
        lblDate - Date Label Widget
        lblImport - import Team Label Widget
        txtImport - Import Team Entry Widget
        txtTeam - Team Number Entry Widget
        txtDate - Date Entry Widget
        RemoveRowButton - Remove Row Button Widget
        AddRowButton - Add Row Button Widget
        SubmitButton - Submit Button Widget
        ImportButton - Import Team Button Widget
        BackButton - Back Buttoon Widget
        lblFirstName - First Name Heading Label Widget
        lblLastName - Last Name Heading Label Widget
        lblGoal - Goal Heading Label Widget
        lblGreenCard - Green Card Heading Label Widget
        lblYellowCard - Yellow Card Heading Label Widget
        lblRedCard - Red card Heading Label Widget
        lblScore - Score Heading Label Widget
        lblWhichurch - Whitchurch Score Label Widget
        lblOpposition - Opposition Core Label Widget
        WhichchurchScore - Whitchurch Score Entry Widget
        oppositionScore - Oppositon Score Entry Widget

    """

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.count = 5
        self.StartCount = self.count +1

        """ Widget Declearations """

        self.Title = tk.Label(self, text="Match Report", font=controller.title_font)
        self.lblTeam = tk.Label(self,text = "Team Number : ")
        self.lblDate = tk.Label(self,text = "Date :")
        self.lblImport = tk.Label(self,text = "Import Team:")
        self.txtImport = ttk.Entry(self)
        self.txtTeam = ttk.Entry(self)
        self.txtDate = ttk.Entry(self)
        self.RemoveRowButton = tk.Button(self,text="Remove row",command = self.RemovePlayer)
        self.AddRowButton = tk.Button(self,text = "Add Row",command= self.AddPlayer )
        self.SubmitButton = tk.Button(self,text = "Submit",command = self.submit)
        self.ImportButton = tk.Button(self,text="Import Team",command = lambda: self.ImportTeam())
        self.BackButton= tk.Button(self, text="Back",command=lambda:SystemToolKit.BackButtonRun(controller))
        self.lblFirstName = tk.Label(self,text = "FirstName")
        self.lblLastName = tk.Label(self,text = "Last Name")
        self.lblGoal = tk.Label(self,text="Goals")
        self.lblGreenCard = tk.Label(self,text="Green Card")
        self.lblYellowCard = tk.Label(self,text= "Yellow Card")
        self.lblRedCard = tk.Label(self,text= "Red Card")
        self.lblScore = tk.Label(self,text="Score: ")
        self.lblWhichurch =  tk.Label(self,text="Whitchchurch")
        self.lblOpposition = tk.Label(self,text = "Opposition")
        self.WhichchurchScore = ttk.Entry(self)
        self.oppositionScore = ttk.Entry(self)

        """ Widget Stylings """

        self.lblImport.config(justify="right",fg = "black",background="#8ABFD9",font=("Arial", 10, 'bold'))
        self.lblTeam.config(justify="right",fg = "black",background="#8ABFD9",font=("Arial", 10, 'bold'))
        self.lblDate.config(justify="right",fg = "black",background="#8ABFD9",font=("Arial", 10, 'bold'))
        self.RemoveRowButton.config(compound="left",background="#307292",relief="flat",font=("Arial", 10, 'bold'),padx=5)
        self.AddRowButton.config(compound="left",background="#307292",relief="flat",font=("Arial", 10, 'bold'),padx=5)
        self.SubmitButton.config(compound="left",background="#307292",relief="flat",font=("Arial", 10, 'bold'),padx=5)
        self.ImportButton.config(compound="left",background="#307292",relief="flat",font=("Arial", 10, 'bold'),padx=5)
        self.BackButton.config(compound="left",background="#307292",relief="flat",font=("Arial", 10, 'bold'),padx=5)
        self.lblFirstName.config(justify="right",fg = "black",background="#8ABFD9",font=("Arial", 10, 'bold'))
        self.lblLastName.config(justify="right",fg = "black",background="#8ABFD9",font=("Arial", 10, 'bold'))
        self.lblGoal.config(justify="right",fg = "black",background="#8ABFD9",font=("Arial", 10, 'bold'))
        self.lblGreenCard.config(justify="right",fg = "black",background="#8ABFD9",font=("Arial", 10, 'bold'))
        self.lblYellowCard.config(justify="right",fg = "black",background="#8ABFD9",font=("Arial", 10, 'bold'))
        self.lblRedCard.config(justify="right",fg = "black",background="#8ABFD9",font=("Arial", 10, 'bold'))
        self.lblScore.config(justify="right",fg = "black",background="#8ABFD9",font=("Arial", 10, 'bold'))
        self.lblWhichurch.config(justify="right",fg = "black",background="#8ABFD9",font=("Arial", 10, 'bold'))
        self.lblOpposition.config(justify="right",fg = "black",background="#8ABFD9",font=("Arial", 10, 'bold'))
        self.Title.config(background="#8ABFD9",fg = "#404040",pady="5")

        """ Widget Positiona """

        self.Title.grid(row = 0,column = 0,columnspan = 8)
        self.lblTeam.grid(row = 1, column = 0)
        self.lblDate.grid(row = 1, column = 2)
        self.txtTeam.grid(row = 1, column = 1)
        self.txtDate.grid(row = 1, column = 3)
        self.lblScore.grid(row = 3, column = 0)
        self.lblWhichurch.grid(row = 2, column = 1)
        self.lblOpposition.grid(row = 2, column = 2)
        self.WhichchurchScore.grid(row = 3, column = 1)
        self.oppositionScore.grid(row = 3, column = 2)
        self.lblFirstName.grid(row = 4, column = 0)
        self.lblLastName.grid(row= 4,column = 1)
        self.lblGoal.grid(row = 4, column =2)
        self.lblGreenCard.grid(row = 4 ,column  = 3)
        self.lblYellowCard.grid(row =4, column = 4)
        self.lblRedCard.grid(row= 4 ,column = 5 )
        self.AddRowButton.grid(row= 4,column = 6)
        self.RemoveRowButton.grid(row=4 ,column = 7)
        self.SubmitButton.grid(row =4 ,column =8)
        self.lblImport.grid(row=1,column = 4)
        self.txtImport.grid(row = 1,column = 5)
        self.ImportButton.grid(row=1,column= 6)
        self.AddPlayer()
        self.BackButton.grid(row =1,column = 7)

class MatchReportCoach(tk.Frame, MatchReport):
    """
    Methods:
        __init__
    Variables:
        controller
        count - Contains a integer that relates to the position of generated widgets during the run time
        StartCount - Contains a integer that relates to the position of generated widgets during the run time
        Title - Title Label Widget
        lblTeam - Team Label Widget
        lblDate - Date Label Widget
        lblImport - import Team Label Widget
        txtImport - Import Team Entry Widget
        txtTeam - Team Number Entry Widget
        txtDate - Date Entry Widget
        RemoveRowButton - Remove Row Button Widget
        AddRowButton - Add Row Button Widget
        SubmitButton - Submit Button Widget
        ImportButton - Import Team Button Widget
        BackButton - Back Buttoon Widget
        lblFirstName - First Name Heading Label Widget
        lblLastName - Last Name Heading Label Widget
        lblGoal - Goal Heading Label Widget
        lblGreenCard - Green Card Heading Label Widget
        lblYellowCard - Yellow Card Heading Label Widget
        lblRedCard - Red card Heading Label Widget
        lblScore - Score Heading Label Widget
        lblWhichurch - Whitchurch Score Label Widget
        lblOpposition - Opposition Core Label Widget
        WhichchurchScore - Whitchurch Score Entry Widget
        oppositionScore - Oppositon Score Entry Widget

    """

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.count = 5
        self.StartCount = self.count +1

        """ Widget Declearations """

        self.Title = tk.Label(self, text="Match Report", font=controller.title_font)
        self.lblTeam = tk.Label(self,text = "Team Number : ")
        self.lblDate = tk.Label(self,text = "Date :")
        self.lblImport = tk.Label(self,text = "Import Team:")
        self.txtImport = ttk.Entry(self)
        self.txtTeam = ttk.Entry(self)
        self.txtDate = ttk.Entry(self)
        self.RemoveRowButton = tk.Button(self,text="Remove row",command = self.RemovePlayer)
        self.AddRowButton = tk.Button(self,text = "Add Row",command= self.AddPlayer )
        self.SubmitButton = tk.Button(self,text = "Submit",command = self.submit)
        self.ImportButton = tk.Button(self,text="Import Team",command = lambda: self.ImportTeam())
        self.BackButton= tk.Button(self, text="Back",command=lambda:SystemToolKit.BackButtonRun(controller))
        self.lblFirstName = tk.Label(self,text = "FirstName")
        self.lblLastName = tk.Label(self,text = "Last Name")
        self.lblGoal = tk.Label(self,text="Goals")
        self.lblGreenCard = tk.Label(self,text="Green Card")
        self.lblYellowCard = tk.Label(self,text= "Yellow Card")
        self.lblRedCard = tk.Label(self,text= "Red Card")
        self.lblScore = tk.Label(self,text="Score: ")
        self.lblWhichurch =  tk.Label(self,text="Whitchchurch")
        self.lblOpposition = tk.Label(self,text = "Opposition")
        self.WhichchurchScore = ttk.Entry(self)
        self.oppositionScore = ttk.Entry(self)

        """ Widget Stylings """

        self.lblImport.config(justify="right",fg = "black",background="#8ABFD9",font=("Arial", 10, 'bold'))
        self.lblTeam.config(justify="right",fg = "black",background="#8ABFD9",font=("Arial", 10, 'bold'))
        self.lblDate.config(justify="right",fg = "black",background="#8ABFD9",font=("Arial", 10, 'bold'))
        self.RemoveRowButton.config(compound="left",background="#307292",relief="flat",font=("Arial", 10, 'bold'),padx=5)
        self.AddRowButton.config(compound="left",background="#307292",relief="flat",font=("Arial", 10, 'bold'),padx=5)
        self.SubmitButton.config(compound="left",background="#307292",relief="flat",font=("Arial", 10, 'bold'),padx=5)
        self.ImportButton.config(compound="left",background="#307292",relief="flat",font=("Arial", 10, 'bold'),padx=5)
        self.BackButton.config(compound="left",background="#307292",relief="flat",font=("Arial", 10, 'bold'),padx=5)
        self.lblFirstName.config(justify="right",fg = "black",background="#8ABFD9",font=("Arial", 10, 'bold'))
        self.lblLastName.config(justify="right",fg = "black",background="#8ABFD9",font=("Arial", 10, 'bold'))
        self.lblGoal.config(justify="right",fg = "black",background="#8ABFD9",font=("Arial", 10, 'bold'))
        self.lblGreenCard.config(justify="right",fg = "black",background="#8ABFD9",font=("Arial", 10, 'bold'))
        self.lblYellowCard.config(justify="right",fg = "black",background="#8ABFD9",font=("Arial", 10, 'bold'))
        self.lblRedCard.config(justify="right",fg = "black",background="#8ABFD9",font=("Arial", 10, 'bold'))
        self.lblScore.config(justify="right",fg = "black",background="#8ABFD9",font=("Arial", 10, 'bold'))
        self.lblWhichurch.config(justify="right",fg = "black",background="#8ABFD9",font=("Arial", 10, 'bold'))
        self.lblOpposition.config(justify="right",fg = "black",background="#8ABFD9",font=("Arial", 10, 'bold'))
        self.Title.config(background="#8ABFD9",fg = "#404040",pady="5")

        """ Widget Positions """

        self.Title.grid(row = 0,column = 0,columnspan = 8)
        self.lblTeam.grid(row = 1, column = 0)
        self.lblDate.grid(row = 1, column = 2)
        self.txtTeam.grid(row = 1, column = 1)
        self.txtDate.grid(row = 1, column = 3)
        self.lblScore.grid(row = 3, column = 0)
        self.lblWhichurch.grid(row = 2, column = 1)
        self.lblOpposition.grid(row = 2, column = 2)
        self.WhichchurchScore.grid(row = 3, column = 1)
        self.oppositionScore.grid(row = 3, column = 2)
        self.lblFirstName.grid(row = 4, column = 0)
        self.lblLastName.grid(row= 4,column = 1)
        self.lblGoal.grid(row = 4, column =2)
        self.lblGreenCard.grid(row = 4 ,column  = 3)
        self.lblYellowCard.grid(row =4, column = 4)
        self.lblRedCard.grid(row= 4 ,column = 5 )
        self.AddRowButton.grid(row= 4,column = 6)
        self.RemoveRowButton.grid(row=4 ,column = 7)
        self.SubmitButton.grid(row =4 ,column =8)
        self.lblImport.grid(row=1,column = 4)
        self.txtImport.grid(row = 1,column = 5)
        self.ImportButton.grid(row=1,column= 6)
        self.AddPlayer()
        self.BackButton.grid(row =1,column = 7)

class MatchReportPlayer(tk.Frame, MatchReport):
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