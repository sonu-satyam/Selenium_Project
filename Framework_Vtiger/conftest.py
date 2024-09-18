from pytest import fixture
from selenium.webdriver.firefox.webdriver import WebDriver
from selenium.webdriver.chrome.webdriver import WebDriver as Chrome
from selenium.webdriver.firefox.webdriver import WebDriver as FireFox
from selenium.webdriver.safari.webdriver import WebDriver as Safari
from selenium.webdriver.edge.webdriver import WebDriver as Edge


@fixture
def tear_bear_down():
    driver = WebDriver()
    driver.get("http://49.249.28.218:8888/index.php?action=Login&module=Users")
    yield driver
    driver.close()

# def