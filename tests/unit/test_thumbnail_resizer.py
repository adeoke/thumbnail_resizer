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


if __name__ == '__main__':
    unittest.main()
