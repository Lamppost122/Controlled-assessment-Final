import json
import tkinter as tk
from tkinter import font  as tkfont
from tkinter import messagebox
from tkinter import ttk

PagesViewed = ["Login"]
from SystemToolKit import *
from Login import *
from Register import *
from ProfileSetup import *
from Home import *
from AddMatch import *
from MatchScreen import *
from AdminCommands import *
from RemoveMatch import *
from EditMatch import *
from News import *
from AddNews import *
from MatchReport import *
from RemovePlayer import *
from EditPlayer import *
from AddTeam import *
from RemoveTeam import *
from EditTeam import *
from System_init import *
from BackUp import *
from ConfirmEmail import *
from Gui import *
from ImportData import *
from SendAviablityCheck import *
from ConfirmAvailablity import *
from ViewAvailablity import *
from PlayerStats import *
import Config

class SampleApp(tk.Tk):

    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
        global PagesViewed


        self.title_font = tkfont.Font(family='ariel', size=18, weight="bold", slant="italic")
        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}
        for F in (LoginAdmin,LoginPlayer,LoginCoach, RegisterAdmin,RegisterPlayer
        ,RegisterCoach,ProfileSetupPlayer,HomeCoach,HomePlayer,HomeAdmin
        ,AddMatchPlayer,AddMatchCoach,AddMatchAdmin,MatchScreenPlayer
        ,MatchScreenCoach,MatchScreenAdmin,AdminCommandsAdmin,AdminCommandsPlayer
        ,AdminCommandsCoach,RemoveMatchPlayer,RemoveMatchCoach,RemoveMatchAdmin
        ,EditMatchCoach,EditMatchPlayer,EditMatchAdmin,NewsAdmin,NewsPlayer,NewsCoach
        ,AddNewsAdmin,AddNewsPlayer,AddNewsCoach,MatchReportAdmin,MatchReportCoach
        ,MatchReportPlayer,RemovePlayerPlayer,RemovePlayerAdmin,RemovePlayerCoach
        ,EditPlayerAdmin,EditPlayerPlayer,EditPlayerCoach,AddTeamPlayer,AddTeamAdmin
        ,AddTeamCoach,RemoveTeamAdmin,RemoveTeamCoach,RemoveTeamPlayer,EditTeamPlayer
        ,EditTeamAdmin,EditTeamCoach,BackUpAdmin,BackUpPlayer,BackUpCoach
        ,ConfirmEmailAdmin,ConfirmEmailCoach,ConfirmEmailPlayer,ImportDataAdmin
        ,ImportDataCoach,ImportDataPlayer,SendAvailablityCheckPlayer,SendAvailablityCheckCoach
        ,SendAvailablityCheckAdmin,ConfirmAvailablityAdmin,ConfirmAvailablityPlayer
        ,ConfirmAvailablityCoach,ViewAvailablityCoach,ViewAvailablityPlayer,ViewAvailablityAdmin
        ,PlayerStatsCoach,PlayerStatsPlayer,PlayerStatsAdmin):
            page_name = F.__name__
            frame = F(parent=container, controller=self)
            self.frames[page_name] = frame
            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame("Login")

    def show_frame(self, page_name):
        '''Show a frame for the given page name'''
        if Config.AccessLevel == "Admin":
            page_name=page_name+"Admin"
        elif Config.AccessLevel == "Coach":
            page_name=page_name+"Coach"
        else:
            page_name=page_name+"Player"

        frame = self.frames[page_name]
        PagesViewed.append(page_name)

        frame.tkraise()
        frame.tk_setPalette("#f4f8ff")
        frame.update()




if __name__ == "__main__":
    #System_init.FileCreation()

    app = SampleApp()
    app.title("Whichurch Hockey Club Team System")
    app.mainloop()