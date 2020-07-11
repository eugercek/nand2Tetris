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
        self.file_name = file_name.split('.')[0]
        self.debug_line_number = 0
        self.fname = file_name.split('.')[0]
        self.rand_labels = list()
        self.is_function = False
    def write_init(self):#TODO wtf??
        self.file.write('@256')
        self.file.write('D=A')
        self.file.write('@SP')
        self.file.write('M=D')
        self.file.write('call')
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
        elif  command_type == Constants.C_PUSH:
            self.write_push(arg1,int(arg2))
        elif command_type == Constants.C_POP:
            self.write_pop(arg1,int(arg2))
        elif command_type == Constants.C_LABEL:
            self.write_label(arg1)
        elif command_type == Constants.C_GOTO:
            self.write_label(arg1)
        elif command_type == Constants.C_IF:
            self.write_if(arg1)
        elif command_type == Constants.C_RETURN:
            self.write_return(arg1)
        elif command_type == Constants.C_CALL:
            self.write_call(arg1)
        elif command_type == Constants.C_FUNCTION:
            self.write_function(arg1)

    def random_label(self):
        temp = ''.join(random.choice(string.ascii_uppercase) for x in range(8))

        while True:
            if not ( temp in self.rand_labels ):
                break
            temp = ''.join(random.choice(string.ascii_uppercase) for x in range(8))

        return temp

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

    def write_push(self,segment,index):
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

    def write_pop(self,segment,index):
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
            self.file.write('M=D\n')#13's value =addr+i
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


    def write_label(self, label):
        """(MyClass.(FunctionName)$label)"""
        if self.is_function:
            self.file.write(f'({self.file_name}.{self.function_name}${label})\n')
        else:
            self.file.write(f'({self.file_name}.{label})\n')

    def write_goto(self, label):
        self.file.write(f'@{self.file_name}.{label}\n')
        self.file.write('0;JMP\n')

    def write_if(self, label):
        self.file.write(f'@{label}\n')
        self.file.write('D;JNE\n')

    def write_call(self,function_name,n_args):
        return_label = f'(RET_{function_name})'

        self.write_push('constant', return_label)
        self.write_push('constant', 'LCL')
        self.write_push('constant', 'ARG')
        self.write_push('constant', 'THIS')
        self.write_push('constant', 'THAT')

        #ARG = SP -5 -nArgs
        self.file.write('@SP')
        self.file.write('D=M')
        self.file.write('@5')
        self.file.write('D=D-A')
        self.file.write(f'@{n_args}')
        self.file.write('D=D-A')
        self.file.write('@ARG')
        self.file.write('D=M-D')

        #LCL = SP
        self.file.write('@SP')
        self.file.write('D=M')
        self.file.write('@LCL')
        self.file.write('M=D')

        #goto Function_name
        self.write_goto(function_name)

        self.write_label(return_label)

    def write_return(self):
        frame = self.random_label()
        ret = self.random_label()

        #frame = LCL
        self.file.write('@LCL')
        self.file.write('D=M')
        self.file.write(f'@{frame}')
        self.file.write('M=D')

        #retAddr = *(frame - 5)
        self.file.write(f'@{frame}')
        self.file.write('D=A')
        self.file.write('@5')
        self.file.write('D=D-A')
        self.file.write(f'@{ret}')
        self.file.write('M=D')

        #*ARG = pop() TODO
        self.write_pop()
        self.write_push('argument', 0)

        #SP = ARG +1
        self.file.write('@ARG')
        self.file.write('D=A+1')
        self.file.write('@SP')
        self.file.write('M=D')

        #THAT = *(frame -1)
        self.file.write(f'@{frame}')
        self.file.write('D=A')
        self.file.write('@1')
        self.file.write('D=D-A')
        self.file.write('@THAT')
        self.file.write('M=D')

        #THIS = *(frame -2)
        self.file.write(f'@{frame}')
        self.file.write('D=A')
        self.file.write('@1')
        self.file.write('D=D-A')
        self.file.write('@THIS')
        self.file.write('M=D')

        #ARG = *(frame -3)
        self.file.write(f'@{frame}')
        self.file.write('D=A')
        self.file.write('@1')
        self.file.write('D=D-A')
        self.file.write('@ARG')
        self.file.write('M=D')

        #LCL = *(frame -4)
        self.file.write(f'@{frame}')
        self.file.write('D=A')
        self.file.write('@1')
        self.file.write('D=D-A')
        self.file.write('@LCL')
        self.file.write('M=D')
        self.write_goto(ret)

        self.is_function = False

    def write_function(self,function_name,n_lcls):
        """(MyClass.foo)"""
        # TODO Should write on Assembly ?
        self.is_function = True
        self.function_name = function_name
        self.file.write(f'({self.file_name}.{function_name})\n')
        for i in range(int(n_lcls)):
            self.write_push('constant',0)

