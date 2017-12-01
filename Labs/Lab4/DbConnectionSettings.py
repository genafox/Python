from configparser import ConfigParser

class DbConnectionSettings(object):
    def __init__(self, filename='Config.ini', sectionName='postgresql'):
        # create a parser
        parser = ConfigParser()
        # read config file
        parser.read(filename)
        # get section
        if parser.has_section(sectionName):
            section = parser[sectionName];
            self.host = section['host'];
            self.port = section['port'];
            self.database = section['database'];
            self.user = section['user'];
            self.password = section['password'];
        else:
            raise Exception('Section {0} not found in the {1} file'.format(sectionName, filename));

    def getDict(self):
        return {
               'host': self.host,
               'port': self.port,
               'database': self.database,
               'user': self.user,
               'password': self.password
            };


