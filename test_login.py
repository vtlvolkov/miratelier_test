from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import pytest

from pages.home_page import HomePage
from pages.about_page import AboutPage


def test_main_page():
    options = Options()
    options.headless = True
    browser = webdriver.Chrome(options=options)
    home_page = HomePage(driver=browser)
    home_page.go()
    assert home_page.current_menu_item.text == 'ГЛАВНАЯ'


def test_main_to_about_page():
    options = Options()
    options.headless = True
    browser = webdriver.Chrome(options=options)
    home_page = HomePage(driver=browser)
    home_page.go()
    home_page.about_us_link.click()
    assert home_page.current_menu_item.text == 'О НАС'


def test_main_to_works_page():
    options = Options()
    options.headless = True
    browser = webdriver.Chrome(options=options)
    home_page = HomePage(driver=browser)
    home_page.go()
    home_page.works_link.click()
    assert home_page.current_menu_item.text == 'РАБОТЫ'


def test_main_to_size_page():
    options = Options()
    options.headless = True
    browser = webdriver.Chrome(options=options)
    home_page = HomePage(driver=browser)
    home_page.go()
    home_page.size_link.click()
    assert home_page.current_menu_item.text == 'РАЗМЕРЫ'


def test_main_to_thumb_size_page():
    options = Options()
    options.headless = True
    browser = webdriver.Chrome(options=options)
    home_page = HomePage(driver=browser)
    home_page.go()
    home_page.size_thumb.click()
    assert home_page.current_menu_item.text == 'РАЗМЕРЫ'


def test_main_to_contacts_page():
    options = Options()
    options.headless = True
    browser = webdriver.Chrome(options=options)
    home_page = HomePage(driver=browser)
    home_page.go()
    home_page.contacts_link.click()
    assert home_page.current_menu_item.text == 'КОНТАКТЫ'
