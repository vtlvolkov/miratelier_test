from selenium.webdriver.common.by import By

from pages.base_element import BaseElement
from pages.base_page import BasePage
from pages.locator import Locator


class AboutPage(BasePage):

    url = 'https://www.miratelier.com/about.html'

    @property
    def logo_section(self):
        locator = (By.ID, 'logo-section')
        return BaseElement(
            driver=self.driver,
            locator=locator
        )

    def verify_dashboard_page_is_open(self):
        assert self.logo_section.text == 'Dashboard'
