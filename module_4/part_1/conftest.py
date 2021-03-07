import pytest
from selenium import webdriver


def pytest_addoption(parser):
    parser.addoption('--language', action='store', default=None,
                     help="Choose language: 'ru' or 'en-GB' or 'es' or 'fr'")


@pytest.fixture(scope="function")
def browser():
    browser = webdriver.Chrome()
    yield browser
    browser.quit()


@pytest.fixture()
def language(request):
    return request.config.getoption("language")
