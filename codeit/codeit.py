#!usr/bin/python3
import sys
import os
from clint.textui import colored
from codeit.codeitHelp import help
from codeit.codeitInit import init
from codeit.codeitMeta import template_cp, get_filename

def main():
    if len(sys.argv) < 2:
        help()

    else:
        countArg = 0
        for arg in sys.argv:
            countArg+=1

            if arg == "-i":
                if sys.argv[countArg] == '-n':
                    fileName = sys.argv[countArg+1]
                    template = template_cp()
                    init_single_file(f'{fileName}.cpp', template)
                    print(colored.yellow(f'Created {fileName}.cpp'))
                    break
                else:
                    contestName = sys.argv[countArg]
                    fileNames = get_filename()
                    init(contestName, fileNames)

            elif arg == "-v":
                print(colored.magenta('CODEIt v0.0.1'))

            elif arg == "-h":
                help()
            

def init_single_file(filename, template='\n'):
  full_filename = os.path.join(os.getcwd(), filename)
  with open(full_filename, 'w+') as f:
    f.write(template)

