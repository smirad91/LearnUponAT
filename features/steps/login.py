from behave import use_step_matcher, given, when, then, step
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from AutoTest.FeatureAction.LoginFeature import LoginFeature
from AutoTest.Lib.Log import Log
from AutoTest.Lib.NonAppSpecific import send_text
from AutoTest.ElementRepository.LoggingRepository import LoggingRepository

use_step_matcher("re")


@given('I have logging page "(.*?)" opened in browser')
def step_impl(context, url):
    """
    :type context: behave.runner.Context
    :type url: str
    """
    Log.info("Open page: {}".format(url))
    # context.driver.implicitly_wait(15)
    context.driver.get(url)
    lf = LoginFeature(context)
    lf.wait_logging_page_opened()


@when('I input (?P<username>.*) as username and (?P<password>.*) as password')
def step_impl(context, username, password):
    """
    :type context: behave.runner.Context
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
        # LoggingRepository.inp_password(context).send_keys(password)
        send_text(LoggingRepository.inp_password(context), password)
        wait.until(EC.text_to_be_present_in_element_value((By.ID, 'password'), password))
        Log.info("Password added")
    Log.screenshot("Entered credentials username:{}, password:{}".format(username, password))


@step('click "Login" button from logging page')
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    Log.info("Click on login button")
    LoggingRepository.btn_login(context).click()
    wait = WebDriverWait(context.driver, 10)
    wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "b[id='info']")))
    Log.screenshot("Button login executed")


@then('page with login information status "(.*?)" opens')
def step_impl(context, login_status):
    """
    :type context: behave.runner.Context
    :type login_status: str
    """
    Log.info("Check if page is opened with status {}".format(login_status))
    assert(login_status in LoggingRepository.b_loginStatus(context).text)
    Log.info("Page opened")
