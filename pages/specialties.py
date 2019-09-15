from typing import List
from urllib.parse import urljoin

from bs4 import BeautifulSoup, ResultSet, Tag

from pages.base.page_factory import register
from pages.base.page_object import PageObject
from selenium_utils.driver_wrapper import DriverWrapper


class Specialties(PageObject):

    base_url: str = 'https://www.doctoralia.com.br/especializacoes-medicas'

    def __init__(self, driver: DriverWrapper):
        super(Specialties, self).__init__(self.base_url, driver)
        self.parsed_page: BeautifulSoup = BeautifulSoup(driver.get_page_source(), 'html.parser')

    def build_url(self, base_url: str, relative_path: str) -> str:
        return urljoin(base_url, relative_path)

    def get_all_specialties(self) -> ResultSet:
        return self.parsed_page.find_all(attrs={'class': "panel-title"})

    def get_link_to_all_specialties(self) -> List[str]:
        link_list: List[str] = []

        link: Tag
        for link in self.get_all_specialties():
            link_list.append(self.build_url(self.driver.get_current_url(), self.get_relative_path(link)))
        return link_list

    def get_relative_path(self, parent: Tag) -> str:
        return parent.find(attrs={'class': "text-muted"}, href=True)['href']

    # Override
    @staticmethod
    def is_it_mine(driver: DriverWrapper, url: str):
        return Specialties.base_url == url


register(Specialties)
