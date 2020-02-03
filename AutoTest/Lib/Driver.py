"""
Class used for creating driver
"""
import os

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
        drivers_folder = os.path.abspath(os.path.join(os.path.dirname(os.path.abspath(__file__)),
                                                      os.pardir, os.pardir, "Drivers"))
        if driver_name.lower() == "firefox":
            driver = webdriver.Firefox(executable_path=os.path.join(drivers_folder, "geckodriver.exe"))
        elif driver_name.lower() == "chrome":
            driver = webdriver.Chrome(executable_path=os.path.join(drivers_folder, "chromedriver.exe"))
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
