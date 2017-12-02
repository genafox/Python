from Models.Entity import *

class Course(Entity):
    def __init__(self, id, name, price, marks=[], lectures=[], sessions=[]):
        self.id = id;
        self.name = name;
        self.price = price;
        self.marks = marks;
        self.lectures = lectures;
        self.sessions = sessions;

    def toString(self, indentLevel=0):
        template = super().getTemplate(indentLevel, "id: {0},", "name: {1},", "price: {2},", "lectures: [{3}],", "marks: [{4}],", "sessions: [{5}]\n");
        return template.format(self.id,
            self.name,
            self.price,
            "\n".join(map(lambda l: l.toString(1), self.lectures)),
            "\n".join(map(lambda m: m.toString(1), self.marks)),
            "\n".join(map(lambda s: s.toString(1), self.sessions)));
