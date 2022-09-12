import pytest
from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys
import time


# Loans to use: 1006510, 1003636, 1006508

@pytest.fixture
def driver():
    driver = webdriver.Chrome(executable_path='/Users/serpuhovvv/Python Dev/QA/venv/chromedriver')
    driver.maximize_window()
    driver.get('https://edoc.admortgage.us/loan/1006508')  # Any URL applicable
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


def wait_id(id, driver):
    element = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable(
            (By.ID, id)
        )
    )
    return element


def test_searchbar_positive(driver):
    searchbar = wait_of_element_located(xpath='//*[@id="input-with-icon-textfield"]', driver=driver)
    searchbar.click()
    searchbar.send_keys('tran')  # Any CORRECT value applicable
    time.sleep(5)
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
    try:
        wait_of_element_located(xpath='/html/body/div[1]/main/div[2]/div[3]/div/div/div[2]', driver=driver)
    except NoSuchElementException:
        assert False
    assert True


def test_properties(driver):
    searchbar = wait_of_element_located(xpath='//*[@id="input-with-icon-textfield"]', driver=driver)
    searchbar.click()
    searchbar.send_keys('tran')  # Any CORRECT value applicable
    result = wait_of_element_located(
        xpath='/html/body/div[1]/main/div[2]/div[1]/div/div[3]/ul/div/div[2]/div/div/div/div/div', driver=driver)
    result.click()
    properties = wait_of_element_located(
        xpath='/html/body/div[1]/main/div[2]/div[3]/div/div/div[1]/div/div/div/button[2]', driver=driver)
    properties.click()

    try:
        wait_of_element_located(
            xpath='/html/body/div[1]/main/div[2]/div[3]/div/div/div[3]/div[1]/div[2]/div/div/div/div',
            driver=driver)
    except NoSuchElementException:
        assert False
    assert True


def test_version_history(driver):
    searchbar = wait_of_element_located(xpath='//*[@id="input-with-icon-textfield"]', driver=driver)
    searchbar.click()
    searchbar.send_keys('tran')  # Any CORRECT value applicable
    result = wait_of_element_located(
        xpath='/html/body/div[1]/main/div[2]/div[1]/div/div[3]/ul/div/div[2]/div/div/div/div/div', driver=driver)
    result.click()
    vers_hist = wait_of_element_located(
        xpath='/html/body/div[1]/main/div[2]/div[3]/div/div/div[1]/div/div/div/button[3]', driver=driver)
    vers_hist.click()

    try:
        wait_of_element_located(
            xpath='/html/body/div[1]/main/div[2]/div[3]/div/div/div[4]',
            driver=driver)
    except NoSuchElementException:
        assert False
    assert True


def test_change_description(driver):
    wait_of_element_located(xpath='/html/body/div[1]/main/div[2]/div[3]/div/div/div[2]/div/ul/div[1]/li/div[2]/p/a',
                            driver=driver).click()
    wait_of_element_located(xpath='/html/body/div[1]/main/div[2]/div[3]/div/div/div[1]/div/div/div/button[2]',
                            driver=driver).click()
    wait_of_element_located(xpath='/html/body/div[1]/main/div[2]/div[3]/div/div/div[3]/div[1]/div[1]/div/div[1]',
                            driver=driver).click()
    desc = wait_of_element_located(
        xpath='/html/body/div[1]/main/div[2]/div[3]/div/div/div[3]/div[1]/div[2]/div/div/div/div/div[6]/div/div/textarea[1]',
        driver=driver)
    time.sleep(5)
    action = ActionChains(driver)
    action.click(desc)
    action.key_down(Keys.CONTROL)
    action.send_keys('A')
    action.key_up(Keys.CONTROL)
    action.send_keys('aaa111')
    action.perform()
    wait_of_element_located(xpath='//*[@id="root"]/header/div/div[1]/div', driver=driver).click()
    time.sleep(5)
    desc2 = wait_of_element_located(
        xpath='/html/body/div[1]/main/div[2]/div[1]/div/div[3]/ul/div[2]/div[2]/div/div/div/div/div[1]/div/div/div[1]/div/div[2]/span',
        driver=driver)
    assert desc2.text == 'aaa111'
