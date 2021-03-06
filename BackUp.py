import os
import json
import tkinter as tk
from tkinter import font  as tkfont
from tkinter import messagebox
from tkinter import ttk
import shutil
import datetime
import Config
from SystemToolKit import *

class BackUp:
    """
    Methods:
        writeToScreen
        createBackUp
        Child
        Parent
        Grandparent
        RecoveryName
        RecoverBackup
    """

    def writeToScreen(self,FileName):
        """
        Writes a json file of backups to the PastBackUpdList Widget
        """
        self.PastBackupsList.delete(0,tk.END)
        with open(FileName)as fp:
            Data = json.load(fp)
        for i in Data:
            self.PastBackupsList.insert(0,i)

    def createBackUp(self,FileName):
        """
        Creates a new set of backup and updates the BackupListFile
        """
        with open(FileName)as fp:
            Data = json.load(fp)
        today = datetime.datetime.today()
        today = today.strftime("%d/%m/%y-%H:%M")
        FileType = ["Child","Parent","Grandparent"]
        Names = []

        for i in FileType:
            for j in Data[i]:

                if i == "Child":
                    NewName = self.Child(j)

                if i =="Parent":
                    NewName=self.Parent(j)
                if i == "Grandparent":
                    NewName =self.GrandParent(j)

                shutil.copy(j,NewName)
                Names.append(NewName)

            if i =="Child":
                Data["Parent"] = Names
            if i == "Parent":
                Data["Grandparent"] = Names
            if i =="Grandparent":
                Data[today] = Names

            Names = []

        with open(FileName,"w")as fp:
            json.dump(Data,fp)

    def Child(self,FileName):
        """
        Convers a child backup file name to a parent backup file name
        Returns a Parent File name(String)
        """
        SplitName = FileName.split(".")
        SplitName.insert(1,"-Parent")
        NewName = SplitName[0]+ SplitName[1]+ "."+SplitName[2]
        return NewName

    def Parent(self,FileName):
        """
        Converts a Parent backup file name to a grandparent backup file name
        returns a Grandparent file name(String)
        """
        SplitName = FileName.split(".")
        DoubleSplitName = []
        for i in SplitName:
            DoubleSplitName.append(i.split("-"))
        DoubleSplitName[0][1] = "-GrandParent"
        NewName = str(DoubleSplitName[0][0])+ str(DoubleSplitName[0][1])+"."+ str(DoubleSplitName[1][0])
        return NewName

    def GrandParent(self,FileName):
        """
        Converts a Grandparent backup File Name to a post-Grandparent Backup File Name
        returns a post-Grandparent Backup File Name(string)
        """

        SplitName = FileName.split(".")
        DoubleSplitName = []
        for i in SplitName:
            DoubleSplitName.append(i.split("-"))
        date =datetime.datetime.today()
        dateFormate =  datetime.datetime.strftime(date,"-%d%B%Y")
        DoubleSplitName[0][1] = dateFormate

        NewName = str(DoubleSplitName[0][0])+ str(DoubleSplitName[0][1])+"."+ str(DoubleSplitName[1][0])
        return NewName

    def RecoveryName(self,FileName):
        """
        Converts a Backup File name to a child Backup file name
        returns a child Backup file name(String)
        """

        SplitName = FileName.split(".")
        DoubleSplitName = []
        for i in SplitName:
            DoubleSplitName.append(i.split("-"))
        NewName = str(DoubleSplitName[0][0])+"."+ str(DoubleSplitName[1][0])
        return NewName


    def RecoverBackUp(self,FileName):
        """
        Search the Backup file list and converts a choosen backup file to a current file
        Updates the Backup file list
        """
        with open(FileName)as fp:
            Data = json.load(fp)

        AnchorValue = self.PastBackupsList.get(tk.ANCHOR)

        if AnchorValue !="Child" and AnchorValue !="":

            Names = []
            for i in Data[AnchorValue]:
                NewName = self.RecoveryName(i)
                shutil.copy(i,NewName)
                Names.append(NewName)
            Data["Child"] = Names

            Names = []
            with open(FileName,"w")as fp:
                json.dump(Data,fp)

class BackUpAdmin(tk.Frame,BackUp):
    """
    Method:
        __init__
    Variables:
        controller
        Title - Title Label Widget
        PastBackupsList  - Past Back ups Listbox Widget
        getBackupListButton  - Get BackUp Button Widget
        createBackUpButton - Create BackUp Button Widget
        recoverBackUpButton  - Recover BackUp Button Widget
        BackButton - Back Button Widget
    """

    def __init__(self, parent, controller):
        """
        Initalises a frame instance of BackUp At Admin Access Level
        """
        tk.Frame.__init__(self, parent)
        self.controller = controller

        """ Widget Declearations """

        self.Title =tk.Label(self,text="BackUps",font = controller.title_font)
        self.PastBackupsList = tk.Listbox(self)
        self.getBackupListButton = tk.Button(self,text="Get Back Ups",command = lambda: self.writeToScreen(Config.BackupListFile))
        self.createBackUpButton = tk.Button(self,text="Create Back up",command =lambda: self.createBackUp(Config.BackupListFile))
        self.recoverBackUpButton = tk.Button(self,text="Recover Back up",command =lambda: self.RecoverBackUp(Config.BackupListFile))
        self.BackButton = tk.Button(self,text = "Back",command = lambda:SystemToolKit.BackButtonRun(controller))

        """ Widget Stylings """

        self.Title.config(background="#8ABFD9",fg = "#404040",pady="5")
        self.getBackupListButton.config(compound="left",background="#307292",relief="flat",font=("Arial", 12, 'bold'),padx=5)
        self.createBackUpButton.config(compound="left",background="#307292",relief="flat",font=("Arial", 12, 'bold'),padx=5)
        self.recoverBackUpButton.config(compound="left",background="#307292",relief="flat",font=("Arial", 12, 'bold'),padx=5)
        self.BackButton.config(compound="left",background="#307292",relief="flat",font=("Arial", 12, 'bold'),padx=5)
        self.PastBackupsList.config(background="white")

        """ Widget Positions """

        self.Title.grid(row = 0,column =0,columnspan=2)
        self.PastBackupsList.grid(row= 1,column= 0,rowspan=4)
        self.getBackupListButton.grid(row = 1,column =1)
        self.createBackUpButton.grid(row=2,column = 1)
        self.recoverBackUpButton.grid(row=3,column = 1)
        self.BackButton.grid(row=4,column=1)


class BackUpPlayer(tk.Frame,BackUp):
    """
    Method:
        __init__
    Variables:
        controller

    """

    def __init__(self, parent, controller):
        """
        Initalises a frame instance of BackUp At Player Access Level
        """
        tk.Frame.__init__(self, parent)
        self.controller = controller

        """ Widget Declearations """

        """ Widget Stlyings """

        """ Widget Positions """


class BackUpCoach(tk.Frame,BackUp):
    """
    Method:
        __init__
    Variables:
        controller

    """

    def __init__(self, parent, controller):
        """
        Initalises a frame instance of BackUp At Coach Access Level
        """
        tk.Frame.__init__(self, parent)
        self.controller = controller

        """ Widget Declearations """

        """ Widget Stlyings """

        """ Widget Positions """
