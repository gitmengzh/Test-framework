Feature: Login Page UI
  As a user
  I want to log in to my account
  So that I can access my dashboard

  Scenario: Successful login
    Given I am on the login page
    When I enter valid username and password
    And I click the login button
    Then I should be redirected to the dashboard

  Scenario: Invalid login
    Given I am on the login page
    When I enter invalid username and password
    And I click the login button
    Then I should see an error message