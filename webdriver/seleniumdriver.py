from selenium import webdriver

from singleton.singleton_decorator import singleton


@singleton
class SeleniumDriver(object):

    base_url = "https://www.saucedemo.com/"

    def __init__(self):
        self.driver = "chrome"
        self.webdriver = None

    def get_webdriver_instance(self):
        if self.webdriver is not None:
            return self.webdriver
        if self.driver == "firefox":
            self.webdriver = webdriver.Firefox()
        elif self.driver == "chrome":
            self.webdriver = webdriver.Chrome()
        elif self.driver == "ie":
            self.webdriver = webdriver.Ie()
        else:
            self.webdriver = webdriver.Chrome()
        self.webdriver.maximize_window()
        self.webdriver.implicitly_wait(3)
        self.webdriver.delete_all_cookies()
        self.webdriver.get(self.base_url)
        return self.webdriver

    def close_webdriver_instance(self):
        self.webdriver.close()
