"""
This is a redone version of the thumbnail maker lib from Tim Ojo.
The reason for this is that it didn't work for me and rather than fix his
implementation I decided to completely re-write it for learning purposes.
"""

import sys
from os.path import dirname
from os.path import abspath

# import urllib.request

# get the directory of this file
directory = dirname(dirname(__file__))

# get the absolute path for this directory
full_dir_path = abspath(directory)

# add this directory to the end of the path
sys.path.append(full_dir_path)


# print(sys.path)


class Downloader:
    def __init__(self):
        pass

    def download_files(self, li):
        pass

    def delete_files(self, li):
        pass
