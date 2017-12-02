class Lecture(object):
    def __init__(self, id, name, courseId, content):
        self.id = id;
        self.name = name;
        self.courseId = courseId;
        self.content = content;

    def toString(self):
        return """id: {0}, 
                  name: {1}, 
                  courseId: {2},
                  content: [{3}]""".format(
                      self.id,
                      self.name,
                      self.courseId,
                      self.content);
