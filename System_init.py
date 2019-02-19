import os
import json
import datetime

class System_init:
    @staticmethod
    def FileCreation():
        files = ["data.json","players.json","matches.json","teams.json","playerStats.json","updates.json","season.json","BackUpList.json","BackupDates.json","matchAvailablity.json","season.txt","matchReport.json"]
        for i in files:
            if not os.path.isfile(i):
                if i == "season.txt":
                    present =datetime.datetime.now()
                    currentYear =present.year
                    if datetime.datetime(currentYear,9,1) >present:
                        currentYear -=1
                    seasonData = "01/09/"+str(currentYear)
                    f= open(i,"w+")
                    f.write(seasonData)
                    f.close()




                elif i == "BackUpList.json":

                    System_init.init__SystemBackUps()
                else:
                    with open(i,"w+") as fp:
                        json.dump({},fp)
                    print("New File Create with name : "+ i)

    @staticmethod
    def init__SystemBackUps():
        data={
        "Child":["data.json","players.json","matches.json","teams.json","playerStats.json","updates.json","season.json"],
        "Parent":[],
        "Grandparent":[]
        }
        with open("BackupList.json","w")as fp:
            json.dump(data,fp)
        print("New File Create with name : "+ "BackupList.json")

    def PlayerFile(PlayerFileName = "players.json"):
        with open(PlayerFileName,"w") as fp:
            json.dump({},fp)

    def TeamFile(TeamFileName ="teams.json" ):
        with open(PlayerFileName,"w") as fp:
                json.dump({},fp)
    def MatchFile(MatchFileName = "matches.json",TeamFileName = "teams.json" ):
        for i in teams:
            data[i] = {}
        with open(MatchFileName,"w") as fp:
            json.dump(data,fp)
