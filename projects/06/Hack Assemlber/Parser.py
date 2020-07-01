class Parser:
    def __init__(self):
        pass
    def aParser(self,line):
        if "//" in line:
            formattedLine = line.split("//")[0].replace(" ","")#foo//bar ====> foo
        else:
            formattedLine = line.replace(" ","")
        return formattedLine.strip()[1:]#omitted @
        

    def cParser(self,line):
        if "//" in line:
            formattedLine = line.split("//")[0].replace(" ","").strip()
        else:
            formattedLine = line.replace(" ","").strip()
        
        #Jump
        if ";" in formattedLine:
            jump=formattedLine.split(';')[1]
        else:
            jump="null"
        
        #Dest
        if '=' in formattedLine:
            dest=formattedLine.split("=")[0]
        else:
            dest="null"
        
        #Comp
        if "=" in formattedLine:
            comp=formattedLine.split(';')[0].split("=")[1]
        else:
            comp =formattedLine.split(';')[0]

        return dest,comp,jump
            
        