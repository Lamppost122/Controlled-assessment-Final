import sys
import os
import json
import Config

class SystemToolKit:

    @staticmethod
    def readFile(FileName):
        """
        Takes a json File and returns its data
        If no file exisits one will be created and populated with a blank dictionary

        """
        Data = ""
        try:
            with open(FileName, 'r') as fp:
                    Data = json.load(fp)
                    return Data

        except ValueError or IOError:
            data = {}
            with open(FileName,"w+") as fp:
                json.dump(data,fp)
            return Data

    @staticmethod
    def getTeamId(TeamNumber):
        """
        Takes a Team Number and returns a Team ID(String)
        If a Team of Number parsed does not exisit will return None

        """

        Teams = SystemToolKit.readFile(Config.TeamFile)
        for i in Teams:
            if Teams[i]["Team Number"] == TeamNumber:
                return i

    def BackButtonRun(controller):
        """
        Triggers a change of frame to the previous frame but at the current access level

        Returns a page name(String)
        """
        Config.PagesViewed.pop()
        controller.show_previous_frame(Config.PagesViewed[-1])
        return Config.PagesViewed[-1]


