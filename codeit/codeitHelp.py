from clint.textui import colored

def help():
    print('\n')

    print(colored.green("""
.d88b .d88b. 888b. 8888 w  w   
8P    8P  Y8 8   8 8www w w8ww 
8b    8b  d8 8   8 8    8  8   
`Y88P `Y88P' 888P' 8888 8  Y8P 
                               
"""))
    print('\n')

    print(colored.cyan("A CLI Script tool to help you initialize CPP files for any contest"))
    print('\nCommands:\n')
    print(colored.yellow("codeit -h -------------------- To display help menu"))
    print(colored.yellow("codeit -i <contest> ---------- To initialize a contest directory"))
    print(colored.yellow("codeit -i -n <file> ---------- To initialize only a single file"))
    print(colored.yellow("codeit -v -------------------- To print version number"))
    print(colored.yellow("codeit -p -------------------- To parse and compile the program"))