"""
Class used to create logs with messages and screenshots in Logs folder
"""
import os
from time import gmtime, strftime
import pyautogui


class Log:
    screenshotNumber = 0
    testLogFolderPath = ""
    driver = None
    fileName = ""

    def __init__(self, driver, log_name):
        """
        Creates html file with given log_name
        :param driver: Driver
        :type driver: WebDriver
        :param log_name: name for html log file (will be placed in Logs folder)
        :type log_name: str
        """
        Log.driver = driver
        log_folder = os.path.join(os.path.dirname(os.path.abspath(__file__)),
                                  os.pardir, os.pardir, "Logs")
        if any(x.startswith(log_name) for x in os.listdir(log_folder)):
            log_duplicate_names = []
            for x in os.listdir(log_folder):
                if x.startswith(log_name):
                    try:
                        log_duplicate_names.append(int(x.split("-")[1]))
                    except:
                        pass
            try:
                last_number = max(log_duplicate_names)
            except:
                last_number = 0
            new_number = last_number + 1
            current_log_folder = os.path.join(log_folder, log_name + "-" + str(new_number))
            os.mkdir(current_log_folder)
        else:
            current_log_folder = os.path.join(log_folder, log_name)
            os.mkdir(current_log_folder)
        Log.testLogFolderPath = current_log_folder
        Log.fileName = os.path.join(current_log_folder, log_name + ".html")
        with open(Log.fileName, "w+") as f:
            pass

    @staticmethod
    def info(msg):
        """
        Log info message in log
        :param msg: Message to log
        :type msg: str
        """
        time = strftime("%Y-%m-%d %H:%M:%S", gmtime())
        msg = time + " -- " + msg
        with open(Log.fileName, "a") as f:
            f.writelines("<p>" + msg + "</p>" + "\n")

    @staticmethod
    def screenshot(msg="", full_screen=False):
        """
        Log screenshot with message
        :param msg: Message to log
        :type msg: str
        :param full_screen: Should full screen be captured or current page
        :type full_screen: bool
        """
        time = strftime("%Y-%m-%d %H:%M:%S", gmtime())
        if msg != "":
            msg = time + " -- " + msg
        screenshot_name = str(Log.screenshotNumber) + ".png"
        picture_path = os.path.join(Log.testLogFolderPath, screenshot_name)
        Log.screenshotNumber += 1
        if full_screen:
            pyautogui.screenshot(picture_path)
        else:
            Log.driver.save_screenshot(picture_path)

        with open(Log.fileName, "a") as f:
            f.writelines("<p><a href='{}'><img src='{}' height='150px' width='200px'></img></a>{}</p>".format(
                screenshot_name, screenshot_name, "<br>"+msg if msg != "" else "") + "\n")
