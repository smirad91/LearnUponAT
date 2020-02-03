from behave import use_step_matcher, given, when, then, step
from AutoTest.FeatureAction.LogginFeature import LoginFeature
from AutoTest.Lib.Log import Log
from AutoTest.Lib.NonAppSpecific import send_text, wait_until
from AutoTest.ElementRepository.LoggingRepository import LoggingRepository

use_step_matcher("re")


@given('I have logging page "(.*?)" opened in browser')
def step_impl(context, url):
    """
    :type context: behave.runner.Context
    :type url: str
    """
    Log.info("Open page: {}".format(url))
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
    if username != "":
        Log.info("Insert username: {}".format(username))
        send_text(LoggingRepository().inp_username(context), username)
        wait_until(context, lambda: LoggingRepository.inp_username(context).get_attribute('value') == username,
                   timeout=10, errorMessage="Username is not correct")
        Log.info("Username added")
    if password != "":
        Log.info("Insert password: {}".format(password))
        send_text(LoggingRepository.inp_password(context), password)
        wait_until(context, lambda: LoggingRepository.inp_password(context).get_attribute('value') == password
                   , timeout=10, errorMessage="Password is not correct")
        Log.info("Password added")
    Log.screenshot("Entered credentials username:{}, password:{}".format(username, password))


@step('click "Login" button from logging page')
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    Log.info("Click on login button")
    LoggingRepository.btn_login(context).click()
    wait_until(context, lambda: context.driver.find_element_by_css_selector("b[id='info']"), timeout=10)
    Log.screenshot("Button login executed")


@then('page with login information status "(.*?)" opens')
def step_impl(context, login_status):
    """
    :type context: behave.runner.Context
    :type login_status: str
    """
    Log.info("Check if page is opened with status {}".format(login_status))
    assert (login_status in LoggingRepository.b_loginStatus(context).text)
    Log.info("Page opened")
