def getIndent(indentLevel):
        indent = "";
        while indentLevel > 0:
            indent += "\t";
            indentLevel -= 1;
        return indent;

def getTemplate(indentLevel, *templateParts):
    indent = getIndent(indentLevel)
    template = ("\n" + indent).join(templateParts);
    return template;


