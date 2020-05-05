import unittest
import os
from os.path import abspath
from os.path import dirname

from app.thumbnail_resizer import Downloader


class TestDownloader(unittest.TestCase):
    EXPECTED_EMPTY_LIST_MESSAGE = 'list is empty'
    # Will probably prefer a config utility that has access to project root etc
    # in the mean time this assumes that the incoming directory is located in
    # the project root directory.
    INCOMING_DIR = os.path.join(abspath(dirname(dirname(dirname(__file__)))),
                                'incoming')

    def setUp(self):
        self.downloader = Downloader()

    def test_list_empty_message_returned(self):
        li = []
        actual_result = self.downloader.download_images(li)
        self.assertEqual(actual_result, self.EXPECTED_EMPTY_LIST_MESSAGE)

    def test_image_list_is_not_empty(self):
        self.assertTrue(self.downloader.image_list(),
                        'Expected list to NOT be empty, but it was EMPTY!')

    def test_images_are_downloaded_to_directory(self):
        list_images = self.downloader.image_list()
        self.downloader.download_images(list_images)
        self.assertTrue(len(os.listdir(self.INCOMING_DIR)) > 0,
                        'expected directory to NOT be empty, but it was')

    def test_resizing_image(self):
        self.downloader.perform_resizing()

    def tearDown(self):
        """I want to run the invoke task to clear the incoming directory"""
        pass


if __name__ == '__main__':
    unittest.main()
