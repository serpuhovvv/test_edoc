import allure
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys
from conftest import wait_xpath


@allure.feature('TestsHeader')
@allure.story('Positive searchbar test')
def test_searchbar_positive(driver):
    searchbar = wait_xpath(xpath='//*[@id=":r5:"]', driver=driver)
    old_url = driver.current_url
    searchbar.click()
    searchbar.send_keys('1006510')  # Any CORRECT value applicable
    result = wait_xpath(xpath='//*[@id="popover"]/div[3]/div/a/div', driver=driver)
    action = ActionChains(driver)
    action.click_and_hold(result)
    action.release(result)
    action.perform()
    new_url = driver.current_url

    assert old_url != new_url


@allure.feature('TestsHeader')
@allure.story('Negative searchbar test')
def test_searchbar_negative(driver):
    searchbar = wait_xpath(xpath='//*[@id=":r5:"]', driver=driver)
    searchbar.click()
    searchbar.send_keys('09vfdjv89er')  # Any INCORRECT value applicable
    result = wait_xpath(xpath='//*[@id="popover"]/div[3]/div/p', driver=driver)

    assert result.text == 'There are no results for this query'


@allure.feature('TestsHeader')
@allure.story('User icon test')
def test_user_icon(driver):
    icon = wait_xpath(xpath='//*[@id="root"]/header/div/div[3]/div/div/div', driver=driver)
    icon.click()

    try:
        wait_xpath(xpath='//*[@id="simple-popover"]/div[3]/div', driver=driver)
    except NoSuchElementException:
        assert False
    assert True


@allure.feature('TestsHeader')
@allure.story('User icon content test')
def test_user_icon_content(driver):
    icon = wait_xpath(xpath='//*[@id="root"]/header/div/div[3]/div/div/div', driver=driver)
    icon.click()
    icon_open = wait_xpath(xpath='//*[@id="simple-popover"]/div[3]/div', driver=driver)

    assert 'ADMIN PANEL', 'LOG OUT' in icon_open.text


@allure.feature('TestsHeader')
@allure.story('User icon admin panel test')
def test_user_icon_adminpanel(driver):
    icon = wait_xpath(xpath='//*[@id="root"]/header/div/div[3]/div/div/div', driver=driver)
    icon.click()
    adminpanel = wait_xpath(xpath='//*[@id="simple-popover"]/div[3]/div/button[1]', driver=driver)
    adminpanel.click()
    new_url = driver.current_url

    assert new_url == 'https://edoc.admortgage.us/admin'


@allure.feature('TestsHeader')
@allure.story('User icon logout test')
def test_user_icon_logout(driver):
    icon = wait_xpath(xpath='//*[@id="root"]/header/div/div[3]/div/div/div', driver=driver)
    icon.click()
    logout = wait_xpath(xpath='//*[@id="simple-popover"]/div[3]/div/button[2]', driver=driver)
    logout.click()
    wait_xpath(xpath='//*[@id=":r2:"]', driver=driver)
    new_url = driver.current_url

    assert new_url == 'https://edoc.admortgage.us/login'


@allure.feature('TestsHeader')
@allure.story('Loan number copying test')
def test_loan_number(driver):
    a = wait_xpath(xpath='//*[@id="root"]/main/div[1]/div/span[1]', driver=driver)
    b = wait_xpath(xpath='//*[@id=":r5:"]', driver=driver)
    action = ActionChains(driver)
    action.click(a)
    action.click_and_hold(b)
    action.release(b)
    action.key_down(Keys.CONTROL)
    action.send_keys('V')
    action.key_up(Keys.CONTROL)
    action.perform()
    c = wait_xpath(xpath='//*[@id="popover"]/div[3]/div/a/div', driver=driver)

    assert a.text in c.text
