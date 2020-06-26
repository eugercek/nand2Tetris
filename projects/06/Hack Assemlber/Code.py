class Code:
    def __init__(self):
        pass
    jumpCodes = {
        "":"000",
        "null":"000",
        "JGT":"001",
        "JEQ":"010",
        "JGE":"011",
        "JLT":"100",
        "JNE":"101",
        "JLE":"110",
        "JMP":"111",
    }

    compCodes = {
        "null":"ERROR!",
        '0':   '0101010',
        '1':   '0111111',
        '-1':  '0111010',
        'D':   '0001100',
        'A':   '0110000',
        '!D':  '0001101',
        '!A':  '0110001',
        '-D':  '0001111',
        '-A':  '0110011',
        'D+1': '0011111',
        'A+1': '0110111',
        'D-1': '0001110',
        'A-1': '0110010',
        'D+A': '0000010',
        'D-A': '0010011',
        'A-D': '0000111',
        'D&A': '0000000',
        'D|A': '0010101',
        'M':   '1110000',
        '!M':  '1110001',
        '-M':  '1110011',
        'M+1': '1110111',
        'M-1': '1110010',
        'D+M': '1000010',
        'D-M': '1010011',
        'M-D': '1000111',
        'D&M': '1000000',
        'D|M': '1010101',
    }

    def getJumpCode(self,jumpPart):
        return self.jumpCodes[jumpPart]
    
    def getCompCode(self,compPart):
        return self.compCodes[compPart]
    def getDestCode(self,destPart):
        registers = ["A","D","M"]
        code = ""
        for register in registers:
            if register in destPart:
                code += "1"
            else:
                code += "0"
        return code
    def getNumCode(self,num):
        return bin(int(num))[2:].zfill(16)
    def getCLineCode(self,elements):
        destCode = self.getDestCode(elements[0])
        compCode = self.getCompCode(elements[1])
        jumpCode = self.getJumpCode(elements[2])
        return "111"+compCode+destCode+jumpCode
        