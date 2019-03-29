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
    def BackButtonRun(self):
            Config.PagesViewed.pop()
            self.controller.show_previous_frame(Config.PagesViewed[-1])

    def ImportData(FileName,DataFileName):
        with open(DataFileName)as fp:
            FileData=json.load(fp)
        with open(FileName)as fp:
            File=fp.readlines()

        delimiter = ","
        TeamNumber= 0
        for i ,j in enumerate(File):

            if i==0:
                HeaderRow = j.split(delimiter)
                for m,n in enumerate(HeaderRow):
                    if n.lower() == "team":
                        TeamNumber = m +1

            else:
                rowData = j.split(delimiter)
                Data={}
                TeamData = {}
                for k,l in enumerate(rowData):
                    if k ==TeamNumber:
                        TeamID = MatchScreen.GetTeamID(TeamNumber)
                    else:

                        Data[HeaderRow[k]]= l
                TeamData[str(uuid.uuid4())] = Data

                FileData[TeamID] = TeamData
        with open(FileName,"w")as fp:
             json.dump(FileData,fp)

class ImportDataAdmin(tk.Frame,ImportData):

        def __init__(self, parent, controller):
            tk.Frame.__init__(self, parent)
            self.controller = controller

            """ Widget Declearations """

            self.Title = tk.Label(self,text="Import Data",font= controller.title_font)
            self.txtFileName =ttk.Entry(self)
            self.importButton =tk.Button(self,text ="Import")
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

        def __init__(self, parent, controller):
            tk.Frame.__init__(self, parent)
            self.controller = controller

            """ Widget Declearations """

            """ Widget Stylings """

            """ Widget Positions """





class ImportDataPlayer(tk.Frame,ImportData):

        def __init__(self, parent, controller):
            tk.Frame.__init__(self, parent)
            self.controller = controller

            """ Widget Declearations """

            """ Widget Stylings """

            """ Widget Positions """
