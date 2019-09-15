from typing import List, Set

from bs4 import BeautifulSoup, Tag, ResultSet

from data.doctor_data import DoctorData, Address
from pages.base.page_factory import register
from pages.base.page_object import PageObject
from selenium_utils.driver_wrapper import DriverWrapper


class Doctor(PageObject):

    base_url: str = 'https://www.doctoralia.com.br/{Doctor}/{Specialty}/{City}{#address}'

    @staticmethod
    def is_it_mine(driver: DriverWrapper, url: str) -> bool:
        return '- Agende uma consulta' in driver.get_title() or driver.get_title().endswith(" - Doctoralia")

    def __init__(self, driver: DriverWrapper):
        super(Doctor, self).__init__(self.base_url, driver)
        self.parsed_page: BeautifulSoup = BeautifulSoup(driver.get_page_source(), 'html.parser')
        self.doctor_data: DoctorData = DoctorData()

    def get_doctors_info(self) -> DoctorData:
        self.doctor_data.nome = self.extract_name()
        self.doctor_data.especialidades = self.extract_specialties()
        self.doctor_data.competencias = self.extract_competencias()
        self.doctor_data.enderecos = self.extract_addresses()
        return self.doctor_data

    def extract_name(self) -> List[str]:
        name: Tag = self.parsed_page.find(attrs={'class': "unified-doctor-header-info__name"})
        return name.text.replace('\n', ' ').strip()

    def extract_specialties(self) -> List[str]:
        profile_panel_tag: Tag = self.parsed_page.find(attrs={"class": "unified-doctor-header-info__content"})
        return [i.strip() for i in profile_panel_tag.find("h2").text.split(",")]

    def extract_competencias_strategy_lots_of_competencies(self) -> List[str]:
        parent: Tag = self.parsed_page.find(attrs={"id": "data-type-expert_in"})
        if not parent:
            return None

        competencies_tag: Tag = parent.find("ul")
        if not competencies_tag:
            return None

        return [competencies.text.strip() for competencies in competencies_tag.find_all('li')]

    def extract_competencias_strategy_few_competencies(self) -> List[str]:
        profile_info_tag: Tag = self.parsed_page.find(attrs={"id": "profile-info"})
        experience_items: ResultSet[Tag] = profile_info_tag.find_all(attrs={"data-id": "doctor-experience-item"})

        competencies_tag: Tag = self.find_experience_item_experiencia_em(experience_items)

        if not competencies_tag:
            return None

        return [competencies.text.strip() for competencies in competencies_tag.find_all('li')]

    def find_experience_item_experiencia_em(self, experience_items: List[Tag]) -> Tag:
        experience_item: Tag
        for experience_item in experience_items:
            span: Tag = experience_item.find("span")
            if span and "Experiência em:" in span.text:
                return experience_item

    def extract_competencias(self) -> List[str]:
        competencias_list: List[str] = self.extract_competencias_strategy_lots_of_competencies()

        if competencias_list:
            return competencias_list

        competencias_list = self.extract_competencias_strategy_few_competencies()

        if competencias_list:
            return competencias_list

        return ['']

    def extract_telefones(self):
        pass

    def extract_addresses(self) -> Set[Address]:
        address_set: Set[Address] = set()
        address_tags: ResultSet = self.parsed_page.find(attrs={"id": "profile-info"}).find_all(attrs={"itemprop": "address"})

        address_tag: Tag
        for address_tag in address_tags:
            address = Address()
            element: Tag = address_tag.find(attrs={'class': "city"})
            if element:
                address.city = element['content']
            element: Tag = address_tag.find(attrs={'class': "province region"})
            if element:
                address.state = element['content']
            address_set.add(address)

        return address_set


register(Doctor)
