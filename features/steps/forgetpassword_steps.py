import time
from behave import given, when, then, use_step_matcher

use_step_matcher("re")

@given('the user goes to the forgot password page of the ecommerce website')
def step(context):
    context.helperfunc.open('https://opencart.abstracta.us/index.php?route=account/forgotten') # goes to the forgot password page
    # context.helperfunc.maximize()

@when('the user enters their email: "([^"]*)"') #regex so that values from the table in feature could be inputted to the function
def enter_user_email(context,email): #the values from the table is inputted as email
    if email == "registered_email":
        #uses the registered email from previous feature test
        context.helperfunc.find_by_id('input-email').send_keys(context.registered_email) # find email field by using its id, enters registered email address
    elif email == "unregistered_email":
        context.helperfunc.find_by_id('input-email').send_keys(context.unregistered_email) # enters the unregistered email address
    else:
        context.helperfunc.find_by_id('input-email').send_keys(context.registered_email.replace("@example.com","")) # enters the registered email address but without the domain (@email.com)

@when('the user click continue button to reset')
def clicks_on_continue_reset_button(context):
    context.helperfunc.find_by_xpath("//input[@value='Continue']").click() #find login button using xpath ("button" with a "continue" text attribute) and click it


@then('the reset result should be: "([^"]*)"')
def check_succesfull_reset(context, result):
    #result is the expected result from the table located in 3_forgetpassword.feature file
    if result == "success":
        assert context.helperfunc.find_by_xpath("//div[contains(text(),'An email with a confirmation link has been sent your email address.')]") # if success a div with this message will show up
    elif result == "fail":
        # unregistered and invalid email results in the same warning showing up
        assert context.helperfunc.find_by_xpath("//div[contains(text(),' Warning: The E-Mail Address was not found in our records, please try again!')]") # if entered email is wrong a div with this text will show up
