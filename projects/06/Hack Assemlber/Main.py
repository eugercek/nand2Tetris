import os
from Parser import Parser
from Code import Code
from SymbolTable import SymbolTable
#TODO Regex must included import re

#Looking for (foo)
def passZero(readFile,writeFile,symbols):
    i=0
    for line in readFile:
        if not line.strip():
            continue
        if "//" in line:
            if line[0] == "/":
                continue
            commentStart =line.index("//")
        else:
            commentStart = len(line)

        if "(" in line and ")" in line:
            start = line.index("(")
            end = line.index(")")
            label = line[start+1:end]
            if start < commentStart:
                symbols.addLabel(label,i)
                continue
        i +=1


def passOne(readFile,writeFile,symbols):
    readFile.seek(0)
    parser = Parser()
    code = Code()
    for line in readFile:
        if not line.strip():
            continue
        elif line[0:2] == "//":
            continue
        elif line[0] == "(":
            continue
        elif  line[0] == '@':
            writeLine=AIns(line,parser,code,symbols)#TODO Too many object passed by arguments
            writeFile.write(writeLine+"\n")
        else:
            writeLine=CIns(line,parser,code,symbols)
            writeFile.write(writeLine+"\n")


def CIns(line,parser,code,symbols):
    elements = parser.cParser(line)
    wrtieLine = code.getCLineCode(elements)
    return wrtieLine

def AIns(line,parser,code,symbols):
    ains = parser.aParser(line)
    if ains.isdigit():
        writeLine=code.getNumCode(ains)
    else:
        if symbols.contains(ains):
            writeLine=code.getNumCode(symbols.getAddress(ains))
        else:
            writeLine=code.getNumCode(symbols.addVariable(ains))
    return writeLine
    
def main():
    if len(os.sys.argv)  !=  2:
        print("Usage py(thon)[2,3] main.py filename.asm")
        os.sys.exit()
    symbols = SymbolTable()
    assemblyFile=os.sys.argv[1]
    binaryFile="hack.hack"
    readFile = open(assemblyFile,"r")
    writeFile = open(binaryFile,"w")
    passZero(readFile,writeFile,symbols)
    passOne(readFile,writeFile,symbols)

if __name__ == '__main__':
    main()
