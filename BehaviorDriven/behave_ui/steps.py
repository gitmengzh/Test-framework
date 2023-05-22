from behave import *
from selenium import webdriver

@given('I am on the login page')
def step_impl(context):
    context.driver = webdriver.Chrome()
    context.driver.get("https://example.com/login")

@when('I enter valid username and password')
def step_impl(context):
    context.driver.find_element_by_name("username").send_keys("myuser")
    context.driver.find_element_by_name("password").send_keys("mypassword")

@when('I enter invalid username and password')
def step_impl(context):
    context.driver.find_element_by_name("username").send_keys("invaliduser")
    context.driver.find_element_by_name("password").send_keys("invalidpassword")

@when('I click the login button')
def step_impl(context):
    context.driver.find_element_by_css_selector("button[type='submit']").click()

@then('I should be redirected to the dashboard')
def step_impl(context):
    assert "dashboard" in context.driver.current_url

@then('I should see an error message')
def step_impl(context):
    assert "Invalid login" in context.driver.page_source