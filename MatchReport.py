import json
import tkinter as tk
from tkinter import font  as tkfont
from tkinter import messagebox
from tkinter import ttk
from Gui import *

class MatchReport(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.count = 5
        self.StartCount = self.count +1
        self.Title = tk.Label(self, text="Match Report", font=controller.title_font)
        self.lblTeam = ttk.Label(self,text = "Team Number : ")
        self.lblDate = ttk.Label(self,text = "Date :")
        self.lblImport = ttk.Label(self,text = "Import Team:")
        self.txtImport = ttk.Entry(self)
        self.txtTeam = ttk.Entry(self)
        self.txtDate = ttk.Entry(self)
        self.RemoveRowButton = tk.Button(self,text="Remove row",command = self.RemovePlayer)
        self.AddRowButton = tk.Button(self,text = "Add Row",command= self.AddPlayer )
        self.SubmitButton = tk.Button(self,text = "Submit",command = self.submit)
        self.ImportButton = tk.Button(self,text="Import Team",command = self.ImportTeam)
        self.BackButton= tk.Button(self, text="Back",command=lambda:self.BackButtonRun(controller))
        self.lblFirstName = ttk.Label(self,text = "FirstName")
        self.lblLastName = ttk.Label(self,text = "Last Name")
        self.lblGoal = ttk.Label(self,text="Goals")
        self.lblGreenCard = ttk.Label(self,text="Green Card")
        self.lblYellowCard = ttk.Label(self,text= "Yellow Card")
        self.lblRedCard = ttk.Label(self,text= "Red Card")
        self.lblScore = ttk.Label(self,text="Score: ")
        self.lblWhichurch =  ttk.Label(self,text="Whitchchurch")
        self.lblOpposition = ttk.Label(self,text = "Opposition")
        self.WhichchurchScore = ttk.Entry(self)
        self.oppositionScore = ttk.Entry(self)
        self.Title.config(background="#f4f8ff",fg = "#485e82",pady="5")
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


    def BackButtonRun(self,controller):
            global PagesViewed
            PagesViewed.pop()
            controller.show_frame(PagesViewed[-1])



    def AddPlayer(self):
        self.count +=1
        self.txtFirstName=ttk.Entry(self)
        self.txtLastName = ttk.Entry(self)
        self.txtGoal = ttk.Entry(self)
        self.txtGreen = ttk.Entry(self)
        self.txtYellow = ttk.Entry(self)
        self.txtRed = ttk.Entry(self)
        self.txtFirstName.grid(row = self.count, column  =0 )
        self.txtLastName.grid(row = self.count,column = 1)
        self.txtGoal.grid(row = self.count, column  =2 )
        self.txtGreen.grid(row = self.count, column  =3 )
        self.txtYellow.grid(row = self.count, column  =4 )
        self.txtRed.grid(row = self.count, column  =5 )
    def RemovePlayer(self):

        for label in self.grid_slaves():
            if int(label.grid_info()["row"]) > self.count-1 and self.count > self.StartCount :
                label.grid_forget()
        if self.count > self.StartCount:
            self.count-=1




    def get_Match_Report_Data(self):
        data = []
        matchData = []
        matchReport = {}


        for i,j in enumerate(self.grid_slaves()):
            if int(j.grid_info()["row"]) >= self.StartCount:

                try:

                    data.append(j.get())
                    if len(data) == 6 :


                        data =  list(reversed(data))

                        playerData = self.Player_Data(data[2],data[3],data[4],data[5])
                        player = "temp"#self.getPLayerID(data[0],data[1])
                        matchReport[player] = playerData
                        data = []


                except :AttributeError
            else:
                try:

                    matchData.append(j.get())
                    if len(matchData) == 5:


                        matchID ="temp" #self.getMatchID(matchData[4],matchData[3])
                        winStatus = self.win_Status(matchData[2],matchData[1])
                        matchData = self.Match_Data(matchID,matchData[2],matchData[1],winStatus)
                        matchReport["Match Data"] = matchData







                except :AttributeError
        return matchReport
    def write_Match_Report(self,matchReport):
        with open('matchReport.json') as fp:
                matchReport= json.load(fp)
        matchReportID = uuid.uuid4()
        matchReport[matchReportID] = matchReport
    def getMatchID(self,Date,Team):
         with open('matchs.json') as fp:
                matchss= json.load(fp)
         for i in players:
            if i["Date"] ==  Date and i["Team"] == Team: #Will need to change dependent on an uodate to match structure
                return i

    def getPlayerID(self,FirstName,LastName):
        with open('player.json') as fp:
                players= json.load(fp)
        print(players)
        for i in players:
            if i["FirstName"] ==  FirstName and i["LastName"] == LastName:
                return i
    def win_Status(self,ClubScore ,OppositonScore):
        if ClubScore > OppositonScore:
            return "Win"
        elif ClubScore == OppositonScore:
            return "Draw"
        else:
            return "Loss"
    def Match_Data( self,MatchID,ClubScore,OppositonScore,winStatus):
        matchData = {
        "matchID" : MatchID,
        "ClubScore" : ClubScore,
        "OppositionScore" : OppositonScore,
        "WinStatus" : winStatus
        }
        return matchData

    def Player_Data(self,Goal,GreenCards,YellowCards,RedCards):

        PlayerData = {
        "Goals": Goal,
        "Green cards": GreenCards,
        "Yellow cards": YellowCards,
        "Red Cards": RedCards
        }

        return PlayerData
    def Player_stats_update(self,matchReport):

        with open('playersStats.txt') as fp:
            playersData = json.load(fp)

        for i in matchReport:
            if i!= "Match Data":
                playersData[i]["Life time goals"] += i["Goal"]
                playersData[i]["Season goals"] += i["Goal"]
                playersData[i]["Life time green cards"] += i["Green cards"]
                playersData[i]["Season green cards"] += i["Green cards"]
                playersData[i]["Life time yellopw cards"] += i["Yellow cards"]
                playersData[i]["Season yellow cards"] += i["Yellow cards"]
                playersData[i]["Life time red cards"] += i["Red cards"]
                playersData[i]["Season red cards"] += i["Red cards"]
                playersData[i]["Life time Games"] +=1
                playersData[i]["Season games"] += 1

        with open('playersStats.json', 'w+') as fp:
                    json.dump(playersData, fp)

    def seasonReset(self):
        with open('playersStats.json') as fp:
            playersData = json.load(fp)
        for data in playersData:
            data["Season goals"] = 0
            data["Season green cards"] = 0
            data["Season yellow cards"] = 0
            data["Season red cards"] = 0
            data["Season games"] = 0

        with open('players.json', 'w+') as fp:
                    json.dump(playersData, fp)

    def newSeason(self):
        with open('season.txt') as fp:
            season= fp.read()
        date = datetime.datetime.strptime(season, '%Y-%d-%m')
        if datetime.datetime.today() > date:
            self.seasonReset()
            date = date + timedelta(year=1)
            with open('season.txt') as fp:
                fp.write(date)

    def submit(self):
        self.newSeason()
        matchReport = self.get_Match_Report_Data()
        self.write_Match_Report(matchReport)
        self.Player_stats_update(matchReport)

    def ImportTeam(self):
        teamNumber = self.txtImport.get()
        team = self.get_Team(teamNumber)
        self.Write_to_screen(team)


    def get_Team(self,teamNumber):


        Names = [["john","mark"],["antony","jamon"]]
##        with open('team.json') as fp:
##            team = fp.read()
##
##
##        for i in team:
##            Names.append(i["First name"],i["Last name"])




        return Names

    def Write_to_screen(self,team):
        counter = 0
        columnFull =False


        for i,j in enumerate(reversed(self.grid_slaves())):
            if int(j.grid_info()["row"]) >= self.StartCount and int(j.grid_info()["column"]) <=1 :


                try:
                    if int(j.grid_info()["column"]) == 0:
                        columnFull = False
                    if columnFull == False:
                        if j.get() != "":
                            columnFull = True
                            counter +=1

                        else:
                            columnFull = False
                            text = team[int(j.grid_info()["row"])-self.StartCount-counter][int(j.grid_info()["column"])]
                            j.delete(0,tk.END)
                            j.insert(0,text)
                    if columnFull == True:

                        for k,l in  enumerate(reversed(self.grid_slaves())):
                            if k == i-1:
                                l.delete(0,tk.END)


                except :AttributeError

