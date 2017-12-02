class Course(object):
    def __init__(self, id, name, price, marks=[], lectures=[], sessions=[]):
        self.id = id;
        self.name = name;
        self.price = price;
        self.marks = marks;
        self.lectures = lectures;
        self.sessions = sessions;

    def toString(self):
        return """id: {0}, 
                  name: {1}, 
                  price: {2},
                  lectures: [{3}],
                  marks: [{4}],
                  sessions: [{5}]""".format(
                      self.id,
                      self.name,
                      self.price,
                      "\n\t".join(map(lambda l: l.toString(), self.lectures)),
                      "\n\t".join(map(lambda m: m.toString(), self.marks)),
                      "\n\t".join(map(lambda s: s.toString(), self.sessions)));
