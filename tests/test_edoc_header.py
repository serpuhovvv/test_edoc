import time

import allure
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys
from conftest import wait_xpath


@allure.feature('TestsHeader')
@allure.story('Positive searchbar test')
def test_searchbar_positive(driver_tests):
    searchbar = wait_xpath(xpath='//*[@id=":r5:"]')
    old_url = driver_tests.current_url
    searchbar.click()
    searchbar.send_keys('1006510')  # Any CORRECT value applicable
    result = wait_xpath(xpath='//*[@id="popover"]/div[3]/div/a/div')
    action = ActionChains(driver_tests)
    action.click_and_hold(result)
    action.release(result)
    action.perform()
    new_url = driver_tests.current_url

    assert old_url != new_url


@allure.feature('TestsHeader')
@allure.story('Negative searchbar test')
def test_searchbar_negative(driver_tests):
    searchbar = wait_xpath(xpath='//*[@id=":r5:"]')
    searchbar.click()
    searchbar.send_keys('09vfdjv89er')  # Any INCORRECT value applicable
    result = wait_xpath(xpath='//*[@id="popover"]/div[3]/div/p')

    assert result.text == 'There are no results for this query'


@allure.feature('TestsHeader')
@allure.story('User icon test')
def test_user_icon(driver_tests):
    icon = wait_xpath(xpath='/html/body/div[1]/header/div/div[3]/div/div/div')
    icon.click()

    try:
        wait_xpath(xpath='//*[@id="simple-popover"]/div[3]/div')
    except NoSuchElementException:
        assert False
    assert True


# @allure.feature('TestsHeader')
# @allure.story('User icon content test')
# def test_user_icon_content(driver_tests):
#       icon = wait_xpath(xpath='/html/body/div[1]/header/div/div[3]/div/div/div')
#       icon.click()
#       icon_open = wait_xpath(xpath='/html/body/div[3]/div[3]/div')

#       assert 'ADMIN PANEL' in icon_open.text \
#       and 'LOG OUT' in icon_open.text


@allure.feature('TestsHeader')
@allure.story('User icon admin panel test')
def test_user_icon_adminpanel(driver_tests):
    icon = wait_xpath(xpath='//*[@id="root"]/header/div/div[3]/div/div/div')
    icon.click()
    adminpanel = wait_xpath(xpath='//*[@id="simple-popover"]/div[3]/div/button[1]')
    adminpanel.click()
    new_url = driver_tests.current_url

    assert new_url == 'https://edoc.admortgage.us/admin' \
           or new_url == 'https://edoc.admortgage.com/admin' \
           or new_url == 'https://edoc.preprod.admortgage.net/admin'


@allure.feature('TestsHeader')
@allure.story('User icon logout test')
def test_user_icon_logout(driver_tests):
    icon = wait_xpath(xpath='//*[@id="root"]/header/div/div[3]/div/div/div')
    icon.click()
    logout = wait_xpath(xpath='//*[@id="simple-popover"]/div[3]/div/button[2]')
    logout.click()
    wait_xpath(xpath='//*[@id=":r2:"]')
    new_url = driver_tests.current_url

    assert new_url == 'https://edoc.admortgage.us/login' \
           or new_url == 'https://edoc.admortgage.com/login' \
           or new_url == 'https://edoc.preprod.admortgage.net/login'


@allure.feature('TestsHeader')
@allure.story('Loan number copying test')
def test_loan_number(driver_tests):
    a = wait_xpath(xpath='//*[@id="root"]/main/div[1]/div/span[1]')
    b = wait_xpath(xpath='//*[@id=":r5:"]')
    action = ActionChains(driver_tests)
    action.click(a)
    action.click_and_hold(b)
    action.release(b)
    action.key_down(Keys.CONTROL)
    action.send_keys('V')
    action.key_up(Keys.CONTROL)
    action.perform()
    c = wait_xpath(xpath='//*[@id="popover"]/div[3]/div/a/div')

    assert a.text in c.text
