import datetime
import os
import json
import tkinter as tk
from tkinter import font  as tkfont
from tkinter import messagebox
from tkinter import ttk
import uuid
from MatchScreen import *
class ImportData:
    """
    Methods:
        ImportData

    """

    def ImportData(self,FileName):
        try:
            with open(FileName)as fp:
                File=fp.readlines()
        except FileNotFoundError:
            messagebox.showinfo("Error Message","File not found this that name")

        delimiter = ","
        TeamData={}
        MatchData= SystemToolKit.readFile(Config.MatchFile)


        for i ,j in enumerate(File):


            if i==0:
                HeaderRow = j.split(delimiter)

            else:

                Data={}

                rowData = j.split(delimiter)
                for m,n in enumerate(HeaderRow):

                    if n.lower() != "team":

                        Data[str(n)] = rowData[m]
                    else:
                        TeamID = SystemToolKit.getTeamId(rowData[m])
                        MatchID = str(uuid.uuid4())
                TeamData[MatchID] = Data

        MatchData[TeamID] =TeamData

        with open(Config.MatchFile,"w")as fp:
             json.dump(MatchData,fp)

class ImportDataAdmin(tk.Frame,ImportData):
    """
    Methods:
        __init__
    Variables:
        controller
        Title - Title Label Widget
        txtFileName - File Name Header Label Widget
        importButton - Import Button Widget
        BackButton - Back button Widget

    """

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller

        """ Widget Declearations """

        self.Title = tk.Label(self,text="Import Data",font= controller.title_font)
        self.txtFileName =ttk.Entry(self)
        self.importButton =tk.Button(self,text ="Import",command = lambda:self.ImportData(self.txtFileName.get()))
        self.BackButton= tk.Button(self, text="Back",command=lambda:SystemToolKit.BackButtonRun(controller))

        """ Widget Styligns """

        self.BackButton.config(compound="left",background="#307292",relief="flat",font=("Arial", 12, 'bold'),padx=5)
        self.Title.config(background="#8ABFD9",fg = "#404040",pady="5")
        self.importButton.config(compound="left",background="#307292",relief="flat",font=("Arial", 12, 'bold'),padx=5)

        """ Widget Positions """

        self.Title.grid(row=0,column=0)
        self.txtFileName.grid(row=1,column=0)
        self.importButton.grid(row=1,column=1)
        self.BackButton.grid(row=1,column=2)

class ImportDataCoach(tk.Frame,ImportData):
    """
    Methods:
        __init__
    Variables:
        controller
        Title - Title Label Widget
        txtFileName - File Name Header Label Widget
        importButton - Import Button Widget
        BackButton - Back button Widget

    """

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller

        """ Widget Declearations """

        """ Widget Stylings """

        """ Widget Positions """





class ImportDataPlayer(tk.Frame,ImportData):
    """
    Methods:
        __init__
    Variables:
        controller
        Title - Title Label Widget
        txtFileName - File Name Header Label Widget
        importButton - Import Button Widget
        BackButton - Back button Widget

    """

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller

        """ Widget Declearations """

        """ Widget Stylings """

        """ Widget Positions """