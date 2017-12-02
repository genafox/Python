from Models.Entity import *

class Session(Entity):
    def __init__(self, id, startDate, endDate, curseId):
        self.id = id;
        self.startDate = startDate;
        self.endDate = endDate;
        self.curseId = curseId;

    def toString(self):
        return "";


