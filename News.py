import json
import tkinter as tk
from tkinter import font  as tkfont
from tkinter import messagebox
from tkinter import ttk
from Gui import *
import Config
class News:

    def write_News_to_screen(self):
        updates = SystemToolKit.readFile(Config.UpdatesFile)
        try:
            j.grid_forget()
            k.grid_forget()
        except UnboundLocalError:
            pass

        for i in updates:


            """ Widget Declearations """

            j = tk.Label(self,text = updates[i]["Data"])
            k = tk.Label(self,text= "Update: "+updates[i]["Date"])

            """ Widget Stylings """

            j.config(justify="right",fg = "black",background="#8ABFD9",font=("Arial", 10, 'bold'))
            k.config(justify="right",fg = "black",background="#8ABFD9",font=("Arial", 10, 'bold'))

            """ Widget Positions """

            j.grid(row = 2 *(len(updates)-int(i)+self.startCount),column  =0,columnspan=2)
            k.grid(row =2 *(len(updates)-int(i)+self.startCount) + 1,column  =0,columnspan=2)

class NewsAdmin(tk.Frame,News):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.startCount = 3

        """ Widget Declearations """

        self.Title = tk.Label(self,text ="News/Updates",font = controller.title_font)
        self.BackButton= tk.Button(self, text="Back",command=lambda:SystemToolKit.BackButtonRun(controller))
        self.GetUpdatesButton =tk.Button(self,text="Get Updates",command=lambda:self.write_News_to_screen())

        """ Widget Stylings """

        self.Title.config(background="#8ABFD9",fg = "#404040",pady="5")
        self.BackButton.config(compound="left",background="#307292",relief="flat",font=("Arial", 12, 'bold'),padx=5)
        self.GetUpdatesButton.config(compound="left",background="#307292",relief="flat",font=("Arial", 12, 'bold'),padx=5)

        """ Widget Positions """

        self.Title.grid(row =0,column =0,columnspan = 2  )
        self.BackButton.grid(row =1,column = 1)
        self.GetUpdatesButton.grid(row=1,column=0)


class NewsCoach(tk.Frame,News):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.startCount = 3

        """ Widget Declearations """

        self.Title = tk.Label(self,text ="News/Updates",font = controller.title_font)
        self.BackButton= tk.Button(self, text="Back",command=lambda:SystemToolKit.BackButtonRun(controller))
        self.GetUpdatesButton =tk.Button(self,text="Get Updates",command=lambda:self.write_News_to_screen())

        """ Widget Stylings """

        self.Title.config(background="#8ABFD9",fg = "#404040",pady="5")
        self.BackButton.config(compound="left",background="#307292",relief="flat",font=("Arial", 12, 'bold'),padx=5)
        self.GetUpdatesButton.config(compound="left",background="#307292",relief="flat",font=("Arial", 12, 'bold'),padx=5)

        """ Widget Positions """

        self.Title.grid(row =0,column =0,columnspan = 2  )
        self.BackButton.grid(row =1,column = 1)
        self.GetUpdatesButton.grid(row=1,column=0)

class NewsPlayer(tk.Frame,News):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.startCount = 3

        """ Widget Declearations """

        self.Title = tk.Label(self,text ="News/Updates",font = controller.title_font)
        self.BackButton= tk.Button(self, text="Back",command=lambda:SystemToolKit.BackButtonRun(controller))
        self.GetUpdatesButton =tk.Button(self,text="Get Updates",command=lambda:self.write_News_to_screen())

        """ Widget Stylings """

        self.Title.config(background="#8ABFD9",fg = "#404040",pady="5")
        self.BackButton.config(compound="left",background="#307292",relief="flat",font=("Arial", 12, 'bold'),padx=5)
        self.GetUpdatesButton.config(compound="left",background="#307292",relief="flat",font=("Arial", 12, 'bold'),padx=5)

        """ Widget Positions """

        self.Title.grid(row =0,column =0,columnspan = 2  )
        self.BackButton.grid(row =1,column = 1)
        self.GetUpdatesButton.grid(row=1,column=0)