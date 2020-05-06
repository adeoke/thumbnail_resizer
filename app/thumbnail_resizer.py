"""
This is a redone version of the thumbnail maker lib from Tim Ojo.
The reason for this is that it didn't work for me and rather than fix his
implementation I decided to completely re-write it for learning purposes.
"""
import os, ssl
import urllib.request
import logging
import time
import PIL
from PIL import Image
import threading

FORMAT = "[%(threadName)s, %(asctime)s, %(levelname)s] %(message)s"
logging.basicConfig(filename='logfile.log', level=logging.DEBUG, format=FORMAT)


class Downloader:
    def __init__(self, home_dir='.'):
        self.home_dir = home_dir
        self.input_dir = self.home_dir + os.path.sep + 'incoming'
        self.output_dir = self.home_dir + os.path.sep + 'outgoing'
        self.downloaded_bytes = 0
        self.dl_lock = threading.Lock()

    @staticmethod
    def image_list():
        li = [
            'https://dl.dropboxusercontent.com/s/2fu69d8lfesbhru/pexels-photo-48603.jpeg',
            'https://dl.dropboxusercontent.com/s/zch88m6sb8a7bm1/pexels-photo-134392.jpeg',
            'https://dl.dropboxusercontent.com/s/lsr6dxw5m2ep5qt/pexels-photo-135130.jpeg',
            'https://dl.dropboxusercontent.com/s/6xinfm0lcnbirb9/pexels-photo-167300.jpeg',
            'https://dl.dropboxusercontent.com/s/2dp2hli32h9p0y6/pexels-photo-167921.jpeg',
            'https://dl.dropboxusercontent.com/s/fjb1m3grcrceqo2/pexels-photo-173125.jpeg',
            'https://dl.dropboxusercontent.com/s/56u8p4oplagc4bp/pexels-photo-185934.jpeg',
            'https://dl.dropboxusercontent.com/s/2s1x7wz4sdvxssr/pexels-photo-192454.jpeg',
            'https://dl.dropboxusercontent.com/s/1gjphqnllzm10hh/pexels-photo-193038.jpeg',
            'https://dl.dropboxusercontent.com/s/pcjz40c8pxpy057/pexels-photo-193043.jpeg',
            'https://dl.dropboxusercontent.com/s/hokdfk7y8zmwe96/pexels-photo-207962.jpeg',
            'https://dl.dropboxusercontent.com/s/k2tk2co7r18juy7/pexels-photo-247917.jpeg',
            'https://dl.dropboxusercontent.com/s/m4xjekvqk4rksbx/pexels-photo-247932.jpeg',
            'https://dl.dropboxusercontent.com/s/znmswtwhcdbpc10/pexels-photo-265186.jpeg',
            'https://dl.dropboxusercontent.com/s/jgb6n4esquhh4gu/pexels-photo-302899.jpeg',
            'https://dl.dropboxusercontent.com/s/rjuggi2ubc1b3bk/pexels-photo-317156.jpeg',
            'https://dl.dropboxusercontent.com/s/cpaog2nwplilrz9/pexels-photo-317383.jpeg',
            'https://dl.dropboxusercontent.com/s/16x2b6ruk18gji5/pexels-photo-320007.jpeg',
            'https://dl.dropboxusercontent.com/s/xqzqzjkcwl52en0/pexels-photo-322207.jpeg',
            'https://dl.dropboxusercontent.com/s/frclthpd7t8exma/pexels-photo-323503.jpeg',
            'https://dl.dropboxusercontent.com/s/7ixez07vnc3jeyg/pexels-photo-324030.jpeg',
            'https://dl.dropboxusercontent.com/s/1xlgrfy861nyhox/pexels-photo-324655.jpeg',
            'https://dl.dropboxusercontent.com/s/v1b03d940lop05d/pexels-photo-324658.jpeg',
            'https://dl.dropboxusercontent.com/s/ehrm5clkucbhvi4/pexels-photo-325520.jpeg',
            'https://dl.dropboxusercontent.com/s/l7ga4ea98hfl49b/pexels-photo-333529.jpeg',
            'https://dl.dropboxusercontent.com/s/rleff9tx000k19j/pexels-photo-341520.jpeg'
        ]
        return li

    def download_image(self, url, index):
        logging.info('downloading image at URL ' + url)
        dest_path = "{}/image-{}.jpg".format(self.input_dir, index)
        urllib.request.urlretrieve(url, dest_path)
        img_size = os.path.getsize(dest_path)

        #  prevent any other thread from modifying the downloaded_bytes var.
        with self.dl_lock:
            self.downloaded_bytes += img_size

        logging.info(
            "image [{} bytes] saved to: {}".format(img_size, dest_path))

    def download_images(self, li):
        """
        :param li: list of images to scan over
        :return: no return, just perform the action
        """

        # this is used to ignore ssl cert issues
        if (not os.environ.get('PYTHONHTTPSVERIFY', '') and
                getattr(ssl, '_create_unverified_context', None)):
            ssl._create_default_https_context = ssl._create_unverified_context

        if not li:
            return 'list is empty'

        # check the directory existence before downloading
        os.makedirs(self.input_dir, exist_ok=True)

        logging.info('beginning image download')

        start_time = time.perf_counter()

        threads = []

        for index, url in enumerate(li):
            thread = threading.Thread(target=self.download_image,
                                      args=(url, index))
            thread.start()
            threads.append(thread)

        for t in threads:
            t.join()

        end_time = time.perf_counter()

        logging.info("downloaded {} images in {} seconds".format(len(li),
                                                                 end_time - start_time))

    def perform_resizing(self):
        """resize the images from in the incoming directory"""
        if not os.listdir(self.input_dir):
            return

        os.makedirs(self.output_dir, exist_ok=True)

        logging.info('beginning image resizing')
        target_sizes = [32, 64, 200]
        num_images = 0

        start = time.perf_counter()
        for image_filename in os.listdir(self.input_dir):
            for image_width in target_sizes:
                with Image.open(
                        os.path.join(self.input_dir, image_filename)) as img:
                    new_height = int((image_width / img.width) * img.height)

                    img = img.resize((image_width, new_height),
                                     PIL.Image.LANCZOS)
                    num_images += 1
                    file_extension = os.path.splitext(image_filename)[-1]
                    filename = os.path.splitext(image_filename)[0]
                    new_filename = '{}_w_{}_h_{}{}'.format(filename,
                                                           int(image_width),
                                                           int(new_height),
                                                           file_extension)
                    print(os.path.join(self.output_dir, new_filename))
                    print('---\n\n')
                    img.save(os.path.join(self.output_dir, new_filename))
            os.remove(os.path.join(self.input_dir, image_filename))
        end = time.perf_counter()

        logging.info("created {} thumbnails in {} seconds".format(num_images,
                                                                  end - start))

    def make_thumbnails(self, img_url_list):
        logging.info("START make_thumbnails")
        start = time.perf_counter()

        self.download_images(img_url_list)
        self.perform_resizing()

        end = time.perf_counter()
        logging.info("END make_thumbnails in {} seconds".format(end - start))


if __name__ == '__main__':
    downloader = Downloader()
    downloader.make_thumbnails(Downloader.image_list())
