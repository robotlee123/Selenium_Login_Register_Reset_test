Feature: Register new user

Scenario Outline: Register with different credentials as inputs
    Given the user goes to the registration page of the ecommerce website
    When the user enters their credentials: "<email>", "<password>"
    And the user click the privacy policy checkbox
    And the user click continue button
    Then the user should see "<result>"

    Examples:
        |email             |password     |result                                |
        |unregistered_email|shortpassword|password too short warning            |
        |unregistered_email|validpassword|success page                          |
        |registered_email  |validpassword|credentials already registered warning|