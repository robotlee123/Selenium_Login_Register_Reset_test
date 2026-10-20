Feature: forget password

Scenario Outline: attempt to reset password with different email address as inputs
    Given the user goes to the forgot password page of the ecommerce website
    When the user enters their email: "<email>"
    And the user click continue button to reset
    Then the reset result should be: "<result>"

    Examples:
        |email             |result                      |
        |registered_email  |success                     |
        |invalid_email     |invalid password warning    |
        |unregistered_email|unregistered account warning|

    