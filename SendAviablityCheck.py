import json
import tkinter as tk
from tkinter import font  as tkfont
from tkinter import messagebox
from tkinter import ttk
from Gui import *
from MatchScreen import *
from SystemToolKit import *
import Config
from Validation import *
import smtplib
from email.MIMEMultipart import MIMEMultipart
from email.MIMEText import MIMEText

class SendAvailablityCheck:
    """
    Methods:
        GetData
        GetTeam
        GetMatches
        UpdateListboxes
        SendEmailToAll
    Variables:
        orderedList - A list of playerIds
        teamMatches - contains a instance of the MatchFile
        matches - cotans oonly a spacifc teams Matches
        TeamPlayers - contains instance
    """

    def GetData(self):
        """ Validates the team number and calls the GetTeam, GetMatches and UpdateListboxes """
        if Validation.TeamNumber( self.txtTeamNumber.get()) == True:
            self.GetTeam()
            self.GetMatches()
            self.UpdateListboxes()

    def GetTeam(self):
        """Adds players into the TeamPlayers List """
        self.TeamPlayers = []
        if Validation.TeamNumber(self.txtTeamNumber.get()) ==True:
            for i, j in enumerate(self.team):
                if self.team[j]["Team Number"] == self.txtTeamNumber.get():
                    for k,l in enumerate(self.team[j]):
                        if self.team[j][l] in self.allPlayers.keys():
                            if self.team[j][l] not in self.TeamPlayers and self.team[j][l] not in self.orderedList:
                                self.TeamPlayers.append(self.team[j][l])

    def GetMatches(self):

        self.orderedList = []
        self.MatchList.delete(0,tk.END)
        self.teamMatches = SystemToolKit.readFile(Config.MatchFile)
        self.matches = self.teamMatches[SystemToolKit.getTeamId(self.txtTeamNumber.get())]
        for i in self.matches:
            self.orderedList.append(i)



    def UpdateListboxes(self):
        self.MatchList.delete(0,tk.END)
        self.TeamList.delete(0,tk.END)
        for i in self.matches:
            text = str(self.txtTeamNumber.get()) +" vs " +self.matches[i]["Opposition"]+" on " +self.matches[i]["Date"]
            self.MatchList.insert(tk.END,text)
        for j in self.TeamPlayers:
            text = str(self.allPlayers[j]["First name"]) + " " + str(self.allPlayers[j]["Last name"])
            self.TeamList.insert(tk.END,text)




    def SendEmailToAll(self,controller):
        self.ConnectToSever()
        Text = self.getText()
        for i in self.getEmailList():
            self.SendEmail(i,Text)
        self.DiscconectToServer()
        self.UpdateAvailablityFile()
        messagebox.showinfo("Message","All Emails Sent")
        SystemToolKit.BackButtonRun(controller)


    def ConnectToSever(self):
        self.server = smtplib.SMTP('smtp.gmail.com', 587)
        self.server.starttls()
        self.server.login(Config.EmailAddress, Config.EmailPassword)


    def DiscconectToServer(self):
        self.server.quit()


    def SendEmail(self,Email,Text):
        msg = MIMEMultipart()
        msg['Subject'] = "Match Availablity"
        msg.attach(MIMEText(Text, 'html'))
        text = msg.as_string()
        self.server.sendmail(Config.EmailAddress,Email, text)



    def getEmailList(self):
        EmailList=[]
        for i in self.TeamPlayers:
            EmailList.append(self.allUsers[i]["Email"])

        return EmailList

    def getText(self):
        try:

            Data = self.matches[self.orderedList[self.MatchList.index(tk.ANCHOR)]]
            text = "Are you able to play on "+Data["Date"]+" at "+Data["Time"]+" against "+ Data["Opposition"]+"\n The Location is " + Data["Location"]
            return text
        except IndexError:
            messagebox.showinfo("Message","No Match referenced")

    def UpdateAvailablityFile(self):
        TeamData = SystemToolKit.readFile(Config.MatchAvailablityFile)


        PlayerData = {}
        for i in self.TeamPlayers:
            PlayerData[i] = "None"
        PlayerData["Date"] =self.matches[self.orderedList[self.MatchList.index(tk.ANCHOR)]]["Date"]

        MatchId = self.orderedList[self.MatchList.index(tk.ANCHOR)]
        TeamId = SystemToolKit.getTeamId(self.txtTeamNumber.get())

        try:
             MatchData =TeamData[TeamId]
        except KeyError:
            MatchData = {}

        MatchData[MatchId] = PlayerData
        TeamData[TeamId] = MatchData

        with open(Config.MatchAvailablityFile,"w+")as fp:
            json.dump(TeamData,fp)

