from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
class HelperFunc(object):
    __TIMEOUT = 10 #timeout of 10 seconds to wait for loading of elements when finding them
    def __init__(self, driver):
        super(HelperFunc, self).__init__()
        self._driver_wait = WebDriverWait(driver, HelperFunc.__TIMEOUT)
        self._driver = driver
    # function to open a url
    def open(self, url):
        self._driver.get(url)
    # function to maximize the browser window
    def maximize(self):
        self._driver.maximize_window()
    # function to quit the driver/close the browser
    def close(self):
        self._driver.quit()
    # helper functions to find an element by its xpath, name, id
    def find_by_xpath(self, xpath):
        '''Instead of an exception if element not found return None'''
        def any_visible(driver):
            for element in driver.find_elements(By.XPATH, xpath):
                if element.is_displayed():
                    return element
            return False

        try:
            return self._driver_wait.until(any_visible)
        except TimeoutException:
            return None

    def find_by_name(self, name):
        return self._driver_wait.until(EC.visibility_of_element_located((By.NAME, name)))

    def find_by_id(self, id):
        return self._driver_wait.until(EC.visibility_of_element_located((By.ID, id)))
    # helper function to get the title of the current web page
    def get_title(self):
        return self._driver.title
    