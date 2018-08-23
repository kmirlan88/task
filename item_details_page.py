from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from utilities import wait
import logging


def increase_item_quantity(num):
    """
    Puts specified amount of items to the quantity field
    :param num: Int value for item quantity
    :return: None
    Note: if num is more than 10, func checks for error message to be present
    """
    quantity = wait.until(EC.element_to_be_clickable((By.CLASS_NAME, 'qty-amount')))
    quantity.clear()
    quantity.send_keys(num)
    print(quantity.get_attribute('value'))
    if num > 10:
        purchase = wait.until(EC.element_to_be_clickable((By.XPATH, '//div[@class="ct"]')))
        purchase.click()

        popup = wait.until(EC.visibility_of_element_located((By.XPATH, '//div[@class="msg-content error"]')))
        if popup.text == "This item's maximum purchase quantity per transaction is 10":
            logging.info("Verified that the user can't increase the item quantity beyond the maximum")
