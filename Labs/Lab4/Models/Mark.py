from Models.Entity import *

class Mark(Entity):
    def __init__(self, courseId, userId, mark, comment):
        self.courseId = courseId;
        self.userId = userId;
        self.mark = mark;
        self.comment = comment;

    def toString(self):
        return "";


