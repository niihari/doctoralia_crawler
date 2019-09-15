from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException, TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import config


class DriverWrapper:

    TIMEOUT = 10000

    def __init__(self):
        self.config = webdriver.ChromeOptions()
        self.config.add_argument('lang=pt-br')
        if not config.args.show_browser:
            self.config.add_argument("--headless")
        self.driver = webdriver.Chrome(config.args.chrome_driver_path,
                                       options = self.config)

    def click_by_class_name(self, by_class_name: str) -> None:
        self.wait_for_element_to_be_clickable(By.CLASS_NAME, by_class_name)
        return self.driver.find_element_by_class_name(by_class_name).click()

    def click_by_css_selector(self, by_css_selector: str) -> None:
        self.wait_for_element_to_be_clickable(By.CSS_SELECTOR, by_css_selector)
        return self.driver.find_element_by_css_selector(by_css_selector).click()

    def click_by_id(self, by_id: str) -> None:
        self.wait_for_element_to_be_clickable(By.ID, by_id)
        return self.driver.find_element_by_id(by_id).click()

    def click_by_name(self, by_name: str) -> None:
        self.wait_for_element_to_be_clickable(By.NAME, by_name)
        return self.driver.find_element_by_name(by_name).click()

    def click_by_tag_name(self, by_tag_name: str) -> None:
        self.wait_for_element_to_be_clickable(By.TAG_NAME, by_tag_name)
        return self.driver.find_element_by_tag_name(by_tag_name).click()

    def click_by_xpath(self, by_xpath: str) -> None:
        self.wait_for_element_to_be_clickable(By.XPATH, by_xpath)
        return self.driver.find_element_by_xpath(by_xpath).click()

    def find_by_class_name(self, by_class_name: str, element_must_exist: bool = True) -> WebElement:
        try:
            self.wait_for_element_to_be_clickable(By.CLASS_NAME, by_class_name)
            return self.driver.find_element_by_class_name(by_class_name)
        except (NoSuchElementException, TimeoutException) as e:
            if element_must_exist:
                raise e
            return None

    def find_by_css_selector(self, by_css_selector: str, element_must_exist: bool = True) -> None:
        try:
            self.wait_for_element_to_be_clickable(By.CSS_SELECTOR, by_css_selector)
            return self.driver.find_element_by_css_selector(by_css_selector)
        except (NoSuchElementException, TimeoutException) as e:
            if element_must_exist:
                raise e
            return None

    def find_by_id(self, by_id: str, element_must_exist: bool = True) -> None:
        try:
            self.wait_for_element_to_be_clickable(By.ID, by_id)
            return self.driver.find_element_by_id(by_id)
        except (NoSuchElementException, TimeoutException) as e:
            if element_must_exist:
                raise e
            return None

    def find_by_name(self, by_name: str, element_must_exist: bool = True) -> None:
        try:
            self.wait_for_element_to_be_clickable(By.NAME, by_name)
            return self.driver.find_element_by_name(by_name)
        except (NoSuchElementException, TimeoutException) as e:
            if element_must_exist:
                raise e
            return None

    def find_by_tag_name(self, by_tag_name: str, element_must_exist: bool = True) -> None:
        try:
            self.wait_for_element_to_be_clickable(By.TAG_NAME, by_tag_name)
            return self.driver.find_element_by_tag_name(by_tag_name)
        except (NoSuchElementException, TimeoutException) as e:
            if element_must_exist:
                raise e
            return None

    def find_by_xpath(self, by_xpath: str, element_must_exist: bool = True) -> None:
        try:
            self.wait_for_element_to_be_clickable(By.XPATH, by_xpath)
            return self.driver.find_element_by_xpath(by_xpath)
        except (NoSuchElementException, TimeoutException) as e:
            if element_must_exist:
                raise e
            return None

    def get(self, url: str) -> None:
        return self.driver.get(url)

    def get_current_url(self) -> str:
        return self.driver.current_url

    def get_page_source(self) -> str:
        return self.driver.page_source

    def get_title(self) -> str:
        return self.driver.title

    def maximize_window(self) -> None:
        return self.driver.maximize_window()

    def send_keys_by_class_name(self, by_class_name: str, value: str) -> None:
        self.wait_for_element_to_be_clickable(By.CLASS_NAME, by_class_name)
        return self.driver.find_element_by_class_name(by_class_name).send_keys(value)

    def send_keys_by_css_selector(self, by_css_selector: str, value: str) -> None:
        self.wait_for_element_to_be_clickable(By.CSS_SELECTOR, by_css_selector)
        return self.driver.find_element_by_css_selector(by_css_selector).send_keys(value)

    def send_keys_by_id(self, by_id: str, value: str) -> None:
        self.wait_for_element_to_be_clickable(By.ID, by_id)
        return self.driver.find_element_by_id(by_id).send_keys(value)

    def send_keys_by_name(self, by_name: str, value: str) -> None:
        self.wait_for_element_to_be_clickable(By.NAME, by_name)
        return self.driver.find_element_by_name(by_name).send_keys(value)

    def send_keys_by_tag_name(self, by_tag_name: str, value: str) -> None:
        self.wait_for_element_to_be_clickable(By.TAG_NAME, by_tag_name)
        return self.driver.find_element_by_tag_name(by_tag_name).send_keys(value)

    def send_keys_by_xpath(self, by_xpath: str, value: str) -> None:
        self.wait_for_element_to_be_clickable(By.XPATH, by_xpath)
        return self.driver.find_element_by_xpath(by_xpath).send_keys(value)

    def quit(self) -> None:
        return self.driver.quit()

    def wait_for_element_to_be_clickable(self, _type: str, _id: str):
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((_type, _id)))
