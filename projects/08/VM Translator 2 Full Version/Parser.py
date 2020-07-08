from Constants import Constants

class Parser():
    """Void Constructor
    """
    def __init__(self):
        pass
    def formatter(self,line):
        """Strips comments, deletes new line
        return value stripped line or
        0 for comment lines"""
        if line.strip() == "":#Empty line check
            return Constants.EMPTY_LINE
        elif line[0] == "/":#Comment line check
            return Constants.COMMENT_LINE
        else:
            if '/' in line:
                end = line.index('/')
                return line[:end].strip()
            else:
                return line.strip()
    def command_type(self,lineFormatted):
        """Returns Arithmetic or Push or Pop info"""
        if len(lineFormatted.split(" ")) ==1:
            return Constants.C_ARITHMETIC
        else:
            if lineFormatted.split(" ")[0] == "push":
                return Constants.C_PUSH
            else:
                return Constants.C_POP

    def arg1(self,lineFormatted,com_type):
        """Arithmetic operator (i.e add) or 
        Memory segment (i.e local)"""
        if com_type == Constants.C_ARITHMETIC:
            return lineFormatted.split(" ")[0]#i.e add 
        else:
            return lineFormatted.split(" ")[1]#i.e local

    def arg2(self,lineFormatted,com_type):
        """Arithmetic -> 0
        Push/Pop i
        """
        if com_type == Constants.C_ARITHMETIC:
            return 0
        else:
            return lineFormatted.split(" ")[2]
