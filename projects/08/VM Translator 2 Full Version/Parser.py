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
        """Returns Arithmetic  Push  Pop
        Goto Label Return Call Function info
        """
        if (lineFormatted.split(" ")) ==1:
            if lineFormatted.split(' ')[0] == 'return':
                return Constants.C_RETURN
            else:
                return Constants.C_ARITHMETIC
        else:
            if lineFormatted.split(" ")[0] == "push":
                return Constants.C_PUSH
            elif lineFormatted.split(' ')[0] == 'pop':
                return Constants.C_POP
            elif lineFormatted.split(' ')[0] == 'label':
                return Constants.C_LABEL
            elif lineFormatted.split(' ')[0] == 'goto':
                return Constants.C_GOTO
            elif lineFormatted.split(' ')[0] == 'if-goto':
                return Constants.C_IF
            elif lineFormatted.split(' ')[0] == 'function':
                return Constants.C_FUNCTION
            elif lineFormatted.split(' ')[0] == 'call':
                return Constants.C_CALL

    def arg1(self,lineFormatted,com_type):
        """Arithmetic operator,Memory segment
        LABEL_NAME,Function_name
        """
        if com_type == Constants.C_ARITHMETIC:
            return lineFormatted.split(" ")[0]#i.e add
        elif com_type == Constants.C_POP or com_type == Constants.C_PUSH:
            return lineFormatted.split(" ")[1]#i.e local
        elif com_type == Constants.C_LABEL:
            return lineFormatted.split(" ")[1]#i.e LABEL_NAME
        elif com_type == Constants.C_GOTO:
            return lineFormatted.split(" ")[1]#i.e LABEL_NAME
        elif com_type == Constants.C_IF:
            return lineFormatted.split(" ")[1]#i.e LABEL_NAME
        elif com_type == Constants.C_RETURN:
            return 0
        elif com_type == Constants.C_CALL:
            return lineFormatted.split(" ")[1]#i.e function_name
        elif com_type == Constants.C_FUNCTION:
            return lineFormatted.split(" ")[1]#i.e function_name

    def arg2(self,lineFormatted,com_type):
        """Arithmetic -> 0
        Push/Pop i
        Call nArgs
        Function nLocals
        """
        if com_type == Constants.C_ARITHMETIC:
            return 0
        elif com_type == Constants.C_POP or com_type == Constants.C_PUSH:
            return lineFormatted.split(" ")[2]
        elif com_type == Constants.C_LABEL:
            return 0
        elif com_type == Constants.C_GOTO:
            return 0
        elif com_type == Constants.C_IF:
            return 0
        elif com_type == Constants.C_RETURN:
            return 0
        elif com_type == Constants.C_CALL:
            return int( lineFormatted.split(" ")[2] ) #nArgs
        elif com_type == Constants.C_FUNCTION:
            return int( lineFormatted.split(" ")[2] ) #nLocals
