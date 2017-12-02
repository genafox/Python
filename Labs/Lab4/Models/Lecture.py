from Models.Entity import *

class Lecture(Entity):
    def __init__(self, id, name, courseId, content):
        self.id = id;
        self.name = name;
        self.courseId = courseId;
        self.content = content;

    def toString(self, indentLevel):
        template = super().getTemplate(indentLevel, "id: {0},", "name: {1},", "courseId: {2},", "content: {3}");
        return template.format(self.id,
            self.name,
            self.courseId,
            self.content);
