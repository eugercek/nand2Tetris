import string
import os
import Constants

class JackTokenizer:
    def __init__(self, file_name):
        self.file = open(file_name + '.jack', 'r')
        self.current_token = ''
        self.current_tokens = list()
        self.next_token = ''
    
    def comment_free(self):
        lines = self.file.read().splitlines()
        new_lines = list()
        for line in lines:
            if line == '':
                continue
            if line[0] == '/': #Handles // /* /**
                continue
            elif line[0] == '*': #Handels Multiline comments
                continue
            else:
                new_lines.append(line)
        self.lines = new_lines
    
    def tokenize(self):
        for line in self.lines:
            elements = line.split(' ')
            for element in elements:
                if [i for i in Constants.SYMBOLS if i in element] and len(element) != 1:
                    element.index()





    def advance(self):
        if self.current_tokens == []:
            self.current_tokens = self.file.readline().strip().split(' ')


        if [i for i in Constants.SYMBOLS if i in x] and len(x) != 1:
            for a in Constants.SYMBOLS:
                if a in x:
                    x = x.replace(a, '')
                    break
            self.current_tokens.insert(1,a)
    
        print(x)




        



    def tokentype(self):

        print(self.current_token, end='\t')
        if self.current_token in Constants.KEYWORDS:
            print('keyword')
            return Constants.KEYWORD
        elif self.current_token in Constants.SYMBOLS:
            print('symbol')
            return Constants.SYMBOL
        elif isinstance(self.current_token, int):
            print('integer')
            return Constants.INT_CONST
        else:
            print('string')
            return Constants.STRING_CONST

    def keyword(self):
        pass

    def symbol(self):
        pass

    def identifier(self):
        pass

    def intVal(self):
        pass

    def stringVal(self):
        pass


    # def advance(self):
    #     if self.next_token != '':
    #         self.current_token = self.next_token
    #         self.next_token = ''
    #         self.tokentype()
    #         return 

    #     list_buffer = list()
    #     while true:
    #         character_buffer = self.file.read(1)
    #         if character_buffer.isspace():
    #             if self.current_token == '':
    #                 continue
    #             else:
    #                 self.current_token = ''.join(list_buffer)
    #                 break
    #         elif character_buffer in Constants.symbols:
    #             self.current_token = ''.join(list_buffer)
    #             self.next_token = character_buffer
    #             break
    #         else:
    #             list_buffer.append(character_buffer)

    #     self.tokentype()
    #     return


j = JackTokenizer('Square')
j.comment_free()