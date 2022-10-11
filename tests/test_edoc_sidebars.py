import time
import allure
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys
from conftest import wait_xpath


@allure.feature('TestsSidebars')
@allure.story('Positive searchbar test')
def test_searchbar_positive(driver_tests):
    searchbar = wait_xpath(xpath='//*[@id="input-with-icon-textfield"]')
    searchbar.click()
    searchbar.send_keys('c')  # Any CORRECT value applicable
    time.sleep(5)
    result = wait_xpath(xpath='/html/body/div[1]/main/div[2]/div[1]/div/div[3]/ul/div[1]/div[2]/div/div/div/div/div')
    result.click()

    try:
        wait_xpath(
            xpath='//*[@id="root"]/main/div[2]/div[2]/div/div/div/div[1]/div/div[2]/div[2]/div/div[1]/div/div[2]')
    except NoSuchElementException:
        assert False
    assert True


@allure.feature('TestsSidebars')
@allure.story('Download button test')
def test_download(driver_tests):
    download_btn = wait_xpath(xpath='//*[@id="root"]/main/div[2]/div[1]/div/div[2]/div[2]/button[1]')
    download_btn.click()

    try:
        wait_xpath(xpath='/html/body/div[3]/div[3]/div')
    except NoSuchElementException:
        assert False
    assert True


@allure.feature('TestsSidebars')
@allure.story('Feed menu test')
def test_feed(driver_tests):
    try:
        wait_xpath(xpath='/html/body/div[1]/main/div[2]/div[3]/div/div/div[2]')
    except NoSuchElementException:
        assert False
    assert True


@allure.feature('TestsSidebars')
@allure.story('Properties menu test')
def test_properties(driver_tests):
    wait_xpath(xpath='/html/body/div[1]/main/div[2]/div[3]/div/div/div[2]/div/ul/div[1]/li/div[2]/p/a').click()
    wait_xpath(xpath='/html/body/div[1]/main/div[2]/div[3]/div/div/div[1]/div/div/div/button[2]').click()
    wait_xpath(xpath='/html/body/div[1]/main/div[2]/div[3]/div/div/div[3]/div[1]/div[1]/div/div[1]').click()
    properties = wait_xpath(xpath='/html/body/div[1]/main/div[2]/div[3]/div/div/div[1]/div/div/div/button[2]')
    properties.click()

    try:
        wait_xpath(xpath='/html/body/div[1]/main/div[2]/div[3]/div/div/div[3]/div[1]/div[2]/div/div/div/div')
    except NoSuchElementException:
        assert False
    assert True


@allure.feature('TestsSidebars')
@allure.story('Version history menu test')
def test_version_history(driver_tests):
    wait_xpath(xpath='/html/body/div[1]/main/div[2]/div[3]/div/div/div[2]/div/ul/div[1]/li/div[2]/p/a').click()
    wait_xpath(xpath='/html/body/div[1]/main/div[2]/div[3]/div/div/div[1]/div/div/div/button[2]').click()
    wait_xpath(xpath='/html/body/div[1]/main/div[2]/div[3]/div/div/div[3]/div[1]/div[1]/div/div[1]').click()
    vers_hist = wait_xpath(xpath='/html/body/div[1]/main/div[2]/div[3]/div/div/div[1]/div/div/div/button[3]')
    vers_hist.click()

    try:
        wait_xpath(xpath='/html/body/div[1]/main/div[2]/div[3]/div/div/div[4]')
    except NoSuchElementException:
        assert False
    assert True


@allure.feature('TestsSidebars')
@allure.story('Description change on the left sidebar after changing it on the right one test')
def test_change_description(driver_tests):
    wait_xpath(xpath='/html/body/div[1]/main/div[2]/div[3]/div/div/div[2]/div/ul/div[1]/li/div[2]/p/a').click()
    wait_xpath(xpath='/html/body/div[1]/main/div[2]/div[3]/div/div/div[1]/div/div/div/button[2]').click()
    wait_xpath(xpath='/html/body/div[1]/main/div[2]/div[3]/div/div/div[3]/div[1]/div[1]/div/div[1]').click()
    desc = wait_xpath(
        xpath='/html/body/div[1]/main/div[2]/div[3]/div/div/div[3]/div[1]/div[2]/div/div/div/div/div[5]/div/div/textarea[1]')
    time.sleep(5)
    action = ActionChains(driver_tests)
    action.click(desc)
    action.key_down(Keys.CONTROL)
    action.send_keys('A')
    action.key_up(Keys.CONTROL)
    action.send_keys('aaa111')
    action.perform()
    wait_xpath(xpath='//*[@id="root"]/header/div/div[1]/div').click()
    time.sleep(5)
    desc2 = wait_xpath(
        xpath='/html/body/div[1]/main/div[2]/div[1]/div/div[3]/ul/div[6]/div[2]/div/div/div/div/div[1]/div/div/div[1]/div/div[2]/span')
    assert desc2.text == 'aaa111'
