# GENERAL: Create a class template based on the given project name

import os

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



print("W-come to the Project Template Creator. Give a project name to create a directory template for.")
template_name = input()
print("Creating a project template for the name \'%s\'..." %  template_name)

# Create-only files for the template

lower_case_name = template_name.lower()

path_list0 = [template_name]
path_list1 = ['bin', lower_case_name]
path_list2 = [lower_case_name, 'test']
path_list3 = [lower_case_name]

files0 = ['setup.py', 'README']
files1 = []
files2 = ['__init__.py', 'test_main.py']
files3 = ['__init__.py', 'main.py']


cwd = os.getcwd()

# Create the root project directory
create_directory_and_files(cwd, path_list0, files0)

new_path = os.path.join(cwd, template_name)

#create_directory_and_files(new_path, path_list0, files0)

cwd = new_path

# Create the rest of the project directories
create_directory_and_files(cwd, path_list1, files1)
create_directory_and_files(cwd, path_list2, files2)
create_directory_and_files(cwd, path_list3, files3)



