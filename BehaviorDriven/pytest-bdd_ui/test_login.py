from pytest_bdd import given, when, then, scenarios
from selenium import webdriver
import time

# Constants
LOGIN_URL = 'https://example.com/login'
DASHBOARD_URL = 'https://example.com/dashboard'
INVALID_LOGIN_MSG = 'Invalid login'

# Scenarios
scenarios('login.feature')

# Fixtures
@given('I am on the login page')
def login_page():
    driver = webdriver.Chrome()
    driver.get(LOGIN_URL)
    yield driver
    driver.quit()

@when('I enter valid username and password')
def enter_valid_credentials(login_page):
    driver = login_page
    driver.find_element_by_name('username').send_keys('myuser')
    driver.find_element_by_name('password').send_keys('mypassword')

@when('I enter invalid username and password')
def enter_invalid_credentials(login_page):
    driver = login_page
    driver.find_element_by_name('username').send_keys('invaliduser')
    driver.find_element_by_name('password').send_keys('invalidpassword')

@when('I click the login button')
def click_login_button(login_page):
    driver = login_page
    driver.find_element_by_css_selector("button[type='submit']").click()

@then('I should be redirected to the dashboard')
def redirected_to_dashboard(login_page):
    assert login_page.current_url == DASHBOARD_URL

@then('I should see an error message')
def see_error_message(login_page):
    assert INVALID_LOGIN_MSG in login_page.page_source