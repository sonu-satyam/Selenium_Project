from selenium.webdriver.firefox.webdriver import WebDriver
from selenium import webdriver

from pytest import fixture

@fixture
def setup_tear_down():
    driver = WebDriver()
    driver.get("https://demowebshop.tricentis.com/")
    yield driver
    driver.close()