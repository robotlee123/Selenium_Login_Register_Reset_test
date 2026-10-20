Feature: Register new user

Scenario Outline: Register with different credentials as inputs
    Given the user goes to the registration page of the ecommerce website
    When the user enters their credentials: "<email>", "<password>"
    And the user click the privacy policy checkbox
    And the user click continue button to register
    Then the register result should be "<result>"

    Examples:
        |email             |password     |result                                |
        |unregistered_email|shortpassword|password too short warning            |
        |unregistered_email|validpassword|success page                          |
        |registered_email  |validpassword|credentials already registered warning|