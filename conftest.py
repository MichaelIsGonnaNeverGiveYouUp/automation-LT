# add project root path to sys.path
import sys
import os

from webdriver.seleniumdriver import SeleniumDriver

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

SeleniumDriver().get_webdriver_instance()
