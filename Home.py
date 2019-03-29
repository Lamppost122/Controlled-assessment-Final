import json
import tkinter as tk
from tkinter import font  as tkfont
from tkinter import messagebox
from tkinter import ttk
from Gui import *
import Config

class Home:

    def BackButtonRun(self):
        Config.PagesViewed.pop()
        self.controller.show_previous_frame(Config.PagesViewed[-1])

    def GetData(self):
        try:
            self.lblDataFirstName.grid_forget()
            self.lblDataLastName.grid_forget()
            self.lblDataPhoneNumber.grid_forget()
            self.lblDataAddress.grid_forget()
            self.lblDataPostcode.grid_forget()
            self.lblDataDateOfBirth.grid_forget()
            self.lblDataTeam.grid_forget()
        except AttributeError:
            pass


        player = SystemToolKit.readFile(Config.PlayerFile)
        team = SystemToolKit.readFile(Config.TeamFile)

        self.lblDataFirstName= tk.Label(self,text ="")
        self.lblDataLastName= tk.Label(self,text="")
        self.lblDataPhoneNumber= tk.Label(self,text="")
        self.lblDataAddress= tk.Label(self,text="")
        self.lblDataPostcode= tk.Label(self,text="")
        self.lblDataDateOfBirth = tk.Label(self,text="")
        self.lblDataTeam = tk.Label(self,text="")

        self.lblDataFirstName.grid(row=1,column=1)
        self.lblDataLastName.grid(row=2,column=1)
        self.lblDataPhoneNumber.grid(row=3,column=1)
        self.lblDataAddress.grid(row=4,column=1)
        self.lblDataPostcode.grid(row=5,column=1)
        self.lblDataDateOfBirth.grid(row=6,column=1)
        self.lblDataTeam.grid(row=7,column = 1 )
        try:
            for k,i in enumerate(team):
                for j in team[i]:
                    if team[i][j] == str(Config.CurrentUser):
                        teamNumber =team[i]["Team Number"]
                        break
                if k == len(team):
                    teamNumber = "No Team Assigned"
            if len(team)==0:
                teamNumber = "No Team Assigned"

            Playerdata = player[Config.CurrentUser]
            self.lblDataFirstName.config(text = Playerdata["First name"])
            self.lblDataLastName.config(text = Playerdata["Last name"])
            self.lblDataPhoneNumber.config(text = Playerdata["Phone number"])
            self.lblDataAddress.config(text = Playerdata["Address"])
            self.lblDataPostcode.config(text = Playerdata["Post code"])
            self.lblDataDateOfBirth.config(text = Playerdata["Date of Birth"])
            self.lblDataTeam.config(text = teamNumber)

        except KeyError:
            messagebox.showinfo("Messgae","Please set up your profile")
            self.controller.show_frame("ProfileSetup")



class HomePlayer(tk.Frame,Home):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller

        """ Widget Declearations """

        self.titleProfile = tk.Label(self,text="My Profile",font=controller.title_font)
        self.lblFirstName= tk.Label(self,text=" First Name :")
        self.lblLastName= tk.Label(self,text=" Last Name :")
        self.lblPhoneNumber= tk.Label(self,text=" Phone Number :")
        self.lblAddress= tk.Label(self,text=" Address :")
        self.lblPostcode= tk.Label(self,text=" Postcode :")
        self.lblDateOfBirth= tk.Label(self,text=" Date of Birth :")
        self.lblTeam = tk.Label(self,text=" Team :")
        self.GetDataButton =tk.Button(self,text="Get Data",command=lambda:self.GetData())
        self.MatchButton =tk.Button(self,text = "Match Data",command = lambda :controller.show_frame("MatchScreen"))
        self.AddPlayerButton=tk.Button(self,text="Setup Profile",command = lambda:controller.show_frame("ProfileSetup"))
        self.NewsButton = tk.Button(self,text = "News/Updates",command = lambda:controller.show_frame("News"))
        self.BackButton= tk.Button(self, text="Back",command=lambda:SystemToolKit.BackButtonRun(controller))

        """ Widget Stylings """

        self.lblFirstName.config(justify="right",fg = "black",background="#8ABFD9",font=("Arial", 10, 'bold'))
        self.lblLastName.config(justify="right",fg = "black",background="#8ABFD9",font=("Arial", 10, 'bold'))
        self.lblPhoneNumber.config(justify="right",fg = "black",background="#8ABFD9",font=("Arial", 10, 'bold'))
        self.lblAddress.config(justify="right",fg = "black",background="#8ABFD9",font=("Arial", 10, 'bold'))
        self.lblPostcode.config(justify="right",fg = "black",background="#8ABFD9",font=("Arial", 10, 'bold'))
        self.lblDateOfBirth.config(justify="right",fg = "black",background="#8ABFD9",font=("Arial", 10, 'bold'))
        self.lblTeam.config(justify="right",fg = "black",background="#8ABFD9",font=("Arial", 10, 'bold'))
        self.GetDataButton.config(compound="left",background="#307292",relief="flat",font=("Arial", 12, 'bold'),padx=5)
        self.MatchButton.config(compound="left",background="#307292",relief="flat",font=("Arial", 12, 'bold'),padx=5)
        self.AddPlayerButton.config(compound="left",background="#307292",relief="flat",font=("Arial", 12, 'bold'),padx=5)
        self.NewsButton.config(compound="left",background="#307292",relief="flat",font=("Arial", 12, 'bold'),padx=5)
        self.BackButton.config(compound="left",background="#307292",relief="flat",font=("Arial", 12, 'bold'),padx=5)
        self.titleProfile.config(background="#8ABFD9",fg = "#404040",pady="5")

        """ Widget Positions """

        self.titleProfile.grid(row = 0 ,column = 0 ,columnspan = 3)
        self.lblFirstName.grid(row=1,column=0)
        self.lblLastName.grid(row=2,column=0)
        self.lblPhoneNumber.grid(row=3,column=0)
        self.lblAddress.grid(row=4,column=0)
        self.lblPostcode.grid(row=5,column=0)
        self.lblDateOfBirth.grid(row=6,column=0)
        self.lblTeam.grid(row=7,column = 0 )
        self.GetDataButton.grid(row=8,column =0)
        self.MatchButton.grid(row = 1,column = 3)
        self.NewsButton.grid(row=3,column =3)
        self.BackButton.grid(row=6,column = 3)
        self.AddPlayerButton.grid(row=4,column=3)

