import os
import pathlib
from django.test import TestCase
from selenium import webdriver
from django.urls import resolve
from orders.views import index

def file_uri(filename):
    return pathlib.Path(os.path.abspath(filename)).as_uri()

DRIVER_PATH = pathlib.Path(os.path.abspath('geckodriver.exe')).as_posix() # On window, it's a bit weird, hacking for now.

    # Create your tests here.
class HomePageTest(TestCase):

    def test_root_url_resolves_to_index_page_view(self):
        found = resolve('/')
        self.assertEqual(found.func, index)    
