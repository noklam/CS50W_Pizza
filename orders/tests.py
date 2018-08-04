from django.test import TestCase
from selenium import webdriver

class NewVistorTest(TestCase):

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

    # Create your tests here.
def test_index(self):
    self.assertEqual(response.status_code, 200)
