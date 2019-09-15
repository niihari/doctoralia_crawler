from selenium_utils.driver_wrapper import DriverWrapper

page_class_list = []


def register(klass):
    page_class_list.append(klass)


def get_page(driver: DriverWrapper):
    for klass in page_class_list:
        if klass.is_it_mine(driver, driver.get_current_url()):
            return klass(driver)
