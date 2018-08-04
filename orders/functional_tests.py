from selenium import webdriver
import unittest
import os
import pathlib

def file_uri(filename):
    return pathlib.Path(os.path.abspath(filename)).as_uri()

DRIVER_PATH = pathlib.Path(os.path.abspath('geckodriver.exe')).as_posix() # On window, it's a bit weird, hacking for now.

class NewVistorTest(unittest.TestCase):

    def setUp(self):        
        self.browser = webdriver.Firefox(executable_path=DRIVER_PATH)
        self.browser.implicitly_wait(3)
        
    
    def tearDown(self):
        self.browser.quit()

    def test_index_page_correct_title(self):
        self.browser.get('http://localhost:8000')
        self.assertEqual('Pizza', self.browser.title)


if __name__ == "__main__":
    unittest.main(warnings='ignore')

    


