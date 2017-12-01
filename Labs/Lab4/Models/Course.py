class Course(object):
    def __init__(self, id, name, price, marks=[], lectures=[], sessions=[]):
        self.id = id;
        self.name = name;
        self.price = price;
        self.marks = marks;
        self.lectures = lectures;
        self.sessions = sessions;
