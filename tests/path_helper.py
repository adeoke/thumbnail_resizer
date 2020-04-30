"""
One of my pet dislikes this, but I have to use it to allow me to import
the file under test within the unittest test runner.
This module adds the application under tests file to the path.
"""

from os.path import dirname
from os.path import abspath
import sys

# get the directory of this file
directory = dirname(dirname(dirname(__file__)))

# get the absolute path for this directory
full_dir_path = abspath(directory)

# add this directory to the end of the path
sys.path.append(full_dir_path)
