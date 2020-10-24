from pytest import fixture

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from config import Config


@fixture(scope='function')
def chrome_browser():
    options = Options()
    options.headless = True
    browser = webdriver.Chrome(options=options)
    yield browser


def pytest_addoption(parser):
    parser.addoption(
        "--env",
        action='store',
        default='dev',
        help='Environment to run tests.'
    )


@fixture(scope='session')
def env(request):
    return request.config.getoption('--env')


@fixture(scope='session')
def app_config(env):
    cfg = Config(env)
    return cfg


@fixture(scope='session')
def base_url(env):
    cfg = Config(env)
    return cfg.base_url
