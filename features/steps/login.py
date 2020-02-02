from behave import use_step_matcher, given, when, then, step
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from AutoTest.Lib.Log import Log
from AutoTest.Lib.NonAppSpecific import send_text, wait_page_load
from AutoTest.ElementsRepository.LoggingRepository import LoggingRepository

use_step_matcher("re")


@given('I have logging page "(.*?)" opened in browser')
def step_impl(context, url):
    """
    :type url: str
    """
    Log.info("Open page: {}".format(url))
    context.driver.get(url)
    wait = WebDriverWait(context.driver, 10)
    wait.until(EC.presence_of_element_located((By.ID, 'username')))
    Log.info("Page opened")


@when('I input (?P<username>.*) as username and (?P<password>.*) as password')
def step_impl(context, username, password):
    """
    :type username: str
    :type password: str
    """
    wait = WebDriverWait(context.driver, 10)
    if username is not "":
        Log.info("Insert username: {}".format(username))
        # LoggingFeature.inp_username(context).send_keys(username)
        send_text(LoggingRepository.inp_username(context), username)
        wait.until(EC.text_to_be_present_in_element_value((By.ID, 'username'), username))
        Log.info("Username added")
    if password is not "":
        Log.info("Insert password: {}".format(password))
        LoggingRepository.inp_password(context).send_keys(password)
        wait.until(EC.text_to_be_present_in_element_value((By.ID, 'password'), password))
    Log.screenshot("Entered credentials username:{}, password:{}".format(username, password))


@step('click "Login" button from logging page')
def step_impl(context):
    Log.info("Click on login button")
    LoggingRepository.btn_login(context).click()
    Log.screenshot("Button login executed")


@then('page with login information status "(.*?)" opens')
def step_impl(context, login_status):
    """
    :type login_status: str
    """
    Log.info("Wait for page to open")
    wait = WebDriverWait(context.driver, 10)
    wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "b[id='info']")))
    assert(login_status in LoggingRepository.b_loginStatus(context).text)
    Log.info("Page opened")



