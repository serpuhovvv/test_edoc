# Create requirements: pip freeze > requirements.txt
# Install requirements: pip install -r requirements.txt

# Delete from git cache: git rm --cached "file_path"

# Launch: pytest --alluredir reports -n 3
# Report:  allure serve reports

import pytest
from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

produrl = 'https://edoc.admortgage.com/login'
testurl = 'https://edoc.admortgage.us/login'
preprodurl = 'https://edoc.preprod.admortgage.net/login'

prodloan = 'https://edoc.admortgage.com/loan/1003636'
testloan = 'https://edoc.admortgage.us/loan/1006508'
preprodloan = 'https://edoc.preprod.admortgage.net/loan/1027992'


@pytest.fixture
def driver_init():
    global driver
    driver = webdriver.Chrome()
    driver.maximize_window()


@pytest.fixture
def driver_login(driver_init):
    driver.get(produrl)

    yield driver
    driver.close()


@pytest.fixture
def driver_tests(driver_init):
    driver.get(prodloan)

    input_username = wait_xpath(xpath='//*[@id=":r0:"]')
    input_password = wait_xpath(xpath='//*[@id=":r1:"]')
    login_button = wait_xpath(xpath='//*[@id=":r2:"]')

    input_username.send_keys('testUser')  # Any username applicable
    input_password.send_keys('Pass')  # Any password applicable
    login_button.click()

    yield driver
    driver.close()


def wait_xpath(xpath):
    element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located(
            (By.XPATH, xpath)
        )
    )
    return element


def wait_id(id):
    element = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable(
            (By.ID, id)
        )
    )
    return element
