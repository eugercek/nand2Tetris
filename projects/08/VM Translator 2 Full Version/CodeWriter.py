import random
import string
from Constants import Constants

class CodeWriter():
    '''
    Translates VM code input to asm code and writes on file
    Constructor file name argument mandatory
    '''
    def __init__(self,file_name):
        self.file=open(file_name,'w')
        self.debug_line_number = 0
        self.fname = file_name.split('.')[0]

    def debug_comments(self,line):
        self.file.write('//'+str( self.debug_line_number )+'\n')
        self.file.write('//'+line)
        self.debug_line_number += 1
    def __d_eq_ptr(self):
        self.file.write('A=M\n')
        self.file.write('D=M\n')

    def __sp_inc(self):
        self.file.write('@SP\n')
        self.file.write('M=M+1\n')

    def __sp_dec(self):
        self.file.write('@SP\n')
        self.file.write('M=M-1\n')

    def write_command(self,command_type,arg1,arg2,debug_line='null'):
        if debug_line != Constants.NO_DEBUG:
            self.debug_comments(debug_line)
        if command_type == Constants.C_ARITHMETIC:
            self.write_arithmetic(arg1)
        else:
            self.write_push_pop(command_type,arg1,int(arg2))#i.e push local 20

    def random_label(self):
        return ''.join(random.choice(string.ascii_uppercase) for x in range(8))
    def compareTemplate(self,operation):#!eq gt lt
        true_label = self.random_label()
        end_if_label = self.random_label()

        self.__sp_dec()
        self.__d_eq_ptr()
        self.__sp_dec()
        self.file.write('A=M\n')
        self.file.write('D=M-D\n')
        self.file.write('@' + true_label + '\n')
        self.file.write(f'D;{Constants.JUMPS[operation]}\n')
        self.file.write('@SP\n')
        self.file.write('A=M\n')
        self.file.write('M=0\n')
        self.file.write(f'@{end_if_label}\n')
        self.file.write('0;JMP\n')
        self.file.write(f'({true_label})\n')
        self.file.write('@SP\n')
        self.file.write('A=M\n')
        self.file.write('M=-1\n')
        self.file.write(f'({end_if_label})\n')
        self.__sp_inc()


    def write_arithmetic(self,operation):
        #Arithmetic
        if operation == 'add':
            self.__sp_dec()
            self.__d_eq_ptr()
            self.__sp_dec()
            self.file.write('A=M\n',)
            self.file.write('M=D+M\n')
            self.__sp_inc()
        elif operation == 'sub':
            self.__sp_dec()
            self.__d_eq_ptr()
            self.__sp_dec()
            self.file.write('A=M\n')
            self.file.write('M=M-D\n')
            self.__sp_inc()
        elif operation == 'neg':
            self.__sp_dec()
            self.file.write('A=M\n')
            self.file.write('M=-M\n')
            self.__sp_inc()
        #Compare
        elif operation in ['eq','gt','lt']:
            self.compareTemplate(operation)
        #Pure Logic
        elif operation == 'and':
            self.__sp_dec()
            self.__d_eq_ptr()
            self.__sp_dec()
            self.file.write('A=M\n')
            self.file.write('M=D&M\n')
            self.__sp_inc()
        elif operation == 'or':
            self.__sp_dec()
            self.__d_eq_ptr()
            self.__sp_dec()
            self.file.write('A=M\n')
            self.file.write('M=D|M\n')
            self.__sp_inc()
        elif operation == 'not':
            self.__sp_dec()
            self.file.write('A=M\n')
            self.file.write('M=!M\n')
            self.__sp_inc()

    def write_push_pop(self,command,segment,index):#i.e push local 20
        if command == Constants.C_PUSH:
            if segment == 'constant':
                self.file.write(f'@{index}\n')
                self.file.write('D=A\n')
                self.file.write('@SP\n')
                self.file.write('A=M\n')
                self.file.write('M=D\n')
                self.__sp_inc()
            elif segment == 'pointer':
                self.file.write(f'@{Constants.SEGMENTS[segment][index]}\n')
                self.file.write('D=M\n')
                self.file.write('@SP\n')
                self.file.write('A=M\n')
                self.file.write('M=D\n')
                self.__sp_inc()
            elif segment == 'temp':
                self.file.write(f'@{index+5}\n')
                self.file.write('D=M\n')
                self.file.write('@SP\n')
                self.file.write('A=M\n')
                self.file.write('M=D\n')
                self.__sp_inc()
            elif segment == 'static':
                self.file.write(f'@{self.fname}.{index}\n')
                self.file.write('D=M\n')
                self.file.write('@SP\n')
                self.file.write('A=M\n')
                self.file.write('M=D\n')
                self.__sp_inc()
            else:
                self.file.write(f'@{index}\n')#@i
                self.file.write('D=A\n')#offset on D
                self.file.write(f'@{Constants.SEGMENTS[segment]}\n')#i.e @LCL
                self.file.write('D=D+M\n')#!Problem 15/134
                self.file.write('A=D\n')
                self.file.write('D=M\n')
                self.file.write('@SP\n')
                self.file.write('A=M\n')
                self.file.write('M=D\n')
                self.__sp_inc()

        elif command == Constants.C_POP:
            if segment == 'pointer':
                self.file.write('@SP\n')
                self.file.write('AM=M-1\n')
                self.file.write('D=M\n')
                self.file.write(f'@{Constants.SEGMENTS[segment][index]}\n')
                self.file.write('M=D\n')
            elif segment == 'temp':
                self.file.write(f'@{index+5}\n')#i.e @11
                self.file.write('D=A\n')#D=A
                self.file.write('@R13\n')#Use @R* when assigning address
                self.file.write('M=D\n')#M=addr+i
                self.file.write('@SP\n')
                self.file.write('AM=M-1\n')
                self.file.write('D=M\n')
                self.file.write('@13\n')
                self.file.write('A=M\n')
                self.file.write('M=D\n')
            elif segment == 'static':
                self.file.write('@SP\n')
                self.file.write('AM=M-1\n')
                self.file.write('D=M\n')
                self.file.write(f'@{self.fname}.{index}\n')
                self.file.write('M=D\n')
            else:
                self.file.write(f'@{index}\n')#@i
                self.file.write('D=A\n')#offset on D
                self.file.write(f'@{Constants.SEGMENTS[segment]}\n')#i.e @LCL
                self.file.write('D=D+M\n')
                self.file.write('@R13\n')#Use @R* when assigning value
                self.file.write('M=D\n')#M=addr+i
                self.file.write('@SP\n')
                self.file.write('AM=M-1\n')
                self.file.write('D=M\n')
                self.file.write('@13\n')
                self.file.write('A=M\n')
                self.file.write('M=D\n')


    def segmentFinder(self,segment,index):
        if segment == 'temp':
            return index +5
        elif segment in ['local','argument','tihs','that' ]:
            return Constants.SEGMENTS[segment]
        elif segment == 'static':
            return f'@{self.fname}.{index}\n'
        elif segment == 'pointer':
            pass#TODO pointer ekle