class HomeCoach(tk.Frame,Home):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller

        """ Widget Declearations """

        self.titleProfile = tk.Label(self,text="My Profile",font=controller.title_font)
        self.lblFirstName= tk.Label(self,text=" First Name :")
        self.lblLastName= tk.Label(self,text=" Last Name :")
        self.lblPhoneNumber= tk.Label(self,text=" Phone Number :")
        self.lblAddress= tk.Label(self,text=" Address :")
        self.lblPostcode= tk.Label(self,text=" Postcode :")
        self.lblDateOfBirth= tk.Label(self,text=" Date of Birth :")
        self.lblTeam = tk.Label(self,text=" Team :")
        self.GetDataButton =tk.Button(self,text="Get Data",command=lambda:self.GetData())
        self.MatchButton =tk.Button(self,text = "Match Data",command = lambda :controller.show_frame("MatchScreen"))
        self.PlayerStatsButton =tk.Button(self,text="Player Stats",command = lambda :controller.show_frame("PlayerStats"))
        self.AdminCommandsButton = tk.Button(self,text = "AdminCommands",command = lambda:controller.show_frame("AdminCommands"))
        self.AddPlayerButton=tk.Button(self,text="Setup Profile",command = lambda:controller.show_frame("ProfileSetup"))
        self.NewsButton = tk.Button(self,text = "News/Updates",command = lambda:controller.show_frame("News"))
        self.BackButton= tk.Button(self, text="Back",command=lambda:SystemToolKit.BackButtonRun(controller))

        """ Widget Stylings """

        self.lblFirstName.config(justify="right",fg = "black",background="#8ABFD9",font=("Arial", 10, 'bold'))
        self.lblLastName.config(justify="right",fg = "black",background="#8ABFD9",font=("Arial", 10, 'bold'))
        self.lblPhoneNumber.config(justify="right",fg = "black",background="#8ABFD9",font=("Arial", 10, 'bold'))
        self.lblAddress.config(justify="right",fg = "black",background="#8ABFD9",font=("Arial", 10, 'bold'))
        self.lblPostcode.config(justify="right",fg = "black",background="#8ABFD9",font=("Arial", 10, 'bold'))
        self.lblDateOfBirth.config(justify="right",fg = "black",background="#8ABFD9",font=("Arial", 10, 'bold'))
        self.lblTeam.config(justify="right",fg = "black",background="#8ABFD9",font=("Arial", 10, 'bold'))
        self.GetDataButton.config(compound="left",background="#307292",relief="flat",font=("Arial", 12, 'bold'),padx=5)
        self.MatchButton.config(compound="left",background="#307292",relief="flat",font=("Arial", 12, 'bold'),padx=5)
        self.AdminCommandsButton.config(compound="left",background="#307292",relief="flat",font=("Arial", 12, 'bold'),padx=5)
        self.AddPlayerButton.config(compound="left",background="#307292",relief="flat",font=("Arial", 12, 'bold'),padx=5)
        self.NewsButton.config(compound="left",background="#307292",relief="flat",font=("Arial", 12, 'bold'),padx=5)
        self.BackButton.config(compound="left",background="#307292",relief="flat",font=("Arial", 12, 'bold'),padx=5)
        self.PlayerStatsButton.config(compound="left",background="#307292",relief="flat",font=("Arial", 12, 'bold'),padx=5)
        self.titleProfile.config(background="#8ABFD9",fg = "#404040",pady="5")

        """ Widget Positions """

        self.titleProfile.grid(row = 0 ,column = 0 ,columnspan = 3)
        self.lblFirstName.grid(row=1,column=0)
        self.lblLastName.grid(row=2,column=0)
        self.lblPhoneNumber.grid(row=3,column=0)
        self.lblAddress.grid(row=4,column=0)
        self.lblPostcode.grid(row=5,column=0)
        self.lblDateOfBirth.grid(row=6,column=0)
        self.lblTeam.grid(row=7,column = 0 )
        self.GetDataButton.grid(row=8,column =0)
        self.MatchButton.grid(row = 1,column = 3)
        self.AdminCommandsButton.grid(row=2,column =3)
        self.NewsButton.grid(row=3,column =3)
        self.BackButton.grid(row=6,column = 3)
        self.PlayerStatsButton.grid(row=5,column =3)
        self.AddPlayerButton.grid(row=4,column=3)



class HomeAdmin(tk.Frame,Home):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller

        """ Widget Declearations """

        self.titleProfile = tk.Label(self,text="My Profile",font=controller.title_font)
        self.lblFirstName= tk.Label(self,text=" First Name :")
        self.lblLastName= tk.Label(self,text=" Last Name :")
        self.lblPhoneNumber= tk.Label(self,text=" Phone Number :")
        self.lblAddress= tk.Label(self,text=" Address :")
        self.lblPostcode= tk.Label(self,text=" Postcode :")
        self.lblDateOfBirth= tk.Label(self,text=" Date of Birth :")
        self.lblTeam = tk.Label(self,text=" Team :")
        self.GetDataButton =tk.Button(self,text="Get Data",command=lambda:self.GetData())
        self.MatchButton =tk.Button(self,text = "Match Data",command = lambda :controller.show_frame("MatchScreen"))
        self.PlayerStatsButton =tk.Button(self,text="Player Stats",command = lambda :controller.show_frame("PlayerStats"))
        self.AdminCommandsButton = tk.Button(self,text = "AdminCommands",command = lambda:controller.show_frame("AdminCommands"))
        self.AddPlayerButton=tk.Button(self,text="Setup Profile",command = lambda:controller.show_frame("ProfileSetup"))
        self.NewsButton = tk.Button(self,text = "News/Updates",command = lambda:controller.show_frame("News"))
        self.BackButton= tk.Button(self, text="Back",command=lambda:SystemToolKit.BackButtonRun(controller))

        """ Widget Stylings """

        self.lblFirstName.config(justify="right",fg = "black",background="#8ABFD9",font=("Arial", 10, 'bold'))
        self.lblLastName.config(justify="right",fg = "black",background="#8ABFD9",font=("Arial", 10, 'bold'))
        self.lblPhoneNumber.config(justify="right",fg = "black",background="#8ABFD9",font=("Arial", 10, 'bold'))
        self.lblAddress.config(justify="right",fg = "black",background="#8ABFD9",font=("Arial", 10, 'bold'))
        self.lblPostcode.config(justify="right",fg = "black",background="#8ABFD9",font=("Arial", 10, 'bold'))
        self.lblDateOfBirth.config(justify="right",fg = "black",background="#8ABFD9",font=("Arial", 10, 'bold'))
        self.lblTeam.config(justify="right",fg = "black",background="#8ABFD9",font=("Arial", 10, 'bold'))
        self.GetDataButton.config(compound="left",background="#307292",relief="flat",font=("Arial", 12, 'bold'),padx=5)
        self.MatchButton.config(compound="left",background="#307292",relief="flat",font=("Arial", 12, 'bold'),padx=5)
        self.AdminCommandsButton.config(compound="left",background="#307292",relief="flat",font=("Arial", 12, 'bold'),padx=5)
        self.AddPlayerButton.config(compound="left",background="#307292",relief="flat",font=("Arial", 12, 'bold'),padx=5)
        self.NewsButton.config(compound="left",background="#307292",relief="flat",font=("Arial", 12, 'bold'),padx=5)
        self.BackButton.config(compound="left",background="#307292",relief="flat",font=("Arial", 12, 'bold'),padx=5)
        self.PlayerStatsButton.config(compound="left",background="#307292",relief="flat",font=("Arial", 12, 'bold'),padx=5)
        self.titleProfile.config(background="#8ABFD9",fg = "#404040",pady="5")

        """ Widget Positions """

        self.titleProfile.grid(row = 0 ,column = 0 ,columnspan = 3)
        self.AdminCommandsButton.grid(row=3,column =4)
        self.lblFirstName.grid(row=1,column=0)
        self.lblLastName.grid(row=2,column=0)
        self.lblPhoneNumber.grid(row=3,column=0)
        self.lblAddress.grid(row=4,column=0)
        self.lblPostcode.grid(row=5,column=0)
        self.lblDateOfBirth.grid(row=6,column=0)
        self.lblTeam.grid(row=7,column = 0 )
        self.GetDataButton.grid(row=8,column =0)
        self.MatchButton.grid(row = 1,column = 3)
        self.AdminCommandsButton.grid(row=2,column =3)
        self.NewsButton.grid(row=3,column =3)
        self.BackButton.grid(row=6,column = 3)
        self.PlayerStatsButton.grid(row=5,column =3)
        self.AddPlayerButton.grid(row=4,column=3)