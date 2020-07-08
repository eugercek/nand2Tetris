from Parser import Parser
from CodeWriter import CodeWriter
from Constants import Constants

class VMTranslator(Constants):
    def __init__(self,name,debug_option):
        self.debug_option = debug_option
        self.parser = Parser()
        self.codewriter = CodeWriter(name+".asm")
        self.readFile = open(name+".vm","r")

    def translate(self):
        for line in self.readFile:
            debug_line = "null" if self.debug_option else line
            formattedLine = self.parser.formatter(line)
            if formattedLine == self.NOT_COMMAND:
                continue
            command_type = self.parser.command_type(formattedLine)#return is integer 
            arg1 = self.parser.arg1(formattedLine,command_type)
            arg2 = self.parser.arg2(formattedLine,command_type)
            self.codewriter.write_command(command_type,arg1,arg2,debug_line=debug_line)
