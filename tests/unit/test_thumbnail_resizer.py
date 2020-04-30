import unittest

from app.thumbnail_resizer import Downloader


class TestDownloader(unittest.TestCase):
    def setUp(self):
        self.downloader = Downloader()

    def test_downloading(self):
        li = []
        self.downloader.download_files(li)


if __name__ == '__main__':
    unittest.main()
