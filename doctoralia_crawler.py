from typing import Generator, List, Tuple, Iterable

import config
from data.doctor_data import DoctorData
from data.pandas_parser import PandasParser
from pages.base.page_factory import get_page
from pages.doctor import Doctor
from pages.one_specialty import OneSpecialty as OneSpecialtyPage
from pages.specialties import Specialties as SpecialtiesPage
from selenium_utils.driver_wrapper import DriverWrapper

base_url: str = 'https://www.doctoralia.com.br/medicos'
driver: DriverWrapper = DriverWrapper()
driver.get(base_url)

page: SpecialtiesPage = get_page(driver)

link_list: List[str] = page.get_link_to_all_specialties()


def get_doctors_links() -> Generator[str, None, None]:
    link: str
    for link in link_list:
        driver.get(link)
        page: OneSpecialtyPage = get_page(driver)
        doctor_link: str
        for doctor_link in page.get_all_doctors_links():
            yield doctor_link


def get_first_n_doctors(n: int) -> Tuple[List[str], Generator[str, None, None]]:
    get_generator: Generator[str, None, None] = get_doctors_links()
    doctors_links_list: List[str] = []
    i: int
    for i in range(n):
        if i + 1 % 100 == 0:
            print("Retrieving doctor %d link" % (i + 1,))
        doctors_links_list.append(next(get_generator))
    return doctors_links_list, get_generator


doctors_link_list: Iterable
if not config.args.all_results:
    generator: Generator[str, None, None]
    doctors_links_list, generator = get_first_n_doctors(config.args.n_results)
else:
    doctors_links_list = get_doctors_links()
excel_adapter: PandasParser = PandasParser()

count: int = 1
link: str
for link in doctors_links_list:
    driver.get(link)
    page: Doctor = get_page(driver)
    if count % 100 == 0:
        print("Processing doctor %d info" % (count,))
    doctor_data: DoctorData = page.get_doctors_info()
    excel_adapter.add_to_dataframe(doctor_data)
    count += 1

excel_adapter.write_to_excel_file()


driver.quit()
