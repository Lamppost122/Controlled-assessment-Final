import os
import json
import datetime
import Config


class System_init:
    """
    Method:
        FileCreation
        init__SystemBackUps


     """

    @staticmethod
    def FileCreation():
        """This creates file if they do not already exist """
        files = [Config.TeamFile,Config.UserFile,Config.PlayerFile,Config.MatchFile,Config.PlayerStatsFile,Config.UpdatesFile,Config.SeasonFile,Config.BackupListFile,Config.BackupDateFile,Config.MatchAvailablityFile,Config.MatchReportFile]
        for i in files:
            if not os.path.isfile(i):
                if i == Config.SeasonFile:
                    present =datetime.datetime.now()
                    currentYear =present.year
                    if datetime.datetime(currentYear,9,1) >present:
                        currentYear -=1
                    seasonData = "01/09/"+str(currentYear)
                    f= open(i,"w+")
                    f.write(seasonData)
                    f.close()

                elif i == Config.BackupListFile:

                    System_init.init__SystemBackUps()
                else:
                    with open(i,"w+") as fp:
                        json.dump({},fp)
                    print("New File Create with name : "+ i)

    @staticmethod
    def init__SystemBackUps():
        """
        Initalises the backup file
        """
        data={
        "Child":[Config.UserFile,Config.PlayerFile,Config.MatchFile,Config.TeamFile,Config.PlayerStatsFile,Config.UpdatesFile,Config.SeasonFile],
        "Parent":[],
        "Grandparent":[]
        }
        with open(Config.BackupListFile,"w")as fp:
            json.dump(data,fp)
        print("New File Create with name : "+ Config.BackupListFile)