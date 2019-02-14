import json
import tkinter as tk
from tkinter import font  as tkfont
from tkinter import messagebox
from tkinter import ttk
from Gui import *
from MatchScreen import *

class SendAvailablityCheck(tk.Frame):

        def __init__(self, parent, controller):
            tk.Frame.__init__(self, parent)
            self.controller = controller
            self.Title =tk.Label(self,text="Send aviablibilty Check",font=controller.title_font)
            self.TeamList = tk.Listbox(self)
            self.GetTeamButton = tk.Button(self,text = "Get Team",command = self.GetTeam)
            self.GetMatchButton = tk.Button(self,text = "Get Matches",command = self.GetMatches)
            self.BackButton= tk.Button(self, text="Back",command=lambda:self.BackButtonRun(controller))
            self.SendEmailButton= tk.Button(self, text="Back",command=lambda:self.BackButtonRun(controller))
            self.lblPlayers = tk.Label(self,text="Players:")
            self.lblMatches = tk.Label(self,text="Matches:")
            self.MatchList = tk.Listbox(self)
            self.txtTeamNumber = tk.Entry(self)
            self.Title.grid(row=0,column=0)
            self.GetTeamButton.grid(row=1,column=1)
            self.GetMatchButton.grid(row=1,column=2)
            self.txtTeamNumber.grid(row=1,column =0)
            self.lblPlayers.grid(row=2,column =0)
            self.TeamList.grid(row=3,column=0)
            self.lblMatches.grid(row=2,column=1)
            self.MatchList.grid(row=3,column=1)
            self.team = SystemToolKit.readFile("team.json")
            self.allPlayers = SystemToolKit.readFile("players.json")
            self.TeamPlayers = []
            self.orderedList = []


        def BackButtonRun(self,controller):
            global PagesViewed
            PagesViewed.pop()
            controller.show_frame(PagesViewed[-1])


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

            self.teamMatches = SystemToolKit.readFile("matches.json")
            print self.teamMatches[MatchScreen.GetTeamID(self.txtTeamNumber.get())]
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

        @staticmethod
        def ConnectToSever():
            pass
        @staticmethod
        def DiscconectToServer():
            pass
        @staticmethod
        def SendEmail(Email,Text):
            pass

        def getEmailList(self):
            EmailList=[]
            for i in self.TeamPlayers:
                EmailList.append(self.team[i]["Email"])
            return EmailList
        def getText():
            Data = self.matches[self.orderedList[self.MatchList.index(tk.ANCHOR)]]
            text = "Are you able to play on "+Data["Date"]+"at "+Date["Time"]+" against "+ Data["Oppositon"]+"\n The Location is " + Data["Location"]
            return text
        def UpdateAvailablityFile(self):
            pass








