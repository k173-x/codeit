from setuptools import setup,find_packages

setup(
  name='codeit',
  version='0.0.2',
  author='Aadhitya A',
  description = 'A CLI tool to create CPP files',
  long_description = README,
  license = 'GPL-3.0',
  packages=find_packages(),
  install_requires=[
    'watchdog',
    'clint'
  ],
  entry_points={
    'console_scripts': [
      'codeit = codeit.codeit:main'
    ]
  }
)
