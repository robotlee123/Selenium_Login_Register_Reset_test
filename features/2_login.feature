Feature: Login a registered user

Scenario Outline: Login with different credentials as inputs
    Given the user goes to the login page of the ecommerce website
    When the user enters their login credentials: "<email>", "<password>"
    And the user click login button
    Then the login result should be "<result>"

    Examples:
        |email             |password     |result                      |
        |registered_email  |validpassword|success                     |
        |registered_email  |wrongpassword|wrong password warning      |
        |unregistered_email|validpassword|unregistered account warning|

    