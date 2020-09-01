from django.test import LiveServerTestCase
from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from selenium.common.exceptions import WebDriverException
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import unittest
import time
import os

class NewVisitorTest(LiveServerTestCase):

    def setUp(self):
        self.browser = webdriver.FireFox()
        stage_browser = os.environ.get('STAGING_SERVER')
        if stage_server :
            self.live_server_url = 'http://' + stage_server

    def tearDown():
        self.browser.quit()

    # Alice visits the silin's cv webpage
    # She clicks a title and saw words in a white squre.
    def post_words_placed_in_a_white_area(self):
        self.browser.get(live_server_url)
        self.browser.set_window_size(1024,768)

        self.browser.find_elemnt_by_id('') 
        self.fail('Test finished')
