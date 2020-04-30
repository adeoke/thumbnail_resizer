from invoke import task
import os
from os.path import abspath, dirname

current_dir = dirname(__file__)
incoming_path = os.path.join(current_dir, 'incoming')
print(incoming_path)


@task(help={'incomming_dir': 'Name of the directory to be deleted'})
def clean_images_dir(c, incomming_dir=None):
    """ cleans the contents of the incoming images directory """
    if incomming_dir is None:
        c.run('rm -rf {}'.format(incoming_path))