class SendAvailablityCheckAdmin(tk.Frame,SendAvailablityCheck):

        def __init__(self, parent, controller):
            tk.Frame.__init__(self, parent)
            self.controller = controller

            """ Widget Declearations """

            self.Title =tk.Label(self,text="Send aviablibilty Check",font=controller.title_font)
            self.TeamList = tk.Listbox(self)
            self.GetTeamButton = tk.Button(self,text = "Get Data",command = self.GetData)
            self.BackButton= tk.Button(self, text="Back",command=lambda:SystemToolKit.BackButtonRun(controller))
            self.SendEmailButton= tk.Button(self, text="Send All Emails",command=lambda:self.SendEmailToAll(controller))
            self.lblPlayers = tk.Label(self,text="Players:")
            self.lblMatches = tk.Label(self,text="Matches:")
            self.MatchList = tk.Listbox(self)
            self.txtTeamNumber = ttk.Entry(self)

            """ Widget Stylings """

            self.Title.config(background="#8ABFD9",fg = "#404040",pady="5")
            self.GetTeamButton.config(compound="left",background="#307292",relief="flat",font=("Arial", 10, 'bold'),padx=5)
            self.BackButton.config(compound="left",background="#307292",relief="flat",font=("Arial", 10, 'bold'),padx=5)
            self.SendEmailButton.config(compound="left",background="#307292",relief="flat",font=("Arial", 10, 'bold'),padx=5)
            self.lblPlayers.config(justify="right",fg = "black",background="#8ABFD9",font=("Arial", 10, 'bold'))
            self.lblMatches.config(justify="right",fg = "black",background="#8ABFD9",font=("Arial", 10, 'bold'))
            self.MatchList.config(width="40")

            """ Widget Positions """

            self.Title.grid(row=0,column=0)
            self.GetTeamButton.grid(row=1,column=1)
            self.txtTeamNumber.grid(row=1,column =0)
            self.lblPlayers.grid(row=2,column =0)
            self.TeamList.grid(row=3,column=0)
            self.lblMatches.grid(row=2,column=1)
            self.MatchList.grid(row=3,column=1)
            self.SendEmailButton.grid(row=3,column = 3)
            self.BackButton.grid(row=1,column=3)

            self.team = SystemToolKit.readFile(Config.TeamFile)
            self.allPlayers = SystemToolKit.readFile(Config.PlayerFile)
            self.allUsers =SystemToolKit.readFile(Config.UserFile)
            self.TeamPlayers = []
            self.orderedList = []

class SendAvailablityCheckCoach(tk.Frame,SendAvailablityCheck):

        def __init__(self, parent, controller):
            tk.Frame.__init__(self, parent)
            self.controller = controller

            """ Widget Declearations """

            self.Title =tk.Label(self,text="Send aviablibilty Check",font=controller.title_font)
            self.TeamList = tk.Listbox(self)
            self.GetTeamButton = tk.Button(self,text = "Get Data",command = self.GetData)
            self.BackButton= tk.Button(self, text="Back",command=lambda:SystemToolKit.BackButtonRun(controller))
            self.SendEmailButton= tk.Button(self, text="Send All Emails",command=lambda:self.SendEmailToAll(controller))
            self.lblPlayers = tk.Label(self,text="Players:")
            self.lblMatches = tk.Label(self,text="Matches:")
            self.MatchList = tk.Listbox(self)
            self.txtTeamNumber = ttk.Entry(self)

            """ Widget Stylings """

            self.Title.config(background="#8ABFD9",fg = "#404040",pady="5")
            self.GetTeamButton.config(compound="left",background="#307292",relief="flat",font=("Arial", 10, 'bold'),padx=5)
            self.BackButton.config(compound="left",background="#307292",relief="flat",font=("Arial", 10, 'bold'),padx=5)
            self.SendEmailButton.config(compound="left",background="#307292",relief="flat",font=("Arial", 10, 'bold'),padx=5)
            self.lblPlayers.config(justify="right",fg = "black",background="#8ABFD9",font=("Arial", 10, 'bold'))
            self.lblMatches.config(justify="right",fg = "black",background="#8ABFD9",font=("Arial", 10, 'bold'))
            self.MatchList.config(width="40")

            """ Widget Positions """

            self.Title.grid(row=0,column=0)
            self.GetTeamButton.grid(row=1,column=1)
            self.txtTeamNumber.grid(row=1,column =0)
            self.lblPlayers.grid(row=2,column =0)
            self.TeamList.grid(row=3,column=0)
            self.lblMatches.grid(row=2,column=1)
            self.MatchList.grid(row=3,column=1)
            self.SendEmailButton.grid(row=3,column = 3)
            self.BackButton.grid(row=1,column=3)

            self.team = SystemToolKit.readFile(Config.TeamFile)
            self.allPlayers = SystemToolKit.readFile(Config.PlayerFile)
            self.allUsers =SystemToolKit.readFile(Config.UserFile)
            self.TeamPlayers = []
            self.orderedList = []


class SendAvailablityCheckPlayer(tk.Frame,SendAvailablityCheck):

        def __init__(self, parent, controller):
            tk.Frame.__init__(self, parent)
            self.controller = controller

            """ Widget Declearations """

            """ Widget Stylings """

            """ Widget Positions """
