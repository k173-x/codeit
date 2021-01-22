#!usr/bin/python3
import sys
import os
from clint.textui import colored
from codeit.codeitHelp import help
from codeit.codeitInit import init, init_noerror, init_noerror_agg, create_only_files
from codeit.codeitMeta import template_agg, template_cp, get_filename, get_fn_beginner

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
                    template = template_agg()
                    init_single_file(f'{fileName}.cpp', template)
                    print(colored.yellow(f'Created {fileName}.cpp'))
                    break
                elif sys.argv[countArg] == '-b':
                    if sys.argv[countArg+1] == '-ne':
                        contestName = sys.argv[countArg+2]
                        fileNames = get_fn_beginner()
                        init_noerror(contestName, fileNames)
                    elif sys.argv[countArg+1] == '-t2':
                        contestName = sys.argv[countArg+2]
                        fileNames = get_fn_beginner()
                        init_noerror_agg(contestName, fileNames)
                    else:
                        contestName = sys.argv[countArg+1]
                        fileNames = get_fn_beginner()
                        init(contestName, fileNames)
                elif sys.argv[countArg] == '-ne':
                    contestName = sys.argv[countArg+1]
                    fileNames = get_filename()
                    init_noerror(contestName, fileNames)
                elif sys.argv[countArg] == '-t2':
                    contestName = sys.argv[countArg+1]
                    fileNames = get_filename()
                    init_noerror_agg(contestName, fileNames)
                else:
                    contestName = sys.argv[countArg]
                    fileNames = get_filename()
                    init(contestName, fileNames)
            elif arg == "-f":
                contestName = sys.argv[countArg]
                fileNames = get_filename()
                create_only_files(contestName, fileNames)

            elif arg == "-v":
                print(colored.magenta('CODEIt v0.0.3 (c)2020 - 2021, alphaX86 under Arch-1'))

            elif arg == "-h":
                help()


def init_single_file(filename, template='\n'):
  full_filename = os.path.join(os.getcwd(), filename)
  with open(full_filename, 'w+') as f:
    f.write(template)
