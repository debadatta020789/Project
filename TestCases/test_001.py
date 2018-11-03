import unittest
from selenium.webdriver import Chrome
from POM.LogIn import LoginPage
import time

class testA(unittest.TestCase):

    def setUp(self):
        self.driver=Chrome("D:/Selenium/ExeFiles/Chromedriver.exe")
        self.driver.get("https://www.facebook.com")

    def tearDown(self):
        self.driver.close()

    def testA(self):
        self.driver.implicitly_wait(30)
        login = LoginPage(self.driver)
        login.wait_for_login_page_to_load()
        login.get_username_textbox().send_keys("hgfhgfg")
        login.get_password_textbox().send_keys("dvdssv")
        login.get_login_button().click()
        time.sleep(3)
        time.sleep(3)
