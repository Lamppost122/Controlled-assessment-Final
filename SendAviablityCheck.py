import json
import tkinter as tk
from tkinter import font  as tkfont
from tkinter import messagebox
from tkinter import ttk
from Gui import *
from MatchScreen import *
from AddMatch import *
import Config
import Validation
class SendAvailablityCheck:
    def BackButtonRun(self):
        Config.PagesViewed.pop()
        self.controller.show_previous_frame(Config.PagesViewed[-1])


    def GetData(self):
        if Validaion.TeamNumber( self.txtTeamNumber.get()) == True:
            self.GetTeam()
            self.GetMatches()

    def GetTeam(self):
        self.TeamList.delete(0,tk.END)

        for i, j in enumerate(self.team):
            if self.team[j]["Team Number"] == self.txtTeamNumber.get():
                for k,l in enumerate(self.allPlayers):
                    self.TeamPlayers.append(self.team[j][str(k)])
                    text = str(self.allPlayers[self.team[j][str(k)]]["First name"]) + " " + str(self.allPlayers[self.team[j][str(k)]]["Last name"])

                    self.TeamList.insert(tk.END,text)
            break

    def GetMatches(self):
        self.MatchList.delete(0,tk.END)
        self.teamMatches = SystemToolKit.readFile(Config.MatchFile)
        self.matches = self.teamMatches[MatchScreen.GetTeamID(self.txtTeamNumber.get())]
        self.orderedList = []
        for item in self.matches:
            self.orderedList.append(item)
            text = str(self.txtTeamNumber.get()) +" vs " +self.matches[item]["Opposition"]+" on " +self.matches[item]["Date"]
            self.MatchList.insert(tk.END,text)

    def SendEmailToAll(self):
        self.ConnectToSever()
        Text = self.getText()
        for i in self.getEmailList():
            self.SendEmail(i,Text)
        self.DiscconectToServer()
        self.UpdateAvailablityFile()
        messagebox.showinfo("Message","All Emails Sent")
        self.BackButtonRun()


    def ConnectToSever(self):
        self.server = smtplib.SMTP('smtp.gmail.com', 587)
        self.server.starttls()
        self.server.login("ComputerScienceTest1@gmail.com", "Password1@")

    def DiscconectToServer(self):
        self.server.quit()

    def SendEmail(self,Email,Text):
        msg = MIMEMultipart()
        msg['Subject'] = "Match Availablity"
        msg.attach(MIMEText(Text, 'html'))
        text = msg.as_string()
        self.server.sendmail("ComputerScienceTest1@gmail.com",Email, text)


    def getEmailList(self):
        EmailList=[]
        for i in self.TeamPlayers:
            for j in self.allUsers:
                EmailList.append(self.allUsers[i]["Email"])

        return EmailList

    def getText(self):
        try:
            Data = self.matches[self.orderedList[self.MatchList.index(tk.ANCHOR)]]
            text = "Are you able to play on "+Data["Date"]+"at "+Data["Time"]+" against "+ Data["Opposition"]+"\n The Location is " + Data["Location"]
            return text
        except IndexError:
            messagebox.showinfo("Message","No Match referenced")

    def UpdateAvailablityFile(self):
        Matches = SystemToolKit.readFile(Config.MatchAvailablityFile)

        MatchAvailablityData = {}

        for i in self.TeamPlayers:
            MatchAvailablityData[i] = "None"
        TeamId = AddMatch.getTeamId(self.txtTeamNumber.get())
        Teams = Matches[TeamId]

        MatchAvailablityData["Date"] =self.matches[self.orderedList[self.MatchList.index(tk.ANCHOR)]]["Date"]
        Teams[self.orderedList[self.MatchList.index(tk.ANCHOR)]] = MatchAvailablityData

        Matches[TeamId]=Teams

        with open(Config.MatchAvailablityFile,"w+")as fp:
            json.dump(Matches,fp)

class SendAvailablityCheckAdmin(tk.Frame,SendAvailablityCheck):

        def __init__(self, parent, controller):
            tk.Frame.__init__(self, parent)
            self.controller = controller

            """ Widget Declearations """

            self.Title =tk.Label(self,text="Send aviablibilty Check",font=controller.title_font)
            self.TeamList = tk.Listbox(self)
            self.GetTeamButton = tk.Button(self,text = "Get Data",command = self.GetData)
            self.BackButton= tk.Button(self, text="Back",command=lambda:self.BackButtonRun())
            self.SendEmailButton= tk.Button(self, text="Send All Emails",command=lambda:self.SendEmailToAll())
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
            self.BackButton= tk.Button(self, text="Back",command=lambda:self.BackButtonRun())
            self.SendEmailButton= tk.Button(self, text="Send All Emails",command=lambda:self.SendEmailToAll())
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
