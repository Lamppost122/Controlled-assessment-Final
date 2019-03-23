import os
import json
import datetime
import Config


class System_init:

    @staticmethod
    def FileCreation():
        files = [Config.TeamFile,Config.UserFile,Config.PlayerFile,Config.MatchFile,Config.PlayerStatsFile,Config.UpdatesFile,Config.SeasonFile,Config.BackupListFile,Config.BackupDateFile,Config.MatchAvailablityFile,Config.MatchReportFile]
        for i in files:
            if not os.path.isfile(i):
                if i == Config.Season:
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
        data={
        "Child":[Config.UserFile,Config.PlayerFile,Config.MatchFile,Config.TeamFile,Config.PlayerStatsFile,Config.UpdatesFile,Config.SeasonFile],
        "Parent":[],
        "Grandparent":[]
        }
        with open(Config.BackupListFile,"w")as fp:
            json.dump(data,fp)
        print("New File Create with name : "+ Config.BackupListFile)


