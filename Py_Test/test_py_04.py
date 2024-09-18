import pytest
from selenium import webdriver
# @pytest.fixture
# def _driver():
#     driver = webdriver.Firefox()
#     driver.get("http://49.249.28.218:8888/")
#     yield driver
#     driver.close()
#
#
# def test_login(_driver):
#     driver = _driver
#     driver.find_element("name", "user_name").send_keys("admin")
#     driver.find_element("name", "user_password").send_keys("admin")
#     driver.find_element("id", "submitButton").click()

#####################################################################
@pytest.fixture()
def setup_teardown():
    print("start")
    yield
    print("end")
class Test1():

    def test_greet(self):
        print("good morning")

    def test_add(self):
        print(10 + 20)

    def test_mul(self):
        print(10 * 2)


class Test2():

    def test_bank(self):
        print("SBI")

    def test_language(self):
        print("python")


#######################################################
# @pytest.fixture
# def display():
#     print("start")
#     yield
#     print("end")
#
# def test_even(display):
#     num = 10
#     assert num % 2 == 0,f"{num} is not even"
#     print("in even")

#####################################################



