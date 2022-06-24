import os
import shutil
from distutils.dir_util import copy_tree

import logging
import sys

logger = logging.getLogger()
logger.setLevel(logging.INFO)
formatter = logging.Formatter('%(asctime)s | %(levelname)s | %(message)s')

stdout_handler = logging.StreamHandler(sys.stdout)
stdout_handler.setLevel(logging.DEBUG)
stdout_handler.setFormatter(formatter)

file_handler = logging.FileHandler('logs.log')
file_handler.setLevel(logging.DEBUG)
file_handler.setFormatter(formatter)


logger.addHandler(file_handler)
logger.addHandler(stdout_handler)


_FOLDERS = '123;Option'
walk_dir = r'books'

_des_dir = r'books/456/'

print('walk_dir = ' + walk_dir)


print('walk_dir (absolute) = ' + os.path.abspath(walk_dir))

for root, subdirs, files in os.walk(walk_dir):
    print('--\nroot = ' + root)
    folder_name = root[root.rfind('/')+1:]
    if folder_name in _FOLDERS.split(";"):
        logger.info( "Found: %s", folder_name)
        copy_tree(root, _des_dir) 

    # list_file_path = os.path.join(root, 'my-directory-list.txt')
    # print('list_file_path = ' + list_file_path)

    # with open(list_file_path, 'wb') as list_file:
    #     for subdir in subdirs:
    #         print('\t- subdirectory ' + subdir)

    for filename in files:
        file_path = os.path.join(root, filename)

        logger.info('\t- file %s (full path: %s)' % (filename, file_path))
