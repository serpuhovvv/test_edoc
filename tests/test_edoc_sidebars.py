import time
import allure
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys
from conftest import wait_xpath


@allure.feature('TestsSidebars')
@allure.story('Positive searchbar test')
def test_searchbar_positive(driver):
    searchbar = wait_xpath(xpath='//*[@id="input-with-icon-textfield"]', driver=driver)
    searchbar.click()
    searchbar.send_keys('tran')  # Any CORRECT value applicable
    time.sleep(5)
    result = wait_xpath(
        xpath='/html/body/div[1]/main/div[2]/div[1]/div/div[3]/ul/div/div[2]/div/div/div/div/div', driver=driver)
    result.click()

    try:
        wait_xpath(
            xpath='//*[@id="root"]/main/div[2]/div[2]/div/div/div/div[1]/div/div[2]/div[2]/div/div[1]/div/div[2]',
            driver=driver)
    except NoSuchElementException:
        assert False
    assert True


@allure.feature('TestsSidebars')
@allure.story('Download button test')
def test_download(driver):
    download_btn = wait_xpath(xpath='//*[@id="root"]/main/div[2]/div[1]/div/div[2]/div[2]/button[1]',
                              driver=driver)
    download_btn.click()

    try:
        wait_xpath(xpath='/html/body/div[3]/div[3]/div', driver=driver)
    except NoSuchElementException:
        assert False
    assert True


@allure.feature('TestsSidebars')
@allure.story('Feed menu test')
def test_feed(driver):
    try:
        wait_xpath(xpath='/html/body/div[1]/main/div[2]/div[3]/div/div/div[2]', driver=driver)
    except NoSuchElementException:
        assert False
    assert True


@allure.feature('TestsSidebars')
@allure.story('Properties menu test')
def test_properties(driver):
    searchbar = wait_xpath(xpath='//*[@id="input-with-icon-textfield"]', driver=driver)
    searchbar.click()
    searchbar.send_keys('tran')  # Any CORRECT value applicable
    result = wait_xpath(
        xpath='/html/body/div[1]/main/div[2]/div[1]/div/div[3]/ul/div/div[2]/div/div/div/div/div', driver=driver)
    result.click()
    properties = wait_xpath(
        xpath='/html/body/div[1]/main/div[2]/div[3]/div/div/div[1]/div/div/div/button[2]', driver=driver)
    properties.click()

    try:
        wait_xpath(
            xpath='/html/body/div[1]/main/div[2]/div[3]/div/div/div[3]/div[1]/div[2]/div/div/div/div',
            driver=driver)
    except NoSuchElementException:
        assert False
    assert True


@allure.feature('TestsSidebars')
@allure.story('Version history menu test')
def test_version_history(driver):
    searchbar = wait_xpath(xpath='//*[@id="input-with-icon-textfield"]', driver=driver)
    searchbar.click()
    searchbar.send_keys('tran')  # Any CORRECT value applicable
    result = wait_xpath(
        xpath='/html/body/div[1]/main/div[2]/div[1]/div/div[3]/ul/div/div[2]/div/div/div/div/div', driver=driver)
    result.click()
    vers_hist = wait_xpath(
        xpath='/html/body/div[1]/main/div[2]/div[3]/div/div/div[1]/div/div/div/button[3]', driver=driver)
    vers_hist.click()

    try:
        wait_xpath(
            xpath='/html/body/div[1]/main/div[2]/div[3]/div/div/div[4]',
            driver=driver)
    except NoSuchElementException:
        assert False
    assert True


@allure.feature('TestsSidebars')
@allure.story('Description change on the left sidebar after changing it on the right one test')
def test_change_description(driver):
    wait_xpath(xpath='/html/body/div[1]/main/div[2]/div[3]/div/div/div[2]/div/ul/div[1]/li/div[2]/p/a',
               driver=driver).click()
    wait_xpath(xpath='/html/body/div[1]/main/div[2]/div[3]/div/div/div[1]/div/div/div/button[2]',
               driver=driver).click()
    wait_xpath(xpath='/html/body/div[1]/main/div[2]/div[3]/div/div/div[3]/div[1]/div[1]/div/div[1]',
               driver=driver).click()
    desc = wait_xpath(
        xpath='/html/body/div[1]/main/div[2]/div[3]/div/div/div[3]/div[1]/div[2]/div/div/div/div/div[5]/div/div/textarea[1]',
        driver=driver)
    time.sleep(5)
    action = ActionChains(driver)
    action.click(desc)
    action.key_down(Keys.CONTROL)
    action.send_keys('A')
    action.key_up(Keys.CONTROL)
    action.send_keys('aaa111')
    action.perform()
    wait_xpath(xpath='//*[@id="root"]/header/div/div[1]/div', driver=driver).click()
    time.sleep(5)
    desc2 = wait_xpath(
        xpath='/html/body/div[1]/main/div[2]/div[1]/div/div[3]/ul/div[2]/div[2]/div/div/div/div/div[1]/div/div/div[1]/div/div[2]/span',
        driver=driver)
    assert desc2.text == 'aaa111'
