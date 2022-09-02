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


@pytest.fixture
def driver2():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get('https://edoc.admortgage.us/login')  # Any URL applicable
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


def test_change_description(driver2):
    wait_id(id=':r3:', driver=driver2).send_keys('1006508')
    wait_of_element_located(xpath='/html/body/div[3]/div[3]/div/a/div/p[1]', driver=driver2).click()
    wait_of_element_located(xpath='/html/body/div[1]/main/div[2]/div[3]/div/div/div[1]/div/div[1]/div/span',
                            driver=driver2).click()
    a = wait_of_element_located(
        xpath='//*[@id="root"]/main/div[2]/div[3]/div/div/div[2]/div/div/div/div/ul/div[1]/li/div[2]/p/a',
        driver=driver2)
    action = ActionChains(driver2)
    action.click_and_hold(a)
    action.release(a)
    action.perform()
    wait_of_element_located(xpath='/html/body/div[1]/main/div[2]/div[3]/div/div[1]/div[1]/div', driver=driver2).click()
    wait_of_element_located(xpath='/html/body/div[1]/main/div[2]/div[3]/div/div[2]/div[1]/div/div[1]/div/span',
                            driver=driver2).click()
    b = wait_id(id=':re:', driver=driver2)
    action.click(b)
    action.key_down(Keys.CONTROL)
    action.send_keys('A')
    action.key_up(Keys.CONTROL)
    action.send_keys('aaa111')
    action.perform()
    wait_of_element_located(xpath='//*[@id="root"]/header/div/div[1]/div', driver=driver2).click()
    time.sleep(10)
    c = wait_of_element_located(
        xpath='//*[@id=":r6:"]/div[2]/div[2]/div/div/div/div/div[1]/div/div/div[1]/div/div[2]/span',
        driver=driver2)
    assert c.text == 'aaa111'
