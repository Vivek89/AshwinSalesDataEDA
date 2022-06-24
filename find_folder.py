import os
import shutil
from distutils.dir_util import copy_tree

_FOLDERS = '456;Option'
walk_dir = r'books'

_des_dir = r'books/123/'

print('walk_dir = ' + walk_dir)


print('walk_dir (absolute) = ' + os.path.abspath(walk_dir))

for root, subdirs, files in os.walk(walk_dir):
    print('--\nroot = ' + root)
    folder_name = root[root.rfind('/')+1:]
    if folder_name in _FOLDERS.split(";"):
        print( "Found: ", folder_name)
        copy_tree(root, _des_dir) 

    # list_file_path = os.path.join(root, 'my-directory-list.txt')
    # print('list_file_path = ' + list_file_path)

    # with open(list_file_path, 'wb') as list_file:
    #     for subdir in subdirs:
    #         print('\t- subdirectory ' + subdir)

    for filename in files:
        file_path = os.path.join(root, filename)

        print('\t- file %s (full path: %s)' % (filename, file_path))
