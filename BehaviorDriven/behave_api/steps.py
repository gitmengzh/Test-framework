from behave import *
import requests


@given('I have valid credentials')
def step_impl(context):
    context.data = {
        'username': 'myuser',
        'password': 'mypassword'
    }


@given('I have invalid credentials')
def step_impl(context):
    context.data = {
        'username': 'invaliduser',
        'password': 'invalidpassword'
    }

@when('I send a POST request to the login endpoint with those credentials')
def step_impl(context):
    context.response = requests.post('https://example.com/api/login', data=context.data)


@then('the response status code should be {status_code:d}')
def step_impl(context, status_code):
    assert context.response.status_code == status_code


@then('the response body should contain a token')
def step_impl(context):
    assert 'token' in context.response.json()