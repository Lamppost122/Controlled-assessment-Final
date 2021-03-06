import json
import hashlib
import email
import tkinter as tk
from tkinter import font  as tkfont
from tkinter import messagebox
from tkinter import ttk
from SystemToolKit import *
from Gui import *
import Config

class Login:
    """
    Methods:
        CheckDetails
        Check Passwords
        Check Username
    """

    def checkDetails(self):
        """
        Searches though the User file for any accounts that can met the login requirements
        These are:
            Check Password returns true
            Check Username returns true
        If these tests are passed the system then goes on to check if the email used to register the account has been confirmed if not the Confirm Email Frame will be open
        else the home page will be opened.


         """
        username = self.txtUsername.get()
        password = self.txtPassword.get()
        users = SystemToolKit.readFile(Config.UserFile)

        for j,i in enumerate(users):
            userHash = users[i]["Password"]
            salt = users[i]["Salt"]
            TestUsername = users[i]["Username"]
            if self.checkPassword(userHash,password,salt) == True and self.checkUsername(username,TestUsername) == True:
                Config.CurrentUser = i

                Config.AccessLevel = users[i]["AccessLevel"]
                if users[i]["ValidEmail"] == True :
                    self.controller.show_frame("Home")
                    break
                else :
                    self.controller.show_frame("ConfirmEmail")
                    break

            elif (j+1) == len(users):
                messagebox.showinfo("Message","Username or Password incorrect")
        if len(users) == 0:
            messagebox.showinfo("Message","No users installed")

    @staticmethod
    def checkPassword(userHash,password,salt):
        """
        Check if generated password has matches hash on record
        returns a boolean
        """
        if userHash  == hashlib.sha512(password.encode('utf-8') + salt.encode('utf-8')).hexdigest():
            return True
        else:
            return False
    @staticmethod
    def checkUsername(username,TestUserName):
        """
        Checks if username entered matches the correct username for the current account being checked
        returns a boolean
        """

        if username == TestUserName:
            return True
        else:
            return False

class LoginAdmin(tk.Frame,Login):
    """
    Methods:
        __init__

    Variable:
        controller
        Title - Title Label Widget
        loginButton -Login Button Widget
        registerButton  - Register Button Widget
        lblUsername -  Username Label Widget
        lblPassword - Password Label Widget
        txtUsername - Username Entry Widget
        txtPassword - Password Entry Widget

    """

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller

        """ Widget Declearations """

        self.Title = tk.Label(self, text="Please login to your account", font=controller.title_font)
        self.loginButton = tk.Button(self, text="Login",command= lambda:self.checkDetails())
        self.registerButton = tk.Button(self, text="Register",command=lambda: controller.show_frame("Register"))
        self.lblUsername = tk.Label(self,text="Username: ")
        self.lblPassword = tk.Label(self,text="Password: ")
        self.txtUsername = ttk.Entry(self)
        self.txtPassword = ttk.Entry(self)

        """ Widget Stylings """

        self.Title.config(background="#8ABFD9",fg = "#404040",pady="5")
        self.loginButton.config(compound="left",background="#307292",relief="flat",font=("Arial", 12, 'bold'),padx=5)
        self.registerButton.config(compound="left",background="#307292",relief="flat",font=("Arial", 12, 'bold'),padx=5)
        self.lblUsername.config(justify="right",fg = "black",background="#8ABFD9",font=("Arial", 10, 'bold'))
        self.lblPassword.config(justify="right",fg = "black",background="#8ABFD9",font=("Arial", 10, 'bold'))
        self.txtUsername.config(width="20")
        self.txtPassword.config(width="20",show="*")

        """ Widget  Positions """

        self.Title.grid(row=0,column=0,columnspan=2)
        self.loginButton.grid(row=4,column=1)
        self.registerButton.grid(row=4,column=0)
        self.lblUsername.grid(row=1,column=0)
        self.lblPassword.grid(row=2,column=0)
        self.txtUsername.grid(row=1,column = 1)
        self.txtPassword.grid(row=2,column = 1)

