from selenium import webdriver
import unittest
import os
import pathlib

def file_uri(filename):
    return pathlib.Path(os.path.abspath(filename)).as_uri()
# On window, it's a bit weird, hacking the driver for now.
DRIVER_PATH = pathlib.Path(os.path.abspath('geckodriver.exe')).as_posix() 

class NewVistorTest(unittest.TestCase):

    def setUp(self):        
        self.browser = webdriver.Firefox(executable_path=DRIVER_PATH)
        self.browser.implicitly_wait(3)
        
    
    def tearDown(self):
        self.browser.quit()

    def test_can_add_items_to_shopping_cart_and_retreive_later(self):
        # Nok heard about a nice pizza shop
        # He checks their homepage
        self.browser.get('http://localhost:8000')

        #He found the title and header shows 'Pizza'
        self.assertEqual('Pizza', self.browser.title)
        header_text = self.browser.find_element_by_tag_name('h1').text
        self.assertEqual('Pizza', header_text)
        

        # He saw a menus for pizza abd various types of items
        menu = self.browser.find_element_by_id('menu')
        self.assertEqual(menu.get_attribute('placeholder'))
        # He try to select a small pepperoni pizza and add them into a shopping cart
        add_button = self.browser.find_element_by_id('add_item')
        self.fail('Finish the test!')

        # The web shows a total price of the pizza that he ordered
        # He try to checkout

if __name__ == "__main__":
    unittest.main(warnings='ignore')

    


