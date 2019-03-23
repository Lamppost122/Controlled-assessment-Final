import tkinter as tk
import json
import tkinter as tk
from tkinter import font  as tkfont
from tkinter import  messagebox
from tkinter import ttk
from SystemToolKit import *
from Login import *
import Config

class ConfirmEmail:

    def CheckConfirmEmail(self):

        with open(Config.UserFile)as fp:
            Data = json.load(fp)

        if Data[Config.CurrentUser]["Confirmation code"] == self.txtConfirm.get():
            Data[Config.CurrentUser]["ValidEmail"] = True
            self.controller.show_frame("Home")
            with open(Config.UserFile,"w") as fp:
                json.dump(Data,fp)
        else:
            messagebox.showinfo("Messgae","Code Incorrect")



class ConfirmEmailAdmin(tk.Frame,ConfirmEmail):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller

        """ Widget Declearations """

        self.title =tk.Label(self,text = "Confirm email" ,font = controller.title_font)
        self.lblText =tk.Label(self,text="Please enter in the code sent to your email address")
        self.txtConfirm =ttk.Entry(self)
        self.ConfirmButton=tk.Button(self,text ="Confirm",command=lambda:self.CheckConfirmEmail())

        """ Widget Stylings """

        self.title.config(background="#8ABFD9",fg = "#404040",pady="5")
        self.lblText.config(justify="right",fg = "black",background="#8ABFD9",font=("Arial", 10, 'bold'))
        self.ConfirmButton.config(compound="left",background="#307292",relief="flat",font=("Arial", 12, 'bold'),padx=5)

        """ Widget Positions """

        self.title.grid(row=0,column=0,columnspan = 2)
        self.lblText.grid(row=1,column=0,columnspan=2)
        self.txtConfirm.grid(row=2,column =0)
        self.ConfirmButton.grid(row=2,column =1 )

class ConfirmEmailPlayer(tk.Frame,ConfirmEmail):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller

        """ Widget Declearations """

        self.title =tk.Label(self,text = "Confirm email" ,font = controller.title_font)
        self.lblText =tk.Label(self,text="Please enter in the code sent to your email address")
        self.txtConfirm =ttk.Entry(self)
        self.ConfirmButton=tk.Button(self,text ="Confirm",command=lambda:self.CheckConfirmEmail())

        """ Widget Stylings """

        self.title.config(background="#8ABFD9",fg = "#404040",pady="5")
        self.lblText.config(justify="right",fg = "black",background="#8ABFD9",font=("Arial", 10, 'bold'))
        self.ConfirmButton.config(compound="left",background="#307292",relief="flat",font=("Arial", 12, 'bold'),padx=5)

        """ Widget Positions """

        self.title.grid(row=0,column=0,columnspan = 2)
        self.lblText.grid(row=1,column=0,columnspan=2)
        self.txtConfirm.grid(row=2,column =0)
        self.ConfirmButton.grid(row=2,column =1 )

class ConfirmEmailCoach(tk.Frame,ConfirmEmail):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller

        """ Widget Declearations """

        self.title =tk.Label(self,text = "Confirm email" ,font = controller.title_font)
        self.lblText =tk.Label(self,text="Please enter in the code sent to your email address")
        self.txtConfirm =ttk.Entry(self)
        self.ConfirmButton=tk.Button(self,text ="Confirm",command=lambda:self.CheckConfirmEmail())

        """ Widget Stlyings """

        self.title.config(background="#8ABFD9",fg = "#404040",pady="5")
        self.lblText.config(justify="right",fg = "black",background="#8ABFD9",font=("Arial", 10, 'bold'))
        self.ConfirmButton.config(compound="left",background="#307292",relief="flat",font=("Arial", 12, 'bold'),padx=5)

        """ Widget Positions """

        self.title.grid(row=0,column=0,columnspan = 2)
        self.lblText.grid(row=1,column=0,columnspan=2)
        self.txtConfirm.grid(row=2,column =0)
        self.ConfirmButton.grid(row=2,column =1 )
