import os
from clint.textui import colored
from codeit.codeitMeta import template_cp, template_agg

def write_to_file(filename, text, contestName=None):
  full_filename = os.path.join(os.getcwd(), filename)
  if contestName is not None:
    full_filename = os.path.join(os.getcwd(), contestName, filename)
  with open(full_filename, 'w+') as f:
    f.write(text)

def init(contestName,fileNames):
  # create a directory with contest name
  try:
    print(colored.blue('Making files and folders for ' + colored.magenta(contestName)))
    os.makedirs(os.path.join(os.getcwd(), contestName))
  except OSError:
    print(colored.red("Failed! This directory cannot be created as it exists."))
  else:
    print(colored.yellow('Directory is made'))
      # create files for contest (should be 6 cpp files)
    for files in range(len(fileNames)):
      write_to_file(fileNames[files], template_cp(), contestName)
    # create input file
    write_to_file('input.txt', '', contestName)
    write_to_file('output.txt', '', contestName)
    write_to_file('error.txt', '', contestName)
    print(colored.green('Files have been created. Happy Coding!'))

def create_only_files(contestName,fileNames):
  # create a directory with contest name
  try:
    # create files for contest (should be 6 cpp files)
    currentDir = os.getcwd()
    for files in range(len(fileNames)):
      write_to_file(fileNames[files], template_cp(), currentDir)
  except OSError as e:
    print(colored.red("Failed! The Files can't be created in current Directory."))
  else:
    print(colored.green('Files have been created. Happy Coding!'))

def init_noerror(contestName, fileNames):
  try:
    print(colored.blue('Making files and folders for ' + colored.magenta(contestName)))
    os.makedirs(os.path.join(os.getcwd(), contestName))
  except OSError:
    print(colored.red("Failed! This directory cannot be created as it exists."))
  else:
    print(colored.yellow('Directory is made'))
      # create files for contest (should be 6 cpp files)
    for files in range(len(fileNames)):
      write_to_file(fileNames[files], template_cp(), contestName)
    # create input file
    write_to_file('input.txt', '', contestName)
    write_to_file('output.txt', '', contestName)
    print(colored.green('Files have been created without error TXT file. Happy Coding!'))

# For template 2
def init_noerror_agg(contestName, fileNames):
  try:
    print(colored.blue('Making files and folders for ' + colored.magenta(contestName)))
    os.makedirs(os.path.join(os.getcwd(), contestName))
  except OSError:
    print(colored.red("Failed! This directory cannot be created as it exists."))
  else:
    print(colored.yellow('Directory is made'))
      # create files for contest (should be 6 cpp files)
    for files in range(len(fileNames)):
      write_to_file(fileNames[files], template_agg(), contestName)
    # create input file
    write_to_file('input.txt', '', contestName)
    write_to_file('output.txt', '', contestName)
    print(colored.green('Files have been created without error TXT file. Happy Coding!'))
