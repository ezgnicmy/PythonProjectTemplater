# GENERAL: Create a class template based on the given project name, with command line param support and -y

import os
import sys

import argparse # For processing command line paramameters

# A directory and file creator

def create_directory_and_files(cwd, path_list, files=None):
    while (path_list is not None and len(path_list) > 0):
        new_dir = path_list.pop(0)      
        cwd = os.path.join(cwd, new_dir)
        if not os.path.exists(cwd):
            os.makedirs(cwd)
            print('Creating a dir:', cwd)
    for file in files:
        if not os.path.exists(os.path.join(cwd,file)):
            # Opens files exclusively for creating them, fails if it exists
            f = open(os.path.join(cwd,file), "x")
            f.close()
            print('Creating a file:', file, 'in the directory:', cwd)


# Parse directory name parameters and the possible confirmation-skipping flag

parser = argparse.ArgumentParser("Directory name parser")
parser.add_argument("strings", metavar="strings", nargs='*', type=str)
parser.add_argument("-y", "--yes", dest="skip_flag", help="Skips the name confirmation prompt, useful in scripts and automated runs", default=None, action="store_true")

args = parser.parse_args()

#print(args.strings, args.skip_flag) # DEBUG
#sys.exit() # DEBUG

template_name = []

# Show start-of-the-program greeting
if args.strings is None:
    print("W-come to the Project Template Creator. Give a project name to create a directory template for.")
    template_name.append(input())
else:
    template_name = args.strings

for tmp_string in template_name:

    cwd = os.getcwd()
    tmp_path = os.path.join(cwd, tmp_string)

    # Check if the directory already exists
    if os.path.exists(tmp_path) and os.path.isdir(tmp_path):
        print("Error - the directory \'%s\' already exists. Skipping it without creating anything." % tmp_path)
        continue

# Check for a skip_flag or confirmation
    if args.skip_flag is None:
        print("Creating a project template for the name \'%s\', are you sure? (y/n) >" %  tmp_string)
        choice = str(input())
        if choice != 'y' and choice != 'yes':
            continue # Skip to the next variable upon failure to get a positive confirmation


    print("Creating a project template for the name \'%s\'..." %  tmp_string)

# Create-only files for the template

    lower_case_name = tmp_string.lower()

    path_list0 = [tmp_string]
    path_list1 = ['bin', lower_case_name]
    path_list2 = [lower_case_name, 'test']
    path_list3 = [lower_case_name]

    files0 = ['setup.py', 'README']
    files1 = []
    files2 = ['__init__.py', 'test_main.py']
    files3 = ['__init__.py', 'main.py']


# Create the root project directory
    create_directory_and_files(cwd, path_list0, files0)

    new_path = os.path.join(cwd, tmp_string)

#create_directory_and_files(new_path, path_list0, files0)

    cwd = new_path

# Create the rest of the project directories
    create_directory_and_files(cwd, path_list1, files1)
    create_directory_and_files(cwd, path_list2, files2)
    create_directory_and_files(cwd, path_list3, files3)



