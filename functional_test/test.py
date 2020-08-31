from django.test import LiveServerTestCase
from selenium.common.exceptions import WebDriverException
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import unittest
import time

class NewVisitorTest(LiveServerTestCase):

    def setUp(self):
        self.browser = webdriver.FireFox()

    def tearDown():
        self.browser.quit()

    # Alice visits the silin's cv webpage
    # She clicks a title and saw words in a white squre.
    def post_words_placed_in_a_white_area(self):
        self.browser.get(live_server_url)
        self.fail('Test finished')
