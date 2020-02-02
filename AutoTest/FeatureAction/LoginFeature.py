from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from AutoTest.Lib.Log import Log


class LoginFeature:

    def __init__(self, context):
        self.driver = context.driver

    def wait_logging_page_opened(self):
        Log.info("Wait for logging page opened")
        wait = WebDriverWait(self.driver, 10)
        wait.until(EC.presence_of_element_located((By.ID, 'username')))
        Log.info("Page opened")
