from abc import ABC, abstractmethod

from selenium_utils.driver_wrapper import DriverWrapper


class PageObject(ABC):

    @property
    def url(self):
        return self._url

    def __init__(self, url: str, driver: DriverWrapper):
        self._url: str = url
        self.driver: DriverWrapper = driver
        super(PageObject, self).__init__()

    def register(self):
        pass

    @staticmethod
    @abstractmethod
    def is_it_mine(driver: DriverWrapper, url: str) -> bool:
        pass
