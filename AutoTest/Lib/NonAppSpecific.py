"""
Methods that can be used for every site
"""
import time

from Lib.common.WaitAction import wait_until
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from AutoTest.Lib.Driver import Driver


def wait_until(somepredicate, timeout=60, period=1, errorMessage="Timeout expired"):
    """
    Somepredicate is function that returns True or False. This function is executed every for period during
    timeout. When somepredicate return True wait is done. If somepredicate don't return True during timeout,
    exception is raised.

    :param somepredicate: Function that return True of False
    :type somepredicate: func
    :param timeout: Timeout to wait
    :type timeout: int
    :param period: Execute function for every period seconds
    :type period: float
    :return:
    """
    mustend = time.time() + timeout
    value = False
    while time.time() < mustend:
        try:
            value = somepredicate()
        except Exception as ex:
            # print(ex)
            pass
        if value:
            return True
        time.sleep(period)
    raise Exception(errorMessage)


def wait_element_visible(driver, css_selector, timeout=30):
    """
    Wait for element with cssSelector to be shown on browser.

    :param driver: Driver
    :type driver: WebDriver
    :param css_selector: Css selector form
    :type css_selector: str
    :return: 
    """""
    wait = WebDriverWait(driver, timeout)
    wait.until(expected_conditions.visibility_of_element_located(
        (By.CSS_SELECTOR, css_selector)))

def wait_page_load(driver):
    """
    Wait page to load
    """
    wait_until(lambda: Driver.driver.execute_script("return document.readyState;") == "complete", timeout=30)

def send_text(element, text, mode="set"):
    """
    Send text with mode set or update. Set mode types into input field. Update mode first clear
    text from input field and then types text.
    :param element: Element for input text
    :type element: WebElement
    :param text: Text to input
    :type text: str
    :param mode: Possible values are 'set' and 'update'.
    :type mode: str
    :return:
    """
    if mode is "set":
        element.send_keys(text)
    elif mode is "update":
        element.clear()
        element.send_keys(text)
    else:
        raise Exception("Possible values for mode are set and update. Given mode is={}".format(mode))