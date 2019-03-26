import json
import tkinter as tk
from tkinter import font  as tkfont
from tkinter import messagebox
from tkinter import ttk
from Gui import *
import Config
from SystemToolKit import *
import Validation

class EditMatch:
    def BackButtonRun(self):
            Config.PagesViewed.pop()
            self.controller.show_previous_frame(Config.PagesViewed[-1])


    def GetMatches(self):

        self.orderedList = []
        matches =SystemToolKit.readFile(Config.MatchFile)
        self.teamMatches = matches[self.txtTeam.get()]

        for i ,j in enumerate(self.teamMatches):
            self.orderedList.append(j)

            """ Widget Declearations """

            self.txtOpposition=ttk.Entry(self)
            self.txtDate = ttk.Entry(self)
            self.txtTime = ttk.Entry(self)
            self.txtLocation = ttk.Entry(self)

            """ Widget Stylings """

            """ Widget Positions """

            self.txtOpposition.grid(row = self.StartCount+i, column  =0 )
            self.txtDate.grid(row = self.StartCount+i,column = 1)
            self.txtTime.grid(row = self.StartCount+i, column  =2 )
            self.txtLocation.grid(row = self.StartCount + i, column  =3 )

            self.txtOpposition.insert(0,self.teamMatches[j]["Opposition"])
            self.txtDate.insert(0,self.teamMatches[j]["Date"])
            self.txtTime.insert(0,self.teamMatches[j]["Time"])
            self.txtLocation.insert(0,self.teamMatches[j]["Location"])

        self.orderedList = list(reversed(self.orderedList))

    def Edit_Match(self):

        count = 0
        error =False
        data = []

        for i,j in enumerate(self.grid_slaves()):
            if int(j.grid_info()["row"]) >= self.StartCount:

                try:

                    data.append(j.get())
                    if len(data) == 4 :
                        data =  list(reversed(data))
                        if Validation.Opposition(data[0]) == True and Validation.Address(data[3])==True and Validation.Time(data[2])==True and Validation.Date(data[1])==True:
                            self.teamMatches[self.orderedList[count]]["Opposition"] = data[0]
                            self.teamMatches[self.orderedList[count]]["Location"] = data[3]
                            self.teamMatches[self.orderedList[count]]["Time"] = data[2]
                            self.teamMatches[self.orderedList[count]]["Date"] = data[1]
                            count +=1
                            data = []
                        else:
                            error =True

                except :AttributeError

        if error == False:
            with open(Config.MatchFile, 'w') as fp:
                json.dump(self.teamMatches,fp)

class EditMatchAdmin(tk.Frame,EditMatch):

        def __init__(self, parent, controller):
            tk.Frame.__init__(self, parent)
            self.controller = controller
            self.StartCount = 2

            """ Widget Declearations """

            self.Title = tk.Label(self,text = "Edit Match" ,font = controller.title_font)
            self.lblTeam = tk.Label(self,text = "Team: ")
            self.txtTeam = ttk.Entry(self)
            self.getMatchesButton = tk.Button(self,text = "Get Matches",command = self.GetMatches)
            self.EditMatchButton = tk.Button(self,text = "Edit Matches",command = self.Edit_Match)
            self.BackButton= tk.Button(self, text="Back",command=lambda:self.BackButtonRun())

            """ Widget Stylings """

            self.lblTeam.config(justify="right",fg = "black",background="#8ABFD9",font=("Arial", 10, 'bold'))
            self.getMatchesButton.config(compound="left",background="#307292",relief="flat",font=("Arial", 12, 'bold'),padx=5)
            self.EditMatchButton.config(compound="left",background="#307292",relief="flat",font=("Arial", 12, 'bold'),padx=5)
            self.BackButton.config(compound="left",background="#307292",relief="flat",font=("Arial", 12, 'bold'),padx=5)
            self.Title.config(background="#8ABFD9",fg = "#404040",pady="5")

            """ Widget Positons """

            self.Title.grid(row =0,column =0,columnspan =4)
            self.lblTeam.grid(row =1,column =0)
            self.txtTeam.grid(row =1,column =1)
            self.getMatchesButton.grid(row =1,column =2)
            self.EditMatchButton.grid(row =1,column =3)
            self.BackButton.grid(row =1,column = 4)

class EditMatchCoach(tk.Frame,EditMatch):

        def __init__(self, parent, controller):
            tk.Frame.__init__(self, parent)
            self.controller = controller
            self.StartCount = 2

            """ Widget Declearations """

            self.Title = tk.Label(self,text = "Edit Match" ,font = controller.title_font)
            self.lblTeam = tk.Label(self,text = "Team: ")
            self.txtTeam = ttk.Entry(self)
            self.getMatchesButton = tk.Button(self,text = "Get Matches",command = self.GetMatches)
            self.EditMatchButton = tk.Button(self,text = "Edit Matches",command = self.Edit_Match)
            self.BackButton= tk.Button(self, text="Back",command=lambda:self.BackButtonRun())

            """ Widget Stylings """

            self.lblTeam.config(justify="right",fg = "black",background="#8ABFD9",font=("Arial", 10, 'bold'))
            self.getMatchesButton.config(compound="left",background="#307292",relief="flat",font=("Arial", 12, 'bold'),padx=5)
            self.EditMatchButton.config(compound="left",background="#307292",relief="flat",font=("Arial", 12, 'bold'),padx=5)
            self.BackButton.config(compound="left",background="#307292",relief="flat",font=("Arial", 12, 'bold'),padx=5)
            self.Title.config(background="#8ABFD9",fg = "#404040",pady="5")

            """ Widget Positions """

            self.Title.grid(row =0,column =0,columnspan =4)
            self.lblTeam.grid(row =1,column =0)
            self.txtTeam.grid(row =1,column =1)
            self.getMatchesButton.grid(row =1,column =2)
            self.EditMatchButton.grid(row =1,column =3)
            self.BackButton.grid(row =1,column = 4)

class EditMatchPlayer(tk.Frame,EditMatch):

        def __init__(self, parent, controller):
            tk.Frame.__init__(self, parent)
            self.controller = controller

            """ Widget Declearations """

            """ Widget Stylings """

            """ Widget Positions """