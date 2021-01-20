from setuptools import setup,find_packages

setup(
  name='codeit',
  version='0.0.3',
  author='Aadhitya A',
  author_email='aadhitya864@gmail.com',
  description = 'A CLI tool to create CPP files for any contest',
  license = 'GPL-3.0',
  url="https://github.com/Arch2x/codeit",
  packages=find_packages(),
  python_requires='>=3.5',
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
