import allure
from conftest import wait_xpath


@allure.feature('TestsLogin')
@allure.story('Positive login')
def test_login_positive(driver_login):
    input_username = wait_xpath(xpath='//*[@id=":r0:"]', driver=driver_login)
    input_password = wait_xpath(xpath='//*[@id=":r1:"]', driver=driver_login)
    login_button = wait_xpath(xpath='//*[@id=":r2:"]', driver=driver_login)

    input_username.send_keys('testUser')
    input_password.send_keys('Pass')
    login_button.click()

    edoc_title = wait_xpath(xpath='//*[@id="root"]/header/div/div[1]/div/p', driver=driver_login)

    assert edoc_title.text == 'eDoc'


@allure.feature('TestsLogin')
@allure.story('Negative login wrong username and password')
def test_login_negative_wrong(driver_login):
    input_username = wait_xpath(xpath='//*[@id=":r0:"]', driver=driver_login)
    input_password = wait_xpath(xpath='//*[@id=":r1:"]', driver=driver_login)
    login_button = wait_xpath(xpath='//*[@id=":r2:"]', driver=driver_login)

    input_username.send_keys('000')
    input_password.send_keys('000')
    login_button.click()

    error_login = wait_xpath(xpath='//*[@id="root"]/div/div/div[2]/p', driver=driver_login)

    assert error_login.text == 'User name or password is wrong'


@allure.feature('TestsLogin')
@allure.story('Negative login empty username')
def test_login_negative_empty_username(driver_login):
    input_username = wait_xpath(xpath='//*[@id=":r0:"]', driver=driver_login)
    input_password = wait_xpath(xpath='//*[@id=":r1:"]', driver=driver_login)
    login_button = wait_xpath(xpath='//*[@id=":r2:"]', driver=driver_login)

    input_username.send_keys('')
    input_password.send_keys('Pass')
    login_button.click()

    username_required = wait_xpath(xpath='//*[@id=":r0:-helper-text"]', driver=driver_login)

    assert username_required.text == 'User name is required'


@allure.feature('TestsLogin')
@allure.story('Negative login empty password')
def test_login_negative_empty_pass(driver_login):
    input_username = wait_xpath(xpath='//*[@id=":r0:"]', driver=driver_login)
    input_password = wait_xpath(xpath='//*[@id=":r1:"]', driver=driver_login)
    login_button = wait_xpath(xpath='//*[@id=":r2:"]', driver=driver_login)

    input_username.send_keys('testUser')
    input_password.send_keys('')
    login_button.click()

    password_required = wait_xpath(xpath='//*[@id=":r1:-helper-text"]', driver=driver_login)

    assert password_required.text == 'Password is required'


@allure.feature('TestsLogin')
@allure.story('Negative login empty username and password')
def test_login_negative_empty_both(driver_login):
    input_username = wait_xpath(xpath='//*[@id=":r0:"]', driver=driver_login)
    input_password = wait_xpath(xpath='//*[@id=":r1:"]', driver=driver_login)
    login_button = wait_xpath(xpath='//*[@id=":r2:"]', driver=driver_login)

    input_username.send_keys('')
    input_password.send_keys('')
    login_button.click()

    username_required = wait_xpath(xpath='//*[@id=":r0:-helper-text"]', driver=driver_login)
    password_required = wait_xpath(xpath='//*[@id=":r1:-helper-text"]', driver=driver_login)

    assert username_required.text == 'User name is required'
    assert password_required.text == 'Password is required'


@allure.feature('TestsLogin')
@allure.story('Negative login space after username')
def test_login_positive_space_after_username(driver_login):
    input_username = wait_xpath(xpath='//*[@id=":r0:"]', driver=driver_login)
    input_password = wait_xpath(xpath='//*[@id=":r1:"]', driver=driver_login)
    login_button = wait_xpath(xpath='//*[@id=":r2:"]', driver=driver_login)

    input_username.send_keys('testUser ')
    input_password.send_keys('Pass')
    login_button.click()

    edoc_title = wait_xpath(xpath='//*[@id="root"]/header/div/div[1]/div/p', driver=driver_login)

    assert edoc_title.text == 'eDoc'


@allure.feature('TestsLogin')
@allure.story('Negative login space after password')
def test_login_negative_space_after_password(driver_login):
    input_username = wait_xpath(xpath='//*[@id=":r0:"]', driver=driver_login)
    input_password = wait_xpath(xpath='//*[@id=":r1:"]', driver=driver_login)
    login_button = wait_xpath(xpath='//*[@id=":r2:"]', driver=driver_login)

    input_username.send_keys('testUser')
    input_password.send_keys('Pass ')
    login_button.click()

    error_login = wait_xpath(xpath='//*[@id="root"]/div/div/div[2]/p', driver=driver_login)

    assert error_login.text == 'User name or password is wrong'
