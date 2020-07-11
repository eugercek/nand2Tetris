import sys
import glob
from Parser import Parser
from CodeWriter import CodeWriter
from Constants import Constants

if __name__ == '__main__':
    parser = Parser()
    if '.' in sys.argv[1]:# .vm file input
        out_file_name =sys.argv[1].split('.')[0]+ '.asm'
        code_writer = CodeWriter(out_file_name)
        with open(sys.argv[1], 'r') as read_file:
            for line in read_file: #Marching through file
                debug_line = line #For debug purposes
                # debug_line = Constants.NO_DEBUG
                #print(line)
                formattedLine = parser.formatter(line)
                if formattedLine == Constants.NOT_COMMAND:
                    continue
                else:
                    command_type = parser.command_type(formattedLine)
                    arg1 = parser.arg1(formattedLine,command_type)
                    arg2 = parser.arg2(formattedLine,command_type)
                    code_writer.write_command(command_type,arg1,arg2,debug_line=debug_line)

    else:# It is a directory
        for in_file in glob.glob("*.vm"):
            out_file_name = in_file + '.asm'
            code_writer = CodeWriter(out_file_name)
            with open(in_file , 'r') as read_file: #Marching through file
                for line in read_file:
                    debug_line = line# If don't want debug line write '' instead of line
                    formattedLine = parser.formatter(line)
                    if formattedLine == Constants.NOT_COMMAND:
                            continue
                    else:
                        command_type = parser.command_type(formattedLine)
                        arg1 = parser.arg1(formattedLine,command_type)
                        arg2 = parser.arg2(formattedLine,command_type)
                        code_writer.write_command(command_type,arg1,arg2,debug_line=debug_line)
