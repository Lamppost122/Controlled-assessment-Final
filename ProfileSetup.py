import json
import tkinter as tk
from tkinter import font  as tkfont
from tkinter import messagebox
from tkinter import ttk
from Gui import *
import Config
class ProfileSetup:

    def BackButtonRun(self):
        Config.PagesViewed.pop()
        self.controller.show_previous_frame(Config.PagesViewed[-1])


    def getPlayerData(self):
        firstName = self.txtFirstName.get()
        lastName = self.txtLastName.get()
        phoneNumber = self.txtPhoneNumber.get()
        address = self.txtAddress.get()
        postCode = self.txtPostcode.get()
        DOB = self.txtDateOfBirth.get()

        return firstName , lastName, phoneNumber, address, postCode, DOB

    def addNewPlayer(self,controller):
        global CurrentUser
        firstName , lastName, phoneNumber, address, postCode, DOB = self.getPlayerData()

        data = {}
        players={}

        if Validation.FirstName(firstName)==True and Validation.LastName(lastName)and Validation.PhoneNumber(phoneNumber)==True and Validation.Address(address)==True and Validation.Postcode(postCode)==True and Validation.DateOfBirth( DOB) == True :


            players =SystemToolKit.readFile(Config.PlayerFile)
            data["First name"] = firstName
            data["Last name"] = lastName
            data["Phone number"] = phoneNumber
            data["Address"] = address
            data["Post code"] = postCode
            data["Date of Birth"] =DOB
            players[Config.CurrentUser] = data


            with open(Config.PlayerFile, 'w+') as fp:
                    json.dump(players, fp)

            controller.show_frame("Home")



class ProfileSetupPlayer(tk.Frame,ProfileSetup):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller

        """ Widget Declearations """

        self.lblFirstName= tk.Label(self,text=" First Name :")
        self.lblLastName= tk.Label(self,text=" Last Name :")
        self.lblPhoneNumber= tk.Label(self,text=" Phone Number :")
        self.lblAddress= tk.Label(self,text=" Address :")
        self.lblPostcode= tk.Label(self,text=" Postcode :")
        self.lblDateOfBirth= tk.Label(self,text=" Date of Birth :")
        self.txtFirstName = ttk.Entry(self)
        self.txtLastName = ttk.Entry(self)
        self.txtPhoneNumber = ttk.Entry(self)
        self.txtAddress = ttk.Entry(self)
        self.txtPostcode = ttk.Entry(self)
        self.txtDateOfBirth = ttk.Entry(self)
        self.SubmitButton= tk.Button(self, text="Submit",command=lambda: self.addNewPlayer(controller) )
        self.BackButton= tk.Button(self, text="Back",command=self.BackButtonRun)

        """ Widget Stylings """

        self.lblFirstName.config(justify="right",fg = "black",background="#8ABFD9",font=("Arial", 10, 'bold'))
        self.lblLastName.config(justify="right",fg = "black",background="#8ABFD9",font=("Arial", 10, 'bold'))
        self.lblPhoneNumber.config(justify="right",fg = "black",background="#8ABFD9",font=("Arial", 10, 'bold'))
        self.lblAddress.config(justify="right",fg = "black",background="#8ABFD9",font=("Arial", 10, 'bold'))
        self.lblPostcode.config(justify="right",fg = "black",background="#8ABFD9",font=("Arial", 10, 'bold'))
        self.lblDateOfBirth.config(justify="right",fg = "black",background="#8ABFD9",font=("Arial", 10, 'bold'))
        self.SubmitButton.config(compound="left",background="#307292",relief="flat",font=("Arial", 12, 'bold'),padx=5)
        self.BackButton.config(compound="left",background="#307292",relief="flat",font=("Arial", 12, 'bold'),padx=5)

        """ Widget Positions """

        self.lblFirstName.grid(row=1,column=0)
        self.lblLastName.grid(row=2,column=0)
        self.lblPhoneNumber.grid(row=3,column=0)
        self.lblAddress.grid(row=4,column=0)
        self.lblPostcode.grid(row=5,column=0)
        self.lblDateOfBirth.grid(row=6,column=0)
        self.txtFirstName.grid(row=1,column=1)
        self.txtLastName.grid(row=2,column=1)
        self.txtPhoneNumber.grid(row=3,column=1)
        self.txtAddress.grid(row=4,column=1)
        self.txtPostcode.grid(row=5,column=1)
        self.txtDateOfBirth.grid(row=6,column=1)
        self.SubmitButton.grid(row=8,column=0,columnspan=2)
        self.BackButton.grid(row=9,column = 0,columnspan = 2)

class ProfileSetupCoach(tk.Frame,ProfileSetup):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller

        """ Widget Declearations """

        self.SubmitButton= tk.Button(self, text="Submit",command=lambda: self.addNewPlayer(controller) )
        self.BackButton= tk.Button(self, text="Back",command=self.BackButtonRun)
        self.lblFirstName= tk.Label(self,text=" First Name :")
        self.lblLastName= tk.Label(self,text=" Last Name :")
        self.lblPhoneNumber= tk.Label(self,text=" Phone Number :")
        self.lblAddress= tk.Label(self,text=" Address :")
        self.lblPostcode= tk.Label(self,text=" Postcode :")
        self.lblDateOfBirth= tk.Label(self,text=" Date of Birth :")
        self.txtFirstName = ttk.Entry(self)
        self.txtLastName = ttk.Entry(self)
        self.txtPhoneNumber = ttk.Entry(self)
        self.txtAddress = ttk.Entry(self)
        self.txtPostcode = ttk.Entry(self)
        self.txtDateOfBirth = ttk.Entry(self)

        """ Widget Stylings """

        self.lblFirstName.config(justify="right",fg = "black",background="#8ABFD9",font=("Arial", 10, 'bold'))
        self.lblLastName.config(justify="right",fg = "black",background="#8ABFD9",font=("Arial", 10, 'bold'))
        self.lblPhoneNumber.config(justify="right",fg = "black",background="#8ABFD9",font=("Arial", 10, 'bold'))
        self.lblAddress.config(justify="right",fg = "black",background="#8ABFD9",font=("Arial", 10, 'bold'))
        self.lblPostcode.config(justify="right",fg = "black",background="#8ABFD9",font=("Arial", 10, 'bold'))
        self.lblDateOfBirth.config(justify="right",fg = "black",background="#8ABFD9",font=("Arial", 10, 'bold'))
        self.SubmitButton.config(compound="left",background="#307292",relief="flat",font=("Arial", 12, 'bold'),padx=5)
        self.BackButton.config(compound="left",background="#307292",relief="flat",font=("Arial", 12, 'bold'),padx=5)

        """ Widget Positions """

        self.lblFirstName.grid(row=1,column=0)
        self.lblLastName.grid(row=2,column=0)
        self.lblPhoneNumber.grid(row=3,column=0)
        self.lblAddress.grid(row=4,column=0)
        self.lblPostcode.grid(row=5,column=0)
        self.lblDateOfBirth.grid(row=6,column=0)
        self.txtFirstName.grid(row=1,column=1)
        self.txtLastName.grid(row=2,column=1)
        self.txtPhoneNumber.grid(row=3,column=1)
        self.txtAddress.grid(row=4,column=1)
        self.txtPostcode.grid(row=5,column=1)
        self.txtDateOfBirth.grid(row=6,column=1)
        self.SubmitButton.grid(row=8,column=0,columnspan=2)
        self.BackButton.grid(row=9,column = 0,columnspan = 2)

class ProfileSetupAdmin(tk.Frame,ProfileSetup):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller

        """ Widget Declearations """

        self.BackButton= tk.Button(self, text="Back",command=self.BackButtonRun)
        self.lblFirstName= tk.Label(self,text=" First Name :")
        self.lblLastName= tk.Label(self,text=" Last Name :")
        self.lblPhoneNumber= tk.Label(self,text=" Phone Number :")
        self.lblAddress= tk.Label(self,text=" Address :")
        self.lblPostcode= tk.Label(self,text=" Postcode :")
        self.lblDateOfBirth= tk.Label(self,text=" Date of Birth :")
        self.txtFirstName = ttk.Entry(self)
        self.txtLastName = ttk.Entry(self)
        self.txtPhoneNumber = ttk.Entry(self)
        self.txtAddress = ttk.Entry(self)
        self.txtPostcode = ttk.Entry(self)
        self.txtDateOfBirth = ttk.Entry(self)
        self.SubmitButton= tk.Button(self, text="Submit",command=lambda: self.addNewPlayer(controller) )

        """ Widget Stylings """

        self.lblFirstName.config(justify="right",fg = "black",background="#8ABFD9",font=("Arial", 10, 'bold'))
        self.lblLastName.config(justify="right",fg = "black",background="#8ABFD9",font=("Arial", 10, 'bold'))
        self.lblPhoneNumber.config(justify="right",fg = "black",background="#8ABFD9",font=("Arial", 10, 'bold'))
        self.lblAddress.config(justify="right",fg = "black",background="#8ABFD9",font=("Arial", 10, 'bold'))
        self.lblPostcode.config(justify="right",fg = "black",background="#8ABFD9",font=("Arial", 10, 'bold'))
        self.lblDateOfBirth.config(justify="right",fg = "black",background="#8ABFD9",font=("Arial", 10, 'bold'))
        self.SubmitButton.config(compound="left",background="#307292",relief="flat",font=("Arial", 12, 'bold'),padx=5)
        self.BackButton.config(compound="left",background="#307292",relief="flat",font=("Arial", 12, 'bold'),padx=5)

        """ Widget Positions """

        self.lblFirstName.grid(row=1,column=0)
        self.lblLastName.grid(row=2,column=0)
        self.lblPhoneNumber.grid(row=3,column=0)
        self.lblAddress.grid(row=4,column=0)
        self.lblPostcode.grid(row=5,column=0)
        self.lblDateOfBirth.grid(row=6,column=0)
        self.txtFirstName.grid(row=1,column=1)
        self.txtLastName.grid(row=2,column=1)
        self.txtPhoneNumber.grid(row=3,column=1)
        self.txtAddress.grid(row=4,column=1)
        self.txtPostcode.grid(row=5,column=1)
        self.txtDateOfBirth.grid(row=6,column=1)
        self.SubmitButton.grid(row=8,column=0,columnspan=2)
        self.BackButton.grid(row=9,column = 0,columnspan = 2)
