from selenium import webdriver
import unittest

class NewVistorTest(unittest.TestCase):

    def setUp(self):        
        self.browser = webdriver.Firefox('../')
        self.browser.implicitly_wait(3)
        
    
    def tearDown(self):
        self.browser.quit()

    def test_index_page_correct_title(self):
        self.browser.get('http://localhost:8000')
        self.assertEqual('Pizzaa', self.browser.title)

if __name__ == '__main__':
    unittest.main(warnings='ignore')

    