class LoginPlayer(tk.Frame,Login):
    """
    Methods:
        __init__

    Variable:
        controller
        Title - Title Label Widget
        loginButton -Login Button Widget
        registerButton  - Register Button Widget
        lblUsername -  Username Label Widget
        lblPassword - Password Label Widget
        txtUsername - Username Entry Widget
        txtPassword - Password Entry Widget

    """

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller

        """ Widget Declearations """

        self.Title = tk.Label(self, text="Please login to your account", font=controller.title_font)
        self.loginButton = tk.Button(self, text="Login",command= lambda:self.checkDetails())
        self.registerButton = tk.Button(self, text="Register",command=lambda: controller.show_frame("Register"))
        self.lblUsername = tk.Label(self,text="Username: ")
        self.lblPassword = tk.Label(self,text="Password: ")
        self.txtUsername = ttk.Entry(self)
        self.txtPassword = ttk.Entry(self)

        """ Widget Stylings """

        self.Title.config(background="#8ABFD9",fg = "#404040",pady="5")
        self.loginButton.config(compound="left",background="#307292",relief="flat",font=("Arial", 12, 'bold'),padx=5)
        self.registerButton.config(compound="left",background="#307292",relief="flat",font=("Arial", 12, 'bold'),padx=5)
        self.lblUsername.config(justify="right",fg = "black",background="#8ABFD9",font=("Arial", 10, 'bold'))
        self.lblPassword.config(justify="right",fg = "black",background="#8ABFD9",font=("Arial", 10, 'bold'))
        self.txtUsername.config(width="20")
        self.txtPassword.config(width="20",show="*")

        """ Widget Positions """

        self.Title.grid(row=0,column=0,columnspan=2)
        self.loginButton.grid(row=4,column=1)
        self.registerButton.grid(row=4,column=0)
        self.lblUsername.grid(row=1,column=0)
        self.lblPassword.grid(row=2,column=0)
        self.txtUsername.grid(row=1,column = 1)
        self.txtPassword.grid(row=2,column = 1)

class LoginCoach(tk.Frame,Login):
    """
    Methods:
        __init__

    Variable:
        controller
        Title - Title Label Widget
        loginButton -Login Button Widget
        registerButton  - Register Button Widget
        lblUsername -  Username Label Widget
        lblPassword - Password Label Widget
        txtUsername - Username Entry Widget
        txtPassword - Password Entry Widget

    """

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller

        """ Widget Declearations """

        self.Title = tk.Label(self, text="Please login to your account", font=controller.title_font)
        self.loginButton = tk.Button(self, text="Login",command= lambda:self.checkDetails())
        self.registerButton = tk.Button(self, text="Register",command=lambda: controller.show_frame("Register"))
        self.lblUsername = tk.Label(self,text="Username: ")
        self.lblPassword = tk.Label(self,text="Password: ")
        self.txtUsername = ttk.Entry(self)
        self.txtPassword = ttk.Entry(self)

        """ Widget Stylings """

        self.Title.config(background="#8ABFD9",fg = "#404040",pady="5")
        self.loginButton.config(compound="left",background="#307292",relief="flat",font=("Arial", 12, 'bold'),padx=5)
        self.registerButton.config(compound="left",background="#307292",relief="flat",font=("Arial", 12, 'bold'),padx=5)
        self.lblUsername.config(justify="right",fg = "black",background="#8ABFD9",font=("Arial", 10, 'bold'))
        self.lblPassword.config(justify="right",fg = "black",background="#8ABFD9",font=("Arial", 10, 'bold'))
        self.txtUsername.config(width="20")
        self.txtPassword.config(width="20",show="*")

        """ Widget Positions """

        self.Title.grid(row=0,column=0,columnspan=2)
        self.loginButton.grid(row=4,column=1)
        self.registerButton.grid(row=4,column=0)
        self.lblUsername.grid(row=1,column=0)
        self.lblPassword.grid(row=2,column=0)
        self.txtUsername.grid(row=1,column = 1)
        self.txtPassword.grid(row=2,column = 1)
