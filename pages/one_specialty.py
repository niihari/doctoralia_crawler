from typing import Generator

from bs4 import BeautifulSoup, Tag

from pages.base.page_factory import register
from pages.base.page_object import PageObject
from selenium_utils.driver_wrapper import DriverWrapper


class OneSpecialty(PageObject):

    base_url: str = 'https://www.doctoralia.com.br/{Specialty}'

    def __init__(self, driver: DriverWrapper):
        super(OneSpecialty, self).__init__(self.base_url, driver)
        self.parsed_page: BeautifulSoup = BeautifulSoup(driver.get_page_source(), 'html.parser')

    def get_all_doctors_links(self) -> Generator[str, None, None]:
        '''WARNING: this method may change the page'''
        doctors_set = self.get_doctors_links_in_page()

        for link in doctors_set:
            yield link

        while self.go_to_next_page():
            doctors_set: Generator[str, None, None] = self.get_doctors_links_in_page()
            link: str
            for link in doctors_set:
                yield link

    def get_doctors_links_in_page(self) -> Generator[str, None, None]:
        link: Tag
        for link in self.parsed_page.find_all(attrs={'class': "rank-element-name__link"}):
            yield link['href']

    def go_to_next_page(self) -> bool:
        next_page_parent: Tag = self.parsed_page.find(attrs={'class': "next"})

        if next_page_parent:
            next_page = next_page_parent.find('a', href=True)['href']
            self.driver.get(next_page)
            self.parsed_page = BeautifulSoup(self.driver.get_page_source(), 'html.parser')
            return True
        else:
            return False

    @staticmethod
    def is_it_mine(driver: DriverWrapper, url: str) -> bool:
        return 'recomendados - Leia opiniões' in driver.get_title()


register(OneSpecialty)
