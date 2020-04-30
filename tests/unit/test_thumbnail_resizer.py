import unittest

from app.thumbnail_resizer import Downloader


class TestDownloader(unittest.TestCase):
    EXPECTED_EMPTY_LIST_MESSAGE = 'list is empty'

    def setUp(self):
        self.downloader = Downloader()

    def test_list_empty_message_returned(self):
        li = []
        actual_result = self.downloader.download_files(li)
        self.assertEqual(actual_result, self.EXPECTED_EMPTY_LIST_MESSAGE)

    def test_image_list_is_not_empty(self):
        self.assertTrue(self.downloader.image_list(),
                        'Expected list to NOT be empty, but it was EMPTY!')

    def test_images_are_downloaded_to_directory(self):
        list_images = self.downloader.image_list()
        self.downloader.download_files(list_images)



if __name__ == '__main__':
    unittest.main()
