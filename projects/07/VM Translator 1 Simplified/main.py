import os
import glob
from VMTranslator import VMTranslator
import argparse

parser = argparse.ArgumentParser(prog="VMTranslator",description="Translates VM code to Assembly code")

parser.add_argument("mode",help="One file or Every *.vm file?", choices=["f","d","file","directory"])
parser.add_argument("name",help="File/Directory will translate ", nargs="?")
parser.add_argument("-p", "--printline", help="Writes line numbers and instructions on .asm file", action="store_true")
args = parser.parse_args()



if args.mode in["d","directory"]:
    if args.name != None:#Default current directory
        os.chdir(args.name)

    dir_files = glob.glob("*.vm")

    for file in dir_files:
        file_name = os.path.splitext(file)[0]
        translator = VMTranslator(file_name,args.printline)
        translator.translate()
else:
    if args.name != None:
        file_name = os.path.splitext(args.name)[0]
    else:
        dir_files = glob.glob("*.vm")
        try:
            file_name = os.path.splitext(dir_files[0])[0]
        except:
            print("There is no .vm file in current directory")
            exit()

    translator = VMTranslator(file_name,args.printline)
    translator.translate()


