import pytest
from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import ElementNotInteractableException
import time


# Loans to use: 1006510, 1003636

@pytest.fixture
def driver():
    driver = webdriver.Chrome(executable_path='/Users/serpuhovvv/Python Dev/QA/venv/chromedriver')
    driver.maximize_window()
    driver.get('https://edoc.admortgage.us/loan/1003636')  # Any URL applicable
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
    searchbar = wait_of_element_located(xpath='//*[@id=":r5:"]', driver=driver)
    old_url = driver.current_url
    searchbar.click()
    searchbar.send_keys('1006510')  # Any CORRECT value applicable
    result = wait_of_element_located(xpath='//*[@id="popover"]/div[3]/div/a/div', driver=driver)
    action = ActionChains(driver)
    action.click_and_hold(result)
    action.release(result)
    action.perform()
    new_url = driver.current_url

    assert old_url != new_url


def test_searchbar_negative(driver):
    searchbar = wait_of_element_located(xpath='//*[@id=":r5:"]', driver=driver)
    searchbar.click()
    searchbar.send_keys('09vfdjv89er')  # Any INCORRECT value applicable
    result = wait_of_element_located(xpath='//*[@id="popover"]/div[3]/div/p', driver=driver)

    assert result.text == 'There are no results for this query'


def test_user_icon(driver):
    icon = wait_of_element_located(xpath='//*[@id="root"]/header/div/div[3]/div/div/div', driver=driver)
    icon.click()

    try:
        wait_of_element_located(xpath='//*[@id="simple-popover"]/div[3]/div', driver=driver)
    except NoSuchElementException:
        assert False
    assert True


def test_user_icon_content(driver):
    icon = wait_of_element_located(xpath='//*[@id="root"]/header/div/div[3]/div/div/div', driver=driver)
    icon.click()
    icon_open = wait_of_element_located(xpath='//*[@id="simple-popover"]/div[3]/div', driver=driver)

    assert 'ADMIN PANEL', 'LOG OUT' in icon_open.text


def test_user_icon_adminpanel(driver):
    icon = wait_of_element_located(xpath='//*[@id="root"]/header/div/div[3]/div/div/div', driver=driver)
    icon.click()
    adminpanel = wait_of_element_located(xpath='//*[@id="simple-popover"]/div[3]/div/button[1]', driver=driver)
    adminpanel.click()
    new_url = driver.current_url

    assert new_url == 'https://edoc.admortgage.us/admin'


def test_user_icon_logout(driver):
    icon = wait_of_element_located(xpath='//*[@id="root"]/header/div/div[3]/div/div/div', driver=driver)
    icon.click()
    logout = wait_of_element_located(xpath='//*[@id="simple-popover"]/div[3]/div/button[2]', driver=driver)
    logout.click()
    wait_of_element_located(xpath='//*[@id=":r2:"]', driver=driver)
    new_url = driver.current_url

    assert new_url == 'https://edoc.admortgage.us/login'


def test_loan_number(driver):
    a = wait_of_element_located(xpath='//*[@id="root"]/main/div[1]/div/span[1]', driver=driver)
    b = wait_of_element_located(xpath='//*[@id=":r5:"]', driver=driver)
    action = ActionChains(driver)
    action.click(a)
    action.click_and_hold(b)
    action.release(b)
    action.key_down(Keys.CONTROL)
    action.send_keys('V')
    action.key_up(Keys.CONTROL)
    action.perform()
    c = wait_of_element_located(xpath='//*[@id="popover"]/div[3]/div/a/div', driver=driver)

    assert a.text in c.text
