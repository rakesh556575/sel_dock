
from selenium import webdriver
from selenium.webdriver.common.by import By
from base.selenium_driver import SeleniumDriver
import utilities.logger as cl
import logging

from base.selenium_driver import SeleniumDriver
import utilities.logger as cl
import logging

class LoginPage(SeleniumDriver):

    log = cl.customLogger(logging.DEBUG)

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Locators
    _login_link = "Login"
    _email_field = "user_email"
    _password_field = "user_password"
    _login_button = "commit"
    _profile_xpath=".//*[@id='navbar']//span[text()='Rakesh Kushwaha']"
    _log_out_button=" Log Out   "

    def clickLoginLink(self):
        self.elementClick(self._login_link, locatorType="link")

    def enterEmail(self, email):
        self.sendKeys(email, self._email_field)

    def enterPassword(self, password):
        self.sendKeys(password, self._password_field)

    def clickLoginButton(self):
        self.elementClick(self._login_button, locatorType="name")

    def logout(self):
        self.elementClick(self._profile_xpath,locatorType="xpath")
        self.elementClick(self._log_out_button,locatorType="link")

    def login(self, email, password):
        self.waitForElement(self._login_link)
        self.clickLoginLink()

        self.enterEmail(email)
        self.enterPassword(password)
        self.clickLoginButton()


    def verifyLoginSucess(self):
        result=self.isElementPresent(".//*[@id='navbar']//span[text()='Rakesh Kushwaha']",locatorType="xpath")
        return result


    def verifyLoginfailure(self):
        result=self.isElementPresent(".//div[contains(text(),'Invalid email or password')]",locatorType="xpath")
        return result