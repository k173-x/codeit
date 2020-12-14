from setuptools import setup,find_packages

setup(
  name='codeit',
  version='0.0.1',
  author='Aadhitya A',
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
