"""
Actions for logging feature
"""

class LoggingRepository:

    ###Elements on logging page

    @staticmethod
    def inp_username(context):
        return context.driver.find_element_by_id("username")

    @staticmethod
    def inp_password(context):
        return context.driver.find_element_by_id("password")

    @staticmethod
    def btn_login(context):
        return context.driver.find_element_by_id("submit")

    @staticmethod
    def b_loginStatus(context):
        return context.driver.find_element_by_css_selector("b[id='info']")