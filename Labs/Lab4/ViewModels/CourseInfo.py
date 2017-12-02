from Utils.PrintHelper import *

class CourseInfo(object):
    def __init__(self, id, name, price, avgMark):
        self.id = id;
        self.name = name;
        self.price = price;
        self.avgMark = avgMark;

    def toString(self, indentLevel=0):
        template = getTemplate(indentLevel, "id: {0},", "name: {1},", "price: {2},", "avgMark: {3},");
        return template.format(self.id,
            self.name,
            self.price,
            self.avgMark);
