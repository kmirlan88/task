from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait

import logging
import os


cwd = os.getcwd()

logging.basicConfig(level=logging.INFO, format='%(asctime)s  %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p')

driver = webdriver.Chrome(cwd + '/chromedriver')

wait = WebDriverWait(driver, 5)

home_page = "http://store.aiononline.com/store/index"


def go_to_home_page():
    """
    Goes to the home page
    :return: None
    """
    driver.get(home_page)


def end_test():
    """
    Closes browser session
    :return: None
    """
    driver.quit()
