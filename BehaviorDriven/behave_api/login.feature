Feature: Login API
  As a user
  I want to log in to my account
  So that I can access my dashboard

  Scenario: Successful login
    Given I have valid credentials
    When I send a POST request to the login endpoint with those credentials
    Then the response status code should be 200
    And the response body should contain a token

  Scenario: Invalid login
    Given I have invalid credentials
    When I send a POST request to the login endpoint with those credentials
    Then the response status code should be 401