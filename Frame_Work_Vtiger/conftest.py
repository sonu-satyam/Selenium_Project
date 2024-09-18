from selenium.webdriver.chrome.webdriver import WebDriver as Chrome
from selenium.webdriver.firefox.webdriver import WebDriver as Firefox
from pytest import fixture

def pytest_addoption(parser):
    parser.addoption("--browser", action="store", dest="browser", default="firefox")
    parser.addoption("--env", action="store", dest="env", default="test")

class TestConfigurations():
    url = "http://49.249.28.218:8888/"
    username = "admin"
    password = "admin"

class StageConfigurations():
    url = "http://49.249.28.218:8888/"
    username = "admin"
    password = "admin"

@fixture
def _config(request):
    if request.config.option.env.upper() == "TEST":
        return TestConfigurations
    elif request.config.option.env.upper() == "STAGE":
        return StageConfigurations
    else:
        raise ValueError("Env not found")
@fixture
def _driver(_config, request):
    # browser_class = request.config.option.browser.upper()
    if request.config.option.browser.upper() == "CHROME":
        driver = Chrome()
    elif request.config.option.browser.upper() == "FIREFOX":
        driver = Firefox()
    else:
        raise Exception("browser not supported")
    driver.get(_config.url)
    yield driver
    driver.close()





