import json
import hashlib
import imaplib
import email
import tkinter as tk
from tkinter import font  as tkfont
from tkinter import messagebox
from tkinter import ttk
from SystemToolKit import *
from Gui import *
import Config
class Login:
    def checkDetails(self,controller):
        global CurrentUser, AccessLevel
        username = self.txtUsername.get()
        password = self.txtPassword.get()
        users = SystemToolKit.readFile(Config.UserFile)




        for j,i in enumerate(users):
            userHash = users[i]["Password"]
            salt = users[i]["Salt"]
            if self.checkPassword(userHash,password,salt) == True:
                Config.CurrentUser = i

                Config.AccessLevel = users[i]["AccessLevel"]
                if users[i]["ValidEmail"] == True :
                    controller.show_frame("Home")
                    break
                else :
                    controller.show_frame("ConfirmEmail")
                    break

            elif (j+1) == len(users):
                messagebox.showinfo("Message","Username or password incorrect")
        if len(users) == 0:
            messagebox.showinfo("Message","No users installed")

    @staticmethod
    def checkPassword(userHash,password,salt):
        if userHash  == hashlib.sha512(password.encode('utf-8') + salt.encode('utf-8')).hexdigest():
            return True
        else:
            return False


    def ValidateEmail(self,UserID):
        with open('data.json', 'r') as fp:
                users = json.load(fp)
        inbox = self.read_Email()

        for i in inbox:
            if i.keys()[0] == str(users[UserID]["Email"]):
                users[UserID]["ValidEmail"] = True
                with open(Config.UserFile, 'w+') as fp:
                    json.dump(users, fp)


    def read_Email(self):
            ORG_EMAIL   = "@gmail.com"
            FROM_EMAIL  = "ComputerScienceTest1" + ORG_EMAIL
            FROM_PWD    = "Password1@"
            SMTP_SERVER = "imap.gmail.com"
            SMTP_PORT   = 993
            mail = imaplib.IMAP4_SSL(SMTP_SERVER)
            mail.login(FROM_EMAIL,FROM_PWD)
            mail.select('inbox')

            type, data = mail.search(None, 'ALL')
            mail_ids = data[0]

            id_list = mail_ids.split()
            first_email_id = int(id_list[0])
            latest_email_id = int(id_list[-1])

            inbox = []

            for i in range(latest_email_id,first_email_id, -1):
                typ, data = mail.fetch(i, '(RFC822)' )

                for response_part in data:
                    if isinstance(response_part, tuple):
                        msg = email.message_from_string(response_part[1])
                        email_subject = msg['subject']
                        Emails =email_subject.split("|")
                        try:
                            Data = {Emails[1]:Emails[0]}
                            inbox.append(Data)
                        except:IndexError

            return inbox

class LoginAdmin(tk.Frame,Login):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.Title = tk.Label(self, text="Please login to your account", font=controller.title_font)
        self.loginButton = tk.Button(self, text="Login",command= lambda:self.checkDetails(controller))
        self.registerButton = tk.Button(self, text="Register",command=lambda: controller.show_frame("Register"))
        self.lblUsername = tk.Label(self,text="Username: ")
        self.lblPassword = tk.Label(self,text="Password: ")
        self.txtUsername = ttk.Entry(self)
        self.txtPassword = ttk.Entry(self)



        self.Title.config(background="#8ABFD9",fg = "#404040",pady="5")
        self.loginButton.config(compound="left",background="#307292",relief="flat",font=("Arial", 12, 'bold'),padx=5)
        self.registerButton.config(compound="left",background="#307292",relief="flat",font=("Arial", 12, 'bold'),padx=5)
        self.lblUsername.config(justify="right",fg = "black",background="#8ABFD9",font=("Arial", 10, 'bold'))
        self.lblPassword.config(justify="right",fg = "black",background="#8ABFD9",font=("Arial", 10, 'bold'))
        self.txtUsername.config(width="20")
        self.txtPassword.config(width="20",show="*")


        self.Title.grid(row=0,column=0,columnspan=2)
        self.loginButton.grid(row=4,column=1)
        self.registerButton.grid(row=4,column=0)
        self.lblUsername.grid(row=1,column=0)
        self.lblPassword.grid(row=2,column=0)
        self.txtUsername.grid(row=1,column = 1)
        self.txtPassword.grid(row=2,column = 1)

class LoginPlayer(tk.Frame,Login):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.Title = tk.Label(self, text="Please login to your account", font=controller.title_font)
        self.loginButton = tk.Button(self, text="Login",command= lambda:self.checkDetails(controller))
        self.registerButton = tk.Button(self, text="Register",command=lambda: controller.show_frame("Register"))
        self.lblUsername = tk.Label(self,text="Username: ")
        self.lblPassword = tk.Label(self,text="Password: ")
        self.txtUsername = ttk.Entry(self)
        self.txtPassword = ttk.Entry(self)

        self.Title.config(background="#8ABFD9",fg = "#404040",pady="5")
        self.loginButton.config(compound="left",background="#307292",relief="flat",font=("Arial", 12, 'bold'),padx=5)
        self.registerButton.config(compound="left",background="#307292",relief="flat",font=("Arial", 12, 'bold'),padx=5)
        self.lblUsername.config(justify="right",fg = "black",background="#8ABFD9",font=("Arial", 10, 'bold'))
        self.lblPassword.config(justify="right",fg = "black",background="#8ABFD9",font=("Arial", 10, 'bold'))
        self.txtUsername.config(width="20")
        self.txtPassword.config(width="20",show="*")

        self.Title.grid(row=0,column=0,columnspan=2)
        self.loginButton.grid(row=4,column=1)
        self.registerButton.grid(row=4,column=0)
        self.lblUsername.grid(row=1,column=0)
        self.lblPassword.grid(row=2,column=0)
        self.txtUsername.grid(row=1,column = 1)
        self.txtPassword.grid(row=2,column = 1)

class LoginCoach(tk.Frame,Login):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.Title = tk.Label(self, text="Please login to your account", font=controller.title_font)
        self.loginButton = tk.Button(self, text="Login",command= lambda:self.checkDetails(controller))
        self.registerButton = tk.Button(self, text="Register",command=lambda: controller.show_frame("Register"))
        self.lblUsername = tk.Label(self,text="Username: ")
        self.lblPassword = tk.Label(self,text="Password: ")
        self.txtUsername = ttk.Entry(self)
        self.txtPassword = ttk.Entry(self)

        self.Title.config(background="#8ABFD9",fg = "#404040",pady="5")
        self.loginButton.config(compound="left",background="#307292",relief="flat",font=("Arial", 12, 'bold'),padx=5)
        self.registerButton.config(compound="left",background="#307292",relief="flat",font=("Arial", 12, 'bold'),padx=5)
        self.lblUsername.config(justify="right",fg = "black",background="#8ABFD9",font=("Arial", 10, 'bold'))
        self.lblPassword.config(justify="right",fg = "black",background="#8ABFD9",font=("Arial", 10, 'bold'))
        self.txtUsername.config(width="20")
        self.txtPassword.config(width="20",show="*")

        self.Title.grid(row=0,column=0,columnspan=2)
        self.loginButton.grid(row=4,column=1)
        self.registerButton.grid(row=4,column=0)
        self.lblUsername.grid(row=1,column=0)
        self.lblPassword.grid(row=2,column=0)
        self.txtUsername.grid(row=1,column = 1)
        self.txtPassword.grid(row=2,column = 1)

