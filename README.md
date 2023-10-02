# PythonProjectTemplater
Creates a custom named Python project template in command line as per Jean-Paul Calderone's Filesystem structure of a Python project

Based on the StackOverflow answer post at https://stackoverflow.com/a/5998845 . The structure is given bellow (copied from the post). The command-line-prompted project name will be lower-cased for the sub-directory project names while the root naming remains as-is. Uses the 'x' file open mode andw will not overwrite anything. The source files are empty.

Project/
|-- bin/
|   |-- project
|
|-- project/
|   |-- test/
|   |   |-- __init__.py
|   |   |-- test_main.py
|   |   
|   |-- __init__.py
|   |-- main.py
|
|-- setup.py
|-- README
