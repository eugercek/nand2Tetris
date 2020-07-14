import string
import os
import Constants

class JackTokenizer:
    def __init__(self, file_name):
        self.file = open(file_name + '.jack', 'r')
        self.file.seek(0, os.SEEK_END)
        self.file_end = self.file.tell()
        self.file.seek(0, os.SEEK_SET)
        self.current_token = ''
        self.next_token = ''


    def hasMoreTokens(self):
        while True:
            if self.file.tell() == self.file_end:
                break
            else:
                self.advance()
        return



    def advance(self):
        if self.next_token != '':
            self.current_token = self.next_token
            self.next_token = ''
            self.tokenType()
            return 

        list_buffer = list()
        while True:
            character_buffer = self.file.read(1)
            if character_buffer.isspace():
                if self.current_token == '':
                    continue
                else:
                    self.current_token = ''.join(list_buffer)
                    break
            elif character_buffer in Constants.SYMBOLS:
                self.current_token = ''.join(list_buffer)
                self.next_token = character_buffer
                break
            else:
                list_buffer.append(character_buffer)

        self.tokenType()
        return



    def tokenType(self):

        print(self.current_token, end='\t')
        if self.current_token in Constants.KEYWORDS:
            print('Keyword')
            return Constants.KEYWORD
        elif self.current_token in Constants.SYMBOLS:
            print('Symbol')
            return Constants.SYMBOL
        elif isinstance(self.current_token, int):
            print('Integer')
            return Constants.INT_CONST
        else:
            print('String')
            return Constants.STRING_CONST

    def keyWord(self):
        pass

    def symbol(self):
        pass

    def identifier(self):
        pass

    def intVal(self):
        pass

    def stringVal(self):
        pass


#test
tokenizer = JackTokenizer('foo')
tokenizer.hasMoreTokens()
