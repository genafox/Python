from Models.Course import *
from Models.Lecture import *
from Models.Mark import *
from Models.User import *
from Models.Session import *

class DataMapper(object):
    def MapCourse(self, row):
        return Course(row[0], row[1], row[2]);

    def MapLecture(self, row):
        return Lecture();

    def MapMark(self, row):
        return Mark();

    def MapUser(self, row):
        return User();

    def MapSession(self, row):
        return Session();


