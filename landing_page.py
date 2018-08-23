from selenium.webdriver.common.action_chains import ActionChains
from utilities import wait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import logging
from utilities import driver


def from_menu_get_to_list(menu_name, list_name):
    """
    Goes to specified menu and clicks on list name
    :param menu_name: Str value for menu name to hover over
    :param list_name: Str value for list name to open
    :return: None
    """
    menu_to_hover = wait.until(EC.element_to_be_clickable((By.XPATH, '//a[text()="{}"]'.format(menu_name))))
    hover = ActionChains(driver).move_to_element(menu_to_hover)
    hover.perform()
    recovery = wait.until(EC.element_to_be_clickable((By.XPATH, '//a[text()="{}"]'.format(list_name))))
    logging.info('Verified that {} is found in {}'.format(list_name, menu_name))
    recovery.click()


def go_to_next_page():
    """
    Clicks on next page button and waits for items to refresh
    :return: None
    """
    items = items_on_current_page()
    next_page_elem = wait.until(EC.element_to_be_clickable((By.XPATH, '//li[@title="Next Page"]')))
    next_page_elem.click()
    wait.until(EC.staleness_of(items[0]))


def items_on_current_page():
    """
    Gets all visible items on a page
    :return: List of webelements on current page
    """
    items_on_page = wait.until(EC.presence_of_all_elements_located((By.XPATH, '//div[@class="item-title"]/a')))
    return items_on_page


def search_for_item(item_name):
    """
    Searches through all pages in the list for item
    :param item_name: Str value for item to find in the list
    :return: Selenium webelement object if found otherwise None
    """
    wait.until(EC.visibility_of_element_located((By.CLASS_NAME, 'pager')))
    total_pages = len(driver.find_elements_by_xpath('//ul[@class="page-links"]/li'))
    while total_pages > 0:
        items = items_on_current_page()
        for item in items:
            if item_name == item.text:
                logging.info("Verified that the {} is present in the list".format(item_name))
                return item
        go_to_next_page()
        total_pages -= 1
    logging.info("{} is not found".format(item_name))
    return None
