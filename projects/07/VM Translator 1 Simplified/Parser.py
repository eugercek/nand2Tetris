from Constants import Constants
class Parser(Constants):
    def __init__(self):
        pass
    def formatter(self,line):
        if line.strip() == "":#Empty line check
            return self.EMPTY_LINE
        if line[0] == "/":#Comment line check
            return self.COMMENT_LINE
        else:
            if '/' in line:
                end = line.index('/')
                return line[:end].strip()
            else:
                return line.strip()
    def command_type(self,lineFormatted):
        if len(lineFormatted.split(" ")) ==1:
            return self.C_ARITHMETIC
        else:
            if lineFormatted.split(" ")[0] == "push":
                return self.C_PUSH
            else:
                return self.C_POP

    def arg1(self,lineFormatted,type):
        if type == self.C_ARITHMETIC:
            return lineFormatted.split(" ")[0]#i.e add 
        else:
            return lineFormatted.split(" ")[1]#i.e local

    def arg2(self,lineFormatted,type):
        if type == self.C_ARITHMETIC:
            return 0
        else:
            return lineFormatted.split(" ")[2]