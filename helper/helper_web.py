from selenium import webdriver
from helper.helper_base import HelperFunc

def get_browser(browser):
    if browser == "chrome":
        options = webdriver.ChromeOptions()
        options.add_argument('--incognito')
        return HelperFunc(webdriver.Chrome(options=options))