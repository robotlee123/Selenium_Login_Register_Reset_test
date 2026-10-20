from selenium import webdriver
from helper.helper_base import HelperFunc

def get_browser(browser):
    if browser == "chrome":
        return HelperFunc(webdriver.Chrome()) #initialise HelperFunc object with chrome webdriver, test will be run in chrome