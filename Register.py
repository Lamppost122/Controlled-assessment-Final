import tkinter as tk
import json
import smtplib
import uuid
import hashlib
import tkinter as tk
from tkinter import font  as tkfont
from tkinter import  messagebox
from tkinter import ttk
from SystemToolKit import *
from Gui import *
from Validation import 
from email.MIMEMultipart import MIMEMultipart
from email.MIMEText import MIMEText
import random
import  Config

class Register:
    """
    Methods:
        registers
        getRegisterData
        addNewUser
        sendEmailConformation
    Variables:
        username - Contain a username(string)
        confirmUsername - Contains a confirmUser Name(string)
        password - Contains a Password(string)
        confirmPassword - Contains a Confirm Password(string)
        Email - Contains a Email Address(string)
        accessLevel - Contains a access Level(string)
        ValidEmail - Contains a ValdidEmail(boolean)
        confirmationCode - contains a confirmation code(integer)

    """

    def registers(self):
        """
        If the data passes the valiatin a new user in created and added to the user file
        calls the login frame """
        self.getRegisterData()
        error = self.addNewUser()
        if error == False:
            self.sendEmailConformation()
            messagebox.showinfo("Message","Thank you for registring with us. You will need to confirm your email")
            self.controller.show_frame("Login")


    def getRegisterData(self):
        """Get the data from the screen """

        self.username =  self.txtUsername.get()
        self.confirmUsername = self.txtConfirmUsername.get()
        self.password = self.txtPassword.get()
        self.confirmPassword = self.txtConfirmPassword.get()
        self.Email = self.txtEmail.get()
        self.accessLevel = self.var.get()
        self.ValidEmail = False
        self.confirmationCode = str(random.randint(10000,99999))



    def addNewUser(self):
        """Adds a new user to the user file  """

        data = {}
        users={}
        error = False
        if Validation.Username(self.username)==True and Validation.Password(self.password)==True and Validation.Email(self.Email) == True:
            if self.username == self.confirmUsername:
                if self.password == self.confirmPassword :

                    users = SystemToolKit.readFile(Config.UserFile)
                    salt = uuid.uuid4().hex
                    hashed_password = hashlib.sha512(self.password.encode('utf-8') + salt.encode('utf-8')).hexdigest()
                    userID = str(uuid.uuid4())
                    data["Username"] = self.username
                    data["Password"] = hashed_password
                    data["Salt"] = salt
                    data["Email"] = self.Email
                    data["AccessLevel"] = self.accessLevel
                    data["ValidEmail"] = self.ValidEmail
                    data["Confirmation code"] = self.confirmationCode
                    users[userID] = data
                    with open(Config.UserFile, 'w+') as fp:
                        json.dump(users, fp)
                else:
                    messagebox.showinfo("Invalid Data","Password and confirm Password do not match ")
                    error = True
            else:
                messagebox.showinfo("Invalid Data","Username and confirm username do not match")
                error = True
        else:
            print("x")
            error = True
        return error



    def sendEmailConformation(self):
        """Sends out a confirmation code """

        msg = MIMEMultipart()
        text = "Confirmation code: "
        body = text + self.confirmationCode
        msg['Subject'] = "Comfirm email"
        msg.attach(MIMEText(body, 'html'))
        text = msg.as_string()
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login(Config.EmailAddress, Config.EmailPassword)
        server.sendmail(Config.EmailAddress, self.Email, text)
        server.quit()



class RegisterAdmin(tk.Frame,Register):
    """
    Methods:
        __init__
    Variables:
        controller
        Title - Title Label Widget
        loginButton - Login Button Widget
        registerButton - Register Button Widget
        lblUsername  - Username Label Widget
        lblPassword -   Password Label Widget
        lblConfirmUsername - Confirm Username Label Widget
        lblConfirmPassword - Confrim Password Label Widget
        lblEmail - Email Label Widget
        txtUsername - Username Entry widget
        txtConfirmUsername  - Confirm Username Entry widget
        txtPassword - Password Entry widget
        txtConfirmPassword - Confirm Password Entry widget
        txtEmail - Email Entry widget
        lblAccessLevel  -Access Level Label Widget
        var - Contains the cmbAccessLevel options
        cmbAccessLevel - Acces Level Option Menu Widget

    """

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller

        """ Widget Declearations """

        self.Title = tk.Label(self, text="Please fill in your details", font=controller.title_font)
        self.loginButton = tk.Button(self, text="Login",command=lambda: controller.show_frame("Login") )
        self.registerButton = tk.Button(self, text="Register",command=lambda: self.registers())
        self.lblUsername = tk.Label(self,text="Username: ")
        self.lblPassword = tk.Label(self,text="Password: ")
        self.lblConfirmUsername = tk.Label(self,text="Confirm Username: ")
        self.lblConfirmPassword = tk.Label(self,text="Confirm Password: ")
        self.lblEmail = tk.Label(self,text="Email: ")
        self.txtUsername = ttk.Entry(self)
        self.txtConfirmUsername = ttk.Entry(self)
        self.txtPassword = ttk.Entry(self)
        self.txtConfirmPassword = ttk.Entry(self)
        self.txtEmail = ttk.Entry(self)
        self.lblAccessLevel = tk.Label(self,text = "Position: ")
        self.var = tk.StringVar()
        options = ["Player","Coach/Captin","Admin"]
        self.var.set(options[0])
        self.cmbAccessLevel = tk.OptionMenu(self, self.var,*options)

        """ Widget Stylings """

        self.txtPassword.config(width="20",show="*")
        self.txtConfirmPassword.config(width="20",show="*")
        self.lblUsername.config(justify="right",fg = "black",background="#8ABFD9",font=("Arial", 10, 'bold'))
        self.lblPassword.config(justify="right",fg = "black",background="#8ABFD9",font=("Arial", 10, 'bold'))
        self.lblConfirmUsername.config(justify="right",fg = "black",background="#8ABFD9",font=("Arial", 10, 'bold'))
        self.lblConfirmPassword.config(justify="right",fg = "black",background="#8ABFD9",font=("Arial", 10, 'bold'))
        self.lblEmail.config(justify="right",fg = "black",background="#8ABFD9",font=("Arial", 10, 'bold'))
        self.loginButton.config(compound="left",background="#307292",relief="flat",font=("Arial", 12, 'bold'),padx=5)
        self.registerButton.config(compound="left",background="#307292",relief="flat",font=("Arial", 12, 'bold'),padx=5)
        self.Title.config(background="#8ABFD9",fg = "#404040",pady="5")

        """ Widget Positions """

        self.txtUsername.grid(row=1,column = 1)
        self.txtConfirmUsername.grid(row=2,column = 1)
        self.txtPassword.grid(row=3,column = 1)
        self.txtConfirmPassword.grid(row=4,column = 1)
        self.txtEmail.grid(row=5,column = 1)
        self.loginButton.grid(row=7,column = 0)
        self.registerButton.grid(row=7,column = 1)
        self.lblUsername.grid(row=1,column = 0)
        self.lblConfirmUsername.grid(row=2,column = 0)
        self.lblPassword.grid(row=3,column = 0)
        self.lblConfirmPassword.grid(row=4,column = 0)
        self.lblEmail.grid(row=5,column = 0)
        self.Title.grid(row=0,column = 0,columnspan=8)
        self.lblAccessLevel.grid(row=6,column =0 )
        self.cmbAccessLevel.grid(row=6,column = 1)

class RegisterCoach(tk.Frame,Register):
    """
    Methods:
        __init__
    Variables:
        controller
        Title - Title Label Widget
        loginButton - Login Button Widget
        registerButton - Register Button Widget
        lblUsername  - Username Label Widget
        lblPassword -   Password Label Widget
        lblConfirmUsername - Confirm Username Label Widget
        lblConfirmPassword - Confrim Password Label Widget
        lblEmail - Email Label Widget
        txtUsername - Username Entry widget
        txtConfirmUsername  - Confirm Username Entry widget
        txtPassword - Password Entry widget
        txtConfirmPassword - Confirm Password Entry widget
        txtEmail - Email Entry widget
        lblAccessLevel  -Access Level Label Widget
        var - Contains the cmbAccessLevel options
        cmbAccessLevel - Acces Level Option Menu Widget
    """

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller

        """ Widget Declearations """

        self.Title = tk.Label(self, text="Please fill in your details", font=controller.title_font)
        self.loginButton = tk.Button(self, text="Login",command=lambda: controller.show_frame("Login") )
        self.registerButton = tk.Button(self, text="Register",command=lambda: self.registers())
        self.lblUsername = tk.Label(self,text="Username: ")
        self.lblPassword = tk.Label(self,text="Password: ")
        self.lblConfirmUsername = tk.Label(self,text="Confirm Username: ")
        self.lblConfirmPassword = tk.Label(self,text="Confirm Password: ")
        self.lblEmail = tk.Label(self,text="Email: ")
        self.txtUsername = ttk.Entry(self)
        self.txtConfirmUsername = ttk.Entry(self)
        self.txtPassword = ttk.Entry(self)
        self.txtConfirmPassword = ttk.Entry(self)
        self.txtEmail = ttk.Entry(self)
        self.lblAccessLevel = tk.Label(self,text = "Position: ")
        self.var = tk.StringVar()
        options = ["Player","Coach/Captin","Admin"]
        self.var.set(options[0])
        self.cmbAccessLevel = tk.OptionMenu(self, self.var,*options)

        """ Widget Stylings """

        self.txtPassword.config(width="20",show="*")
        self.txtConfirmPassword.config(width="20",show="*")
        self.lblUsername.config(justify="right",fg = "black",background="#8ABFD9",font=("Arial", 10, 'bold'))
        self.lblPassword.config(justify="right",fg = "black",background="#8ABFD9",font=("Arial", 10, 'bold'))
        self.lblConfirmUsername.config(justify="right",fg = "black",background="#8ABFD9",font=("Arial", 10, 'bold'))
        self.lblConfirmPassword.config(justify="right",fg = "black",background="#8ABFD9",font=("Arial", 10, 'bold'))
        self.lblAccessLevel.config(justify="right",fg = "black",background="#8ABFD9",font=("Arial", 10, 'bold'))
        self.lblEmail.config(justify="right",fg = "black",background="#8ABFD9",font=("Arial", 10, 'bold'))
        self.loginButton.config(compound="left",background="#307292",relief="flat",font=("Arial", 12, 'bold'),padx=5)
        self.registerButton.config(compound="left",background="#307292",relief="flat",font=("Arial", 12, 'bold'),padx=5)
        self.Title.config(background="#8ABFD9",fg = "#404040",pady="5")

        """ Widget Positions """

        self.txtUsername.grid(row=1,column = 1)
        self.txtConfirmUsername.grid(row=2,column = 1)
        self.txtPassword.grid(row=3,column = 1)
        self.txtConfirmPassword.grid(row=4,column = 1)
        self.txtEmail.grid(row=5,column = 1)
        self.loginButton.grid(row=7,column = 0)
        self.registerButton.grid(row=7,column = 1)
        self.lblUsername.grid(row=1,column = 0)
        self.lblConfirmUsername.grid(row=2,column = 0)
        self.lblPassword.grid(row=3,column = 0)
        self.lblConfirmPassword.grid(row=4,column = 0)
        self.lblEmail.grid(row=5,column = 0)
        self.Title.grid(row=0,column = 0,columnspan=2)
        self.lblAccessLevel.grid(row=6,column =0 )
        self.cmbAccessLevel.grid(row=6,column = 1)

