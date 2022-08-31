import pytest
from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys
import time


# Loans to use: 1006510, 1003636

@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get('https://edoc.admortgage.us/loan/1006510')  # Any URL applicable
    input_username = wait_of_element_located(xpath='//*[@id=":r0:"]', driver=driver)
    input_password = wait_of_element_located(xpath='//*[@id=":r1:"]', driver=driver)
    login_button = wait_of_element_located(xpath='//*[@id=":r2:"]', driver=driver)

    input_username.send_keys('testUser')  # Any username applicable
    input_password.send_keys('Pass')  # Any password applicable
    login_button.click()
    yield driver
    driver.close()


def wait_of_element_located(xpath, driver):
    element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located(
            (By.XPATH, xpath)
        )
    )
    return element


def test_searchbar_positive(driver):
    searchbar = wait_of_element_located(xpath='//*[@id="input-with-icon-textfield"]', driver=driver)
    searchbar.click()
    searchbar.send_keys('closing')  # Any CORRECT value applicable
    result = wait_of_element_located(
        xpath='/html/body/div[1]/main/div[2]/div[1]/div/div[3]/ul/div/div[2]/div/div/div/div/div', driver=driver)
    result.click()

    try:
        wait_of_element_located(
            xpath='//*[@id="root"]/main/div[2]/div[2]/div/div/div/div[1]/div/div[2]/div[2]/div/div[1]/div/div[2]',
            driver=driver)
    except NoSuchElementException:
        assert False
    assert True


def test_download(driver):
    download_btn = wait_of_element_located(xpath='//*[@id="root"]/main/div[2]/div[1]/div/div[2]/div[2]/button[1]',
                                           driver=driver)
    download_btn.click()

    try:
        wait_of_element_located(xpath='/html/body/div[3]/div[3]/div', driver=driver)
    except NoSuchElementException:
        assert False
    assert True


def test_feed(driver):
    feed = wait_of_element_located(xpath='//*[@id="root"]/main/div[2]/div[3]/div/div/div[1]/div', driver=driver)
    feed.click()

    try:
        wait_of_element_located(xpath='//*[@id="root"]/main/div[2]/div[3]/div/div/div[2]/div/div/div/div/ul',
                                driver=driver)
    except NoSuchElementException:
        assert False
    assert True


def test_main_properties(driver):
    searchbar = wait_of_element_located(xpath='//*[@id="input-with-icon-textfield"]', driver=driver)
    searchbar.click()
    searchbar.send_keys('closing')  # Any CORRECT value applicable
    result = wait_of_element_located(
        xpath='/html/body/div[1]/main/div[2]/div[1]/div/div[3]/ul/div/div[2]/div/div/div/div/div', driver=driver)
    result.click()
    main_prop = wait_of_element_located(xpath='//*[@id="root"]/main/div[2]/div[3]/div/div[2]/div[1]/div', driver=driver)
    main_prop.click()

    try:
        wait_of_element_located(xpath='//*[@id="root"]/main/div[2]/div[3]/div/div[2]/div[2]/div/div/div/div',
                                driver=driver)
    except NoSuchElementException:
        assert False
    assert True


def test_version_history(driver):
    searchbar = wait_of_element_located(xpath='//*[@id="input-with-icon-textfield"]', driver=driver)
    searchbar.click()
    searchbar.send_keys('closing')  # Any CORRECT value applicable
    result = wait_of_element_located(
        xpath='/html/body/div[1]/main/div[2]/div[1]/div/div[3]/ul/div/div[2]/div/div/div/div/div', driver=driver)
    result.click()
    vers_hist = wait_of_element_located(xpath='//*[@id="root"]/main/div[2]/div[3]/div/div[3]/div[1]/div', driver=driver)
    vers_hist.click()

    try:
        wait_of_element_located(
            xpath='//*[@id="root"]/main/div[2]/div[3]/div/div[3]/div[2]/div/div/div/div/div/div/div/div[1]',
            driver=driver)
    except NoSuchElementException:
        assert False
    assert True



