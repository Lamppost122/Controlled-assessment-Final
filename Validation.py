import re
from SystemToolKit import *
import Config
class Validation:
    @staticmethod
    def FirstName(FirstName):

        rule = re.compile('[A-Za-z]{2,30}( [A-Za-z]{2,30})?')
        if not rule.search(FirstName):
            return False
        else:
            return True
    @staticmethod
    def LastName(LastName):
        rule = re.compile('[A-Za-z]{2,30}( [A-Za-z]{2,30})?')
        if not rule.search(LastName):
            return False
        else:
            return True
    @staticmethod
    def PhoneNumber(PhoneNumber):
        rule = re.compile(r'^\+?(44)?(0|7)\d{9,13}$')
        if not rule.search(PhoneNumber):
            return False
        else:
            return True
    @staticmethod
    def Address(Address):
        rule = re.compile(r'^\d+\s[A-z]+\s[A-z]')
        if not rule.search(Address):
            return False
        else:
            return True

    @staticmethod
    def DateOfBirth(DateOfBirth):
         try:
            datetime.strptime(dateOfBirth, '%d/%m/%Y')
            if datetime.datetime.now() - timedelta(days=2000) > datetime.strptime(dateOfBirth, '%d/%m/%Y'):
                return True
            else:
                return False
         except ValueError:
            return False
    @staticmethod
    def TeamNumber(TeamNumber):
        Data =SystemToolKit.readFile("team.json")
        for i in Data:
            for j in Data[i]:
                if j == "Team Number":
                    if Data[i][j] == str(TeamNumber):
                        return True
        return False
    @staticmethod
    def Date(Date,TimeState = "None"):
        try:
            if TimeState == "Future":
                if datetime.datetime.now() < datetime.strptime(dateOfBirth, '%d/%m/%Y'):
                    datetime.strptime(dateOfBirth, '%d/%m/%Y')
                    return True
                else:
                    return False
            elif TimeState == "Past":
                if datetime.datetime.now() > datetime.strptime(dateOfBirth, '%d/%m/%Y'):
                    datetime.strptime(dateOfBirth, '%d/%m/%Y')
                    return True
                else:
                    return False
            else:
                datetime.strptime(dateOfBirth, '%d/%m/%Y')

        except ValueError:
            return False
    @staticmethod
    def Time(Time):
        try:
            datetime.strptime(Time, '%h:%M')
            return True
        except ValueError:
            return False
    @staticmethod
    def Opposition(Opposition):
        if re.findall('[^A-Za-z0-9]',Opposition):
            return False
        else:
            return True
    @staticmethod
    def Score(Score):

            Score = int(Score)




Validation.Score("asds")