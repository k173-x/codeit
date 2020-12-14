from clint.textui import colored

def help():
    print('\n')

    print(colored.white(""" ██████╗ ██████╗ ██████╗ ███████╗██╗████████╗
██╔════╝██╔═══██╗██╔══██╗██╔════╝██║╚══██╔══╝
██║     ██║   ██║██║  ██║█████╗  ██║   ██║   
██║     ██║   ██║██║  ██║██╔══╝  ██║   ██║   
╚██████╗╚██████╔╝██████╔╝███████╗██║   ██║   
 ╚═════╝ ╚═════╝ ╚═════╝ ╚══════╝╚═╝   ╚═╝   
                                             """))

    print(colored.cyan("A CLI Script tool to help you initialize CPP files for any contest"))
    print('\nCommands:\n')
    print(colored.magenta("codemon <flags> <args>\n"))
    print(colored.red('Args list\n'))
    print(colored.yellow("-h \n" + colored.blue("To display help menu")))
    print(colored.yellow("-i <contest> \n" + colored.blue("To initialize a contest directory")))
    print(colored.yellow("-i -b <contest> \n" + colored.blue("To initialize a contest directory for practice and beginner level")))
    print(colored.yellow("-i <args> -ne <contest> \n" + colored.blue("To initialize a contest directory without error.txt file")))
    print(colored.yellow("-i -n <file> \n"  + colored.blue("To initialize only a single file")))
    print(colored.yellow("-v \n" + colored.blue("To print version number")))