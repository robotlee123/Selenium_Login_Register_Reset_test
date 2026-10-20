Feature: Login a registered user

Scenario: Successfull login using registered credentials
    Given the user goes to the login page of the ecommerce website
    When the user enters their registered credentials
    And the user click login button
    Then the user should be redirected to my account page