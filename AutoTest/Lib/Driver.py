"""
Class used for creating driver
"""
from selenium import webdriver
from Lib.common.NonAppSpecific import close_driver

class Driver:
    def __init__(self):
        self.driver = None

    def create_driver(self, driver_name):
        """
        Create driver instance
        :param driver_name: browser name
        :type driver_name: str
        """
        if driver_name.lower() == "firefox":
            driver = webdriver.Firefox()
        elif driver_name.lower() == "chrome":
            driver = webdriver.Chrome()
        else:
            raise Exception("Supported drivers are Firefox and Chrome. You forwarded {}".format(driver_name))
        driver.maximize_window()
        self.driver = driver
        return driver

    def close(self):
        """
        Close driver and all handles (all tabs...)
        """
        close_driver(self.driver)
