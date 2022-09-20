import pytest
from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait


# Loans to use: 1006510, 1003636, 1006508
# Launch: pytest --alluredir reports -n 3
# Report:  allure serve reports

# delete from git cache: git rm --cached "file_path"

@pytest.fixture
def driver_login():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get('https://edoc.admortgage.us/login')  # Any URL applicable
    yield driver
    driver.close()


@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get('https://edoc.admortgage.us/loan/1006508')  # Any URL applicable
    input_username = wait_xpath(xpath='//*[@id=":r0:"]', driver=driver)
    input_password = wait_xpath(xpath='//*[@id=":r1:"]', driver=driver)
    login_button = wait_xpath(xpath='//*[@id=":r2:"]', driver=driver)

    input_username.send_keys('testUser')  # Any username applicable
    input_password.send_keys('Pass')  # Any password applicable
    login_button.click()
    yield driver
    driver.close()


def wait_xpath(xpath, driver):
    element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located(
            (By.XPATH, xpath)
        )
    )
    return element


def wait_id(id, driver):
    element = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable(
            (By.ID, id)
        )
    )
    return element
