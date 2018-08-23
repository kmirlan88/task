from utilities import go_to_home_page, logging, end_test
from landing_page import from_menu_get_to_list, search_for_item
from item_details_page import increase_item_quantity


go_to_home_page()
from_menu_get_to_list("Supply", "Recovery")
found = search_for_item('Revival Stone')

if found:
    found.click()
    increase_item_quantity(11)
    logging.info("PASS")
else:
    logging.info("FAIL")

end_test()
