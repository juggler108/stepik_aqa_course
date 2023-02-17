from time import sleep
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


def pytest_addoption(parser):
    parser.addoption('--language', action='store', default="en", help="Choose the language!")


@pytest.fixture(scope="function")
def browser(request):
    user_language = request.config.getoption("language")

    options = Options()
    options.add_experimental_option('prefs', {'intl.accept_languages': user_language})

    print("\nstart chrome browser for test..")
    driver = webdriver.Chrome(options=options)

    yield driver

    print("\nquit browser..")
    driver.quit()


# @pytest.fixture(scope="function")
# def browser(request):
#     language = request.config.getoption("language")
#     link = f"http://selenium1py.pythonanywhere.com/{language}/catalogue/coders-at-work_207/"
#
#     print("\nstart chrome browser for test..")
#     driver = webdriver.Chrome()
#     driver.implicitly_wait(3)
#
#     driver.get(link)
#     sleep(10)
#     yield driver
#
#     print("\nquit browser..")
#     driver.quit()
