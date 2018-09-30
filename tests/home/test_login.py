from selenium import webdriver
from selenium.webdriver.common.by import By
from pages.home.login_page import LoginPage
import utilities.logger as cl
import logging
import pytest


@pytest.mark.usefixtures("oneTimeSetUp", "setUp")
class TestLogin():

    @pytest.fixture(autouse=True)
    def classSetup(self, oneTimeSetUp):
        self.lp = LoginPage(self.driver)


    @pytest.mark.run(order=2)
    def test_validLogin(self):
        self.lp.login("Rakeshsingh556585@gmail.com",'new@123')
        result = self.lp.verifyLoginSucess()
        assert result == True
        self.lp.logout()

    @pytest.mark.run(order=1)
    def test_invalidLogin(self):
        self.lp.login("Rakeshsingh556585@gmail.com", 'new1@123')
        result = self.lp.verifyLoginfailure()
        assert result == True



