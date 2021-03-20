from clint.textui import colored


def help():
    function = {"  -h ": " To display help menu.",
                "  -i <contest> ": " To initialize a contest directory.",
                "  -f ": " To create only files in a directory.", 
                "  -i -b <contest> ": " To initialize a contest directory for practice and beginner level.",
                "  -i <args> -t2 <contest> ": " To initialize a contest directory and use 2nd template.",
                "  -i -n <file> ": " To initialize only a single file.",
                "  -v ": " To print version number."}

    print('\n')

    print(colored.red("""  ██████╗  ██████╗  ██████╗  ███████╗ ██╗ ████████╗
 ██╔════╝ ██╔═══██╗ ██╔══██╗ ██╔════╝ ██║ ╚══██╔══╝
 ██║      ██║   ██║ ██║  ██║ █████╗   ██║    ██║   
 ██║      ██║   ██║ ██║  ██║ ██╔══╝   ██║    ██║   
 ╚██████╗ ╚██████╔╝ ██████╔╝ ███████╗ ██║    ██║   
  ╚═════╝  ╚═════╝  ╚═════╝  ╚══════╝ ╚═╝    ╚═╝   """))

    print(colored.cyan(
        "\n The CLI Script tool to help you initialize CPP files for any contest."))

    print(colored.red('\n Command: '))
    print(colored.cyan("  codeit <args> <filename/contestname>"))

    print(colored.red('\n Args list: '))
    for arg, func in function.items():
        print(colored.yellow(arg) + '-'*(30-len(arg)) + '>' + colored.cyan(func))
    print('\n')
