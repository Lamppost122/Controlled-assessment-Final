import re
from SystemToolKit import *
from tkinter import messagebox
import Config
import datetime
class Validation:
    """
    Methods:
        Firstname
        Lastname
        Postcode
        PhoneNumber
        Address
        DateOfBirth
        TeamNumber
        Date
        Time
        Oppositon
        Score
        PresentsCheck
        Username
        Passwords
        NewTeam

    """

    @staticmethod
    def FirstName(FirstName):
        """Validate the first name"""
        if len(FirstName) < 30:
            if FirstName != "":

                rule = re.compile("^[\w'\-,.][^0-9_!?????/\\+=@#$%?&*(){}|~<>;:[\]]{2,}$")
                if not rule.search(FirstName):
                    messagebox.showinfo("Invalid Data","The First Name you have added does not match the necessary criteria")

                    return False
                else:
                    return True
            else:
                messagebox.showinfo("Invalid Data","First name is empty")
                return False
        else:
            messagebox.showinfo("Invalid Data","The First Name you have added does not match the necessary criteria")
            return False

    @staticmethod
    def LastName(LastName):
        """Validates the Last Name """
        if len(LastName) < 30 :
            if LastName != "":

                    rule = re.compile("^[\w'\-,.][^0-9_!?????/\\+=@#$%?&*(){}|~<>;:[\]]{2,}$")
                    if not rule.search(LastName):
                        messagebox.showinfo("Invalid Data","The Last Name you have added does not match the necessary criteria")
                        return False
                    else:
                        return True
            else:
                 messagebox.showinfo("Invalid Data","Last name is empty")
                 return False
        else:
            messagebox.showinfo("Invalid Data","The Last Name you have added does not match the necessary criteria")
            return False

    @staticmethod
    def PhoneNumber(PhoneNumber):
        """Validate the Phone Numbers"""
        if PhoneNumber =="":
            messagebox.showinfo("Invalid Data","Phone Number is empty")
            return False
        else:
            rule = re.compile(r'^\+?(44)?(0|7)\d{9,13}$')
            if not rule.search(PhoneNumber):
                messagebox.showinfo("Invalid Data","The Phone Number you have added does not match the necessary criteria")
                return False
            else:
                return True

    @staticmethod
    def Address(Address):
        """Validates the Address"""
        if Address =="":
            messagebox.showinfo("Invalid Data","Address is empty")
            return False
        else:
            rule = re.compile("[A-Za-z0-9'\.\-\s\,]")
            if not rule.search(Address):
                messagebox.showinfo("Invalid Data","The Address you have added does not match the necessary criteria")
                return False
            else:
                return True

    @staticmethod
    def Postcode(Postcode):
        """Validate the Postcode  """
        if Postcode =="":
            messagebox.showinfo("Invalid Data","Postcode is empty")
            return False
        else:
            rule = re.compile("^(([gG][iI][rR] {0,}0[aA]{2})|((([a-pr-uwyzA-PR-UWYZ][a-hk-yA-HK-Y]?[0-9][0-9]?)|(([a-pr-uwyzA-PR-UWYZ][0-9][a-hjkstuwA-HJKSTUW])|([a-pr-uwyzA-PR-UWYZ][a-hk-yA-HK-Y][0-9][abehmnprv-yABEHMNPRV-Y]))) {0,}[0-9][abd-hjlnp-uw-zABD-HJLNP-UW-Z]{2}))$")
            if not rule.search(Postcode):
                messagebox.showinfo("Invalid Data","The Postcode you have added does not match the necessary criteria")
                return False
            else:
                return True

    @staticmethod
    def DateOfBirth(dateOfBirth):
        """Validates the date of birth"""
        if dateOfBirth =="":
            messagebox.showinfo("Invalid Data","Date of Birth is empty")
            return False
        else:
             try:
                datetime.datetime.strptime(dateOfBirth, '%d/%m/%Y')
                if datetime.datetime.now() - datetime.timedelta(days=2000) > datetime.datetime.strptime(dateOfBirth, '%d/%m/%Y'):
                    return True
                else:
                    messagebox.showinfo("Invalid Data","The Date of Birth you have added is too young")
                    return False
             except ValueError:
                messagebox.showinfo("Invalid Data","The Data of birth you have added does not meet the necessary format(DD/MM/YYYY)")
                return False

    @staticmethod
    def TeamNumber(TeamNumber):
        """Validates the Team Number"""
        if TeamNumber =="":
            messagebox.showinfo("Invalid Data","Team Number is empty")
            return False
        else:
            Data =SystemToolKit.readFile(Config.TeamFile)
            for i in Data:
                for j in Data[i]:
                    if j == "Team Number":
                        if Data[i][j] == str(TeamNumber):
                            return True
            messagebox.showinfo("Invalid Data","That team does not exist")
            return False

    @staticmethod
    def Date(Date,TimeState = "None"):
        """Validates the Date"""
        if Date =="":
            messagebox.showinfo("Invalid Data","Date is empty")
            return False
        else:
            try:
                if TimeState == "Future":
                    if datetime.datetime.now() < datetime.datetime.strptime(Date, '%d/%m/%Y'):
                        datetime.datetime.strptime(Date, '%d/%m/%Y')
                        return True
                    else:
                        messagebox.showinfo("Invalid Data","The date you have added is in the past")
                        return False
                elif TimeState == "Past":
                    if datetime.datetime.now() > datetime.datetime.strptime(Date, '%d/%m/%Y'):
                        datetime.datetime.strptime(Date, '%d/%m/%Y')
                        return True
                    else:
                        messagebox.showinfo("Invalid Data","The date you have added is in the future")
                        return False
                else:
                    datetime.datetime.strptime(Date, '%d/%m/%Y')
                    return True

            except ValueError:
                messagebox.showinfo("Invalid Data","The Date you have added does not meet the necessary format(DD/MM/YYYY)")
                return False

    @staticmethod
    def Time(Time):
        """Validates the Time"""
        if Time =="":
            messagebox.showinfo("Invalid Data","Time is empty")
            return False
        else:
            try:
                datetime.datetime.strptime(Time, '%H:%M')
                return True
            except ValueError:
                messagebox.showinfo("Invalid Data","The Time you have added does not meet the necessary format(HH:MM)")
                return False

    @staticmethod
    def Opposition(Opposition):
        """Validates the opposition"""
        if Opposition =="":
            messagebox.showinfo("Invalid Data","Opposition is empty")
            return False
        else:
            if re.findall('[^A-Za-z0-9]+$',Opposition):
                messagebox.showinfo("Invalid Data","The Team you have added does not match the necessary criteria")
                return False
            else:
                return True

    @staticmethod
    def Score(Score):
        """Validates the score"""
        if Score =="":
            messagebox.showinfo("Invalid Data","Score is empty")
            return False
        else:
            try:
                Score = int(Score)
                if Score >99:
                    messagebox.showinfo("Invalid Data","The Score you have add is greater than 99")
                    return False
                else:
                    return True
            except ValueError:
                messagebox.showinfo("Invalid Data","The data you have added is not a number")
                return False

    @staticmethod
    def PresentsCheck(Data):
        """Checks if the data is blank"""
        if Data == "":
            messagebox.showinfo("Missing Data","Field Cannot be left blank")
            return False
        else:
            return True

    @staticmethod
    def Username(Username):
        """Validates the Username"""
        Data= SystemToolKit.readFile(Config.UserFile)
        if Username != "":

                rule = re.compile("^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)[a-zA-Z\d]{8,30}$")
                if  rule.search(Username):

                    for i in Data:
                        if Data[i]["Username"] == Username:
                            messagebox.showinfo("Invalid Data","Username is already in use")
                            return False
                    return True
                else:
                    messagebox.showinfo("Invalid Data","Username should:\n Contain at least 1 number \n Contain Both upper and lower case letters \n be between 6 and 30 characters")
                    return False


        else:
            messagebox.showinfo("Invalid Data","Username is should not be left blank")
            return False

    @staticmethod
    def Password(Password):
        """Validates the passwords"""

        if re.match("^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)[a-zA-Z\d]{8,}$", Password):
            return True
        else:
            messagebox.showinfo("Invalid Data","Password does not meet criteria \n Must Contain:\n upper and lower case characters \n at least 1 number \n Be 8 characters or more")
            return False

    @staticmethod
    def Email(Email):
        """Validates the email """
        Data= SystemToolKit.readFile(Config.UserFile)
        for i in Data:
            if Data[i]["Email"] == Email:
                messagebox.showinfo("Invalid Data","Email is already in use")
                return False
        return True

    @staticmethod
    def newTeam(TeamNumber):
        """Validates a teamNumber"""
        if TeamNumber !="":
            try:
                TeamNumber = int(TeamNumber)
                if TeamNumber <99:
                    return True
                else:
                    messagebox.showinfo("Invalid Data","Team number is too large(>99)")
                    return False
            except ValueError:
                messagebox.showinfo("Invalid Data","Team number entered is not a number")
                return False
        else:
            messagebox.showinfo("Invalid Data","Team number cannot be left blank")
            return False
