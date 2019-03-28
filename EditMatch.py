import json
import tkinter as tk
from tkinter import font  as tkfont
from tkinter import messagebox
from tkinter import ttk
from Gui import *
from AddMatch import *
import Config
from SystemToolKit import *
from Validation import *

class EditMatch:
    def BackButtonRun(self):
            Config.PagesViewed.pop()
            self.controller.show_previous_frame(Config.PagesViewed[-1])


    def GetMatches(self):

        self.orderedList = []
        self.teamMatches = []
        matches =SystemToolKit.readFile(Config.MatchFile)
        teamID = AddMatch.getTeamId(self.txtTeam.get())

        """ Widget Declearations """
        self.lblOpposition=tk.Label(self,text="Opposition")
        self.lblDate =tk.Label(self,text="Date")
        self.lblTime =tk.Label(self,text="Time")
        self.lblLocation =tk.Label(self,text="Location")

        """ Widget Stylings """

        self.lblOpposition.config(justify="right",fg = "black",background="#8ABFD9",font=("Arial", 10, 'bold'))
        self.lblDate.config(justify="right",fg = "black",background="#8ABFD9",font=("Arial", 10, 'bold'))
        self.lblTime.config(justify="right",fg = "black",background="#8ABFD9",font=("Arial", 10, 'bold'))
        self.lblLocation.config(justify="right",fg = "black",background="#8ABFD9",font=("Arial", 10, 'bold'))

        """ Widget Positions """

        self.lblOpposition.grid(row = self.StartCount-1, column  =0 )
        self.lblDate.grid(row = self.StartCount-1, column  =1 )
        self.lblTime.grid(row = self.StartCount-1, column  =2 )
        self.lblLocation.grid(row = self.StartCount-1, column  =3 )

        try:
            self.txtOpposition.grid_forget()
            self.txtDate.grid_forget()
            self.txtTime.grid_forget()
            self.txtLocation.grid_forget()
        except AttributeError:
            pass


        for i in matches:
            if i == teamID:
                for j in matches[i]:

                    if j not in self.orderedList :

                        self.teamMatches.append(matches[i][j])
                        self.orderedList.append(j)




        for i ,j in enumerate(self.teamMatches):


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




            self.txtOpposition.insert(0,str(j["Opposition"]))
            self.txtDate.insert(0,str(j["Date"]))
            self.txtTime.insert(0,str(j["Time"]))
            self.txtLocation.insert(0,str(j["Location"]))
        self.orderedList =list(reversed(self.orderedList))




    def Edit_Match(self):

        count = 0
        error =False
        data = []
        with open(Config.MatchFile,"r") as fp:
            MatchTeamData = json.load(fp)
        MatchData = MatchTeamData[AddMatch.getTeamId(self.txtTeam.get())]

        for i,j in enumerate(self.grid_slaves()):

            if int(j.grid_info()["row"]) >= self.StartCount:

                    data.append(j.get())


                    if len(data) == 4 :
                        data =  list(reversed(data))


                        if count<len(self.orderedList):
                            if Validation.Opposition(data[0]) == True and Validation.Address(data[3])==True and Validation.Time(data[2])==True and Validation.Date(data[1])==True:

                                MatchData[self.orderedList[count]] = {"Opposition":data[0],"Location":data[3],"Time":data[2],"Date":data[1]}

                                count +=1
                                data = []

                            else:
                                error =True




        MatchTeamData[AddMatch.getTeamId(self.txtTeam.get())] =MatchData


        with open(Config.MatchFile,"w") as fp:
            json.dump(MatchTeamData,fp)
        self.controller.show_frame("Home")


class EditMatchAdmin(tk.Frame,EditMatch):

        def __init__(self, parent, controller):
            tk.Frame.__init__(self, parent)
            self.controller = controller
            self.StartCount = 3

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
            self.StartCount = 3

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
