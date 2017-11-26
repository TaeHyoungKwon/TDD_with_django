from selenium import webdriver
import unittest

class newVisitorTest(unittest.TestCase):

    def setUp(self):
        self.browser = webdriver.Firefox()

    def tearDown(self):
        self.browser.quit()

    def test_can_start_a_list_and_retrieve_it_later(self):
        #Edith has heart about a cool new online to-do app. 
        #Shoe goed to check out its homeplage

        self.browser.get('http://localhost:8000')

        #She notices the page title and header mention to-do lists
        self.assertIn('To-Do', self.browser.title)
        self.fail('Finish the test!')

        #she is invied to enter a to-do item straight away

    if __name__ == '__main__':
        unittest.main(warnings='ignore')