Feature: Register new user

Scenario: Successfull registration of a new user with an unregistered credentials
    Given the user goes to the registration page of the ecommerce website
    When the user enters their credentials
    And the user click the privacy policy checkbox
    And the user click continue button
    Then the user should be redirected to success page