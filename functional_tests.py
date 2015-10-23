from selenium import webdriver
import unittest

class NewVisitorTest(unittest.TestCase):

    def setUp(self):
#        print ("in setup")
        self.browser=webdriver.Firefox()
        self.browser.implicitly_wait(3);
    def tearDown(self):
#        print ("tear down")
        self.browser.quit()

    def test_can_start_a_list_and_retrieve_it_later(self):
#        print ("testCanStartAList")
        self.browser.get('http://localhost:8000')
        self.assertIn('To-Do', self.browser.title)
        self.fail('Finish the test')

#    def test_I_added_another_test(self):
#        print ("second test")

#    def test_I_added_yet_another_test(self):
#            print ("third test")

if __name__ == '__main__':
        unittest.main(warnings='ignore')
