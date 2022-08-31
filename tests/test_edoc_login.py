import pytest
from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
import time
from selenium.webdriver.common.keys import Keys


# Loans to use: 1006510, 1003636

@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get('https://edoc.admortgage.us/loan/1006510')  # Any URL applicable
    yield driver
    driver.close()


def wait_of_element_located(xpath, driver):
    element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located(
            (By.XPATH, xpath)
        )
    )
    return element


def test_login_positive(driver):
    input_username = wait_of_element_located(xpath='//*[@id=":r0:"]', driver=driver)
    input_password = wait_of_element_located(xpath='//*[@id=":r1:"]', driver=driver)
    login_button = wait_of_element_located(xpath='//*[@id=":r2:"]', driver=driver)

    input_username.send_keys('testUser')
    input_password.send_keys('Pass')
    login_button.click()

    edoc_title = wait_of_element_located(xpath='//*[@id="root"]/header/div/div[1]/div/p', driver=driver)

    assert edoc_title.text == 'eDoc'


def test_login_negative_wrong(driver):
    input_username = wait_of_element_located(xpath='//*[@id=":r0:"]', driver=driver)
    input_password = wait_of_element_located(xpath='//*[@id=":r1:"]', driver=driver)
    login_button = wait_of_element_located(xpath='//*[@id=":r2:"]', driver=driver)

    input_username.send_keys('000')
    input_password.send_keys('000')
    login_button.click()

    error_login = wait_of_element_located(xpath='//*[@id="root"]/div/div/div[2]/p', driver=driver)

    assert error_login.text == 'User name or password is wrong'


def test_login_negative_empty_username(driver):
    input_username = wait_of_element_located(xpath='//*[@id=":r0:"]', driver=driver)
    input_password = wait_of_element_located(xpath='//*[@id=":r1:"]', driver=driver)
    login_button = wait_of_element_located(xpath='//*[@id=":r2:"]', driver=driver)

    input_username.send_keys('')
    input_password.send_keys('Pass')
    login_button.click()

    username_required = wait_of_element_located(xpath='//*[@id=":r0:-helper-text"]', driver=driver)

    assert username_required.text == 'User name is required'


def test_login_negative_empty_pass(driver):
    input_username = wait_of_element_located(xpath='//*[@id=":r0:"]', driver=driver)
    input_password = wait_of_element_located(xpath='//*[@id=":r1:"]', driver=driver)
    login_button = wait_of_element_located(xpath='//*[@id=":r2:"]', driver=driver)

    input_username.send_keys('testUser')
    input_password.send_keys('')
    login_button.click()

    password_required = wait_of_element_located(xpath='//*[@id=":r1:-helper-text"]', driver=driver)

    assert password_required.text == 'Password is required'


def test_login_negative_empty_both(driver):
    input_username = wait_of_element_located(xpath='//*[@id=":r0:"]', driver=driver)
    input_password = wait_of_element_located(xpath='//*[@id=":r1:"]', driver=driver)
    login_button = wait_of_element_located(xpath='//*[@id=":r2:"]', driver=driver)

    input_username.send_keys('')
    input_password.send_keys('')
    login_button.click()

    username_required = wait_of_element_located(xpath='//*[@id=":r0:-helper-text"]', driver=driver)
    password_required = wait_of_element_located(xpath='//*[@id=":r1:-helper-text"]', driver=driver)

    assert username_required.text == 'User name is required'
    assert password_required.text == 'Password is required'


def test_login_positive_space_after_username(driver):
    input_username = wait_of_element_located(xpath='//*[@id=":r0:"]', driver=driver)
    input_password = wait_of_element_located(xpath='//*[@id=":r1:"]', driver=driver)
    login_button = wait_of_element_located(xpath='//*[@id=":r2:"]', driver=driver)

    input_username.send_keys('testUser ')
    input_password.send_keys('Pass')
    login_button.click()

    edoc_title = wait_of_element_located(xpath='//*[@id="root"]/header/div/div[1]/div/p', driver=driver)

    assert edoc_title.text == 'eDoc'


def test_login_negative_space_after_password(driver):
    input_username = wait_of_element_located(xpath='//*[@id=":r0:"]', driver=driver)
    input_password = wait_of_element_located(xpath='//*[@id=":r1:"]', driver=driver)
    login_button = wait_of_element_located(xpath='//*[@id=":r2:"]', driver=driver)

    input_username.send_keys('testUser')
    input_password.send_keys('Pass ')
    login_button.click()

    error_login = wait_of_element_located(xpath='//*[@id="root"]/div/div/div[2]/p', driver=driver)

    assert error_login.text == 'User name or password is wrong'
