"""
This is a redone version of the thumbnail maker lib from Tim Ojo.
The reason for this is that it didn't work for me and rather than fix his
implementation I decided to completely re-write it for learning purposes.
"""
import os


class Downloader:
    def __init__(self, home_dir='.'):
        self.home_dir = home_dir
        self.input_dir = self.home_dir + os.path.sep + 'incoming'
        self.output_dir = self.home_dir + os.path.sep + 'outgoing'

    def download_files(self, li):
        if not li:
            return 'list is empty'

    def delete_files(self, li):
        pass
