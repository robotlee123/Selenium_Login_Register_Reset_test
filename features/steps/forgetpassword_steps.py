import time
from behave import given, when, then, use_step_matcher

use_step_matcher("re")

@given('the user goes to the forgot password page of the ecommerce website')
def step(context):
    context.helperfunc.open('https://ecommerce-playground.lambdatest.io/index.php?route=account/forgotten') # goes to the forgot password page
    # context.helperfunc.maximize()

@when('the user enters their email: "([^"]*)"')
def enter_user_email(context,email):
    if email == "registered_email":
        #uses the registered email from previous feature test
        context.helperfunc.find_by_id('input-email').send_keys(context.email) # find email field by using its id, enters registered email address
    elif email == "unregistered_email":
        context.helperfunc.find_by_id('input-email').send_keys(context.unregistered_email) # enters the unregistered email address
    else:
        context.helperfunc.find_by_id('input-email').send_keys(context.email.replace("@email.com","")) # enters the registered email address but without the domain (@email.com)

@when('the user click continue button to reset')
def clicks_on_continue_reset_button(context):
    context.helperfunc.find_by_xpath("//button[text()='Continue']").click() #find login button using xpath and click it

@then('the reset result should be: "([^"]*)"')
def check_succesfull_reset(context, result):
    if result == "success":
        time.sleep(3)
        assert context.helperfunc.find_by_xpath("//div[contains(text(),'An email with a confirmation link has been sent your email address.')]") # if success this div will show up
    elif result == "invalid password warning" or result == "unregistered account warning":
        # unregistered and invalid password results in the same warning showing up
        time.sleep(3)
        assert context.helperfunc.find_by_xpath("//div[contains(text(),' Warning: The E-Mail Address was not found in our records, please try again!')]") # if entered email is wrong a div with this text can be found
