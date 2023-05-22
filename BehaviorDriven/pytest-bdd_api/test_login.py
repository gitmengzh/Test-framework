from pytest_bdd import given, when, then, scenarios
import requests

# Constants
LOGIN_URL = 'https://example.com/api/login'

# Scenarios
scenarios('login.feature')

# Fixtures
@given('I have valid credentials')
def valid_credentials():
    return {
        'username': 'myuser',
        'password': 'mypassword'
    }

@given('I have invalid credentials')
def invalid_credentials():
    return {
        'username': 'invaliduser',
        'password': 'invalidpassword'
    }

@when('I send a POST request to the login endpoint with those credentials')
def send_login_request(valid_credentials, invalid_credentials):
    data = valid_credentials if hasattr(valid_credentials, 'get') else invalid_credentials
    response = requests.post(LOGIN_URL, data=data)
    return response

@then('the response status code should be {status_code:d}')
def check_status_code(send_login_request, status_code):
    assert send_login_request.status_code == status_code

@then('the response body should contain a token')
def check_token(send_login_request):
    assert 'token' in send_login_request.json()