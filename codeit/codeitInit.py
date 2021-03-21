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
    print(colored.green('Files have been created. Happy Coding!'))


# For template 2
def init_agg(contestName, fileNames):
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
    print(colored.green('Files have been created. Happy Coding!'))

def create_only_files(contestName, fileNames):
  try:
    print(colored.blue('Making files for ' + colored.magenta(contestName)))
    os.makedirs(os.path.join(os.getcwd(), contestName))
  except OSError:
    print(colored.red("Failed! This directory cannot be created as it exists."))
  else:
    print(colored.yellow('Directory is made'))
      # create files for contest (should be 6 cpp files)
    for files in range(len(fileNames)):
      write_to_file(fileNames[files], template_agg(), contestName)

    print(colored.green('Files have been created. Happy Coding!'))
