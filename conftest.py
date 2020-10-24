from pytest import fixture
import json

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from tests.config import Config


def load_test_data(path):
    with open(path) as data_file:
        data = json.load(data_file)
        return data


@fixture(params=load_test_data('tests/test_data.json'))
def test_data(request):
    data = request.param
    return data


@fixture(scope='function')
def chrome_browser():
    options = Options()
    options.headless = True
    browser = webdriver.Chrome(options=options)
    yield browser


@fixture(params=[webdriver.Chrome, webdriver.Firefox])
def browser(request):
    driver = request.param
    drv = driver()
    yield drv
    drv.quit()


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
