from django.test import TestCase
from selenium import webdriver
import os

def file_uri(filename):
    return pathlib.Path(os.path.abspath(filename)).as_uri()

DRIVER_PATH = pathlib.Path(os.path.abspath('geckodriver.exe')).as_posix() # On window, it's a bit weird, hacking for now.


PATH = os.path.abspath('geckodriver.exe')
    # Create your tests here.
def test_index(self):
    self.assertEqual(response.status_code, 200)
