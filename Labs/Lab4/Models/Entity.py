from Utils.PrintHelper import *

class Entity(object):
    def getTemplate(self, indentLevel, *templateParts):
        template = getTemplate(indentLevel, *templateParts);
        return template;


