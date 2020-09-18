from selenium.webdriver.common.by import By

from pages.base_element import BaseElement
from pages.base_page import BasePage
from pages.locator import Locator


class HomePage(BasePage):

    url = 'https://www.miratelier.com/index.html'

    @property
    def current_menu_item(self):
        locator = Locator(By.XPATH, "//li[@class='current-menu-item']")
        return BaseElement(
            driver=self.driver,
            locator=locator
        )

    @property
    def main_link(self):
        locator = Locator(By.XPATH, "//a[text()='Главная']")
        return BaseElement(
            driver=self.driver,
            locator=locator
        )

    @property
    def about_us_link(self):
        locator = Locator(By.XPATH, "//a[text()='О нас']")
        return BaseElement(
            driver=self.driver,
            locator=locator
        )

    @property
    def works_link(self):
        locator = (By.XPATH,  "//a[text()='Работы']")
        return BaseElement(
            driver=self.driver,
            locator=locator
        )

    @property
    def size_link(self):
        locator = (By.XPATH, "//a[text()='Размеры']")
        return BaseElement(
            driver=self.driver,
            locator=locator
        )

    @property
    def size_thumb(self):
        locator = (By.XPATH, "//div[@class ='thumb']//a[contains(@href, 'size')]")
        return BaseElement(
            driver=self.driver,
            locator=locator
        )
    
    @property
    def contacts_link(self):
        locator = (By.XPATH, "//a[text()='Контакты']")
        return BaseElement(
            driver=self.driver,
            locator=locator
        )