class RegisterPlayer(tk.Frame,Register):
    """
    Methods:
        __init__
    Variables:
        controller
        Title - Title Label Widget
        loginButton - Login Button Widget
        registerButton - Register Button Widget
        lblUsername  - Username Label Widget
        lblPassword -   Password Label Widget
        lblConfirmUsername - Confirm Username Label Widget
        lblConfirmPassword - Confrim Password Label Widget
        lblEmail - Email Label Widget
        txtUsername - Username Entry widget
        txtConfirmUsername  - Confirm Username Entry widget
        txtPassword - Password Entry widget
        txtConfirmPassword - Confirm Password Entry widget
        txtEmail - Email Entry widget
        lblAccessLevel  -Access Level Label Widget
        var - Contains the cmbAccessLevel options
        cmbAccessLevel - Acces Level Option Menu Widget
    """

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller

        """ Widget Declearations """

        self.Title = tk.Label(self, text="Please fill in your details", font=controller.title_font)
        self.loginButton = tk.Button(self, text="Login",command=lambda: controller.show_frame("Login") )
        self.registerButton = tk.Button(self, text="Register",command= lambda:self.registers())
        self.lblUsername = tk.Label(self,text="Username: ")
        self.lblPassword = tk.Label(self,text="Password: ")
        self.lblConfirmUsername = tk.Label(self,text="Confirm Username: ")
        self.lblConfirmPassword = tk.Label(self,text="Confirm Password: ")
        self.lblEmail = tk.Label(self,text="Email: ")
        self.txtUsername = ttk.Entry(self)
        self.txtConfirmUsername = ttk.Entry(self)
        self.txtPassword = ttk.Entry(self)
        self.txtConfirmPassword = ttk.Entry(self)
        self.txtEmail = ttk.Entry(self)
        self.lblAccessLevel = tk.Label(self,text = "Position: ")
        self.var = tk.StringVar()
        options = ["Player","Coach/Captin","Admin"]
        self.var.set(options[0])
        self.cmbAccessLevel = tk.OptionMenu(self, self.var,*options)

        """ Widget Stylings """

        self.txtPassword.config(width="20",show="*")
        self.txtConfirmPassword.config(width="20",show="*")
        self.lblUsername.config(justify="right",fg = "black",background="#8ABFD9",font=("Arial", 10, 'bold'))
        self.lblPassword.config(justify="right",fg = "black",background="#8ABFD9",font=("Arial", 10, 'bold'))
        self.lblConfirmUsername.config(justify="right",fg = "black",background="#8ABFD9",font=("Arial", 10, 'bold'))
        self.lblConfirmPassword.config(justify="right",fg = "black",background="#8ABFD9",font=("Arial", 10, 'bold'))
        self.lblAccessLevel.config(justify="right",fg = "black",background="#8ABFD9",font=("Arial", 10, 'bold'))
        self.lblEmail.config(justify="right",fg = "black",background="#8ABFD9",font=("Arial", 10, 'bold'))
        self.loginButton.config(compound="left",background="#307292",relief="flat",font=("Arial", 12, 'bold'),padx=5)
        self.registerButton.config(compound="left",background="#307292",relief="flat",font=("Arial", 12, 'bold'),padx=5)
        self.Title.config(background="#8ABFD9",fg = "#404040",pady="5")

        """ Widget Positions """

        self.txtUsername.grid(row=1,column = 1)
        self.txtConfirmUsername.grid(row=2,column = 1)
        self.txtPassword.grid(row=3,column = 1)
        self.txtConfirmPassword.grid(row=4,column = 1)
        self.txtEmail.grid(row=5,column = 1)
        self.loginButton.grid(row=7,column = 0)
        self.registerButton.grid(row=7,column = 1)
        self.lblUsername.grid(row=1,column = 0)
        self.lblConfirmUsername.grid(row=2,column = 0)
        self.lblPassword.grid(row=3,column = 0)
        self.lblConfirmPassword.grid(row=4,column = 0)
        self.lblEmail.grid(row=5,column = 0)
        self.Title.grid(row=0,column = 0,columnspan=2)
        self.lblAccessLevel.grid(row=6,column =0 )
        self.cmbAccessLevel.grid(row=6,column = 1)
