from invoke import task
import os
from os.path import abspath, dirname

current_dir = dirname(__file__)
incoming_path = os.path.join(current_dir, 'incoming')
outgoing_path = os.path.join(current_dir, 'outgoing')
test_root = os.path.join(dirname(__file__), 'tests')
app_root = os.path.join(dirname(__file__), 'app')
print(test_root)


@task(help={'incoming_dir': 'Name of the directory to be deleted'})
def clean_incoming_images_dir(c, incomming_dir=None):
    """ cleans the contents of the incoming images directory """
    if incomming_dir is None:
        c.run('rm -rfv {}/*'.format(incoming_path))


@task(help={'outgoing_dir': 'Name of the outgoing dir contents to be deleted'})
def clean_outgoing_images_dir(c, outgoing_dir=None):
    """cleans the contents of the outgoing images directory"""
    if outgoing_dir is None:
        c.run('rm -rfv {}/*'.format(outgoing_path))


@task(help={'directory': 'Name of the test directory to run tests from'})
def run_unit_tests(c, directory=test_root):
    """Runs all the tests"""
    c.run("python -m unittest discover {} 'test_*.py'".format(directory))


@task
def run_main(c):
    """Runs the main module"""
    c.run("python {}/thumbnail_resizer.py".format(app_root))
