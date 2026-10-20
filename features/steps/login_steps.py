import time
from behave import given, when, then, use_step_matcher

use_step_matcher("re")

@given('the user goes to the login page of the ecommerce website')
def step(context):
    context.helperfunc.open('https://ecommerce-playground.lambdatest.io/index.php?route=account/login') # goes to the login page
    # context.helperfunc.maximize()

@when('the user enters their login credentials: "([^"]*)", "([^"]*)"')
def enter_user_login_credentials(context,email,password):
    if email == "registered_email":
        #uses the registered email from previous feature test
        context.helperfunc.find_by_id('input-email').send_keys(context.email) # find email field by using its id, enters registered email address
        if password == "validpassword":
            context.helperfunc.find_by_id('input-password').send_keys(context.password)# find password field by using its id, enters correct&valid password
        else:
            context.helperfunc.find_by_id('input-password').send_keys(context.password[:8])# enters wrong password (incomplete correct&valid password)
    else:
        context.helperfunc.find_by_id('input-email').send_keys(context.unregistered_email) # enters the unregistered email address
        context.helperfunc.find_by_id('input-password').send_keys(context.password)

@when('the user click login button')
def click_on_login_button(context):
    context.helperfunc.find_by_xpath("//input[@value='Login']").click() #find login button using xpath and click it

@then('the login result should be "([^"]*)"')
def check_succesfull_login(context, result):
    if result == "my account page":
        title = context.helperfunc.get_title()
        time.sleep(3)
        assert(title == "My Account") # successfull login redirects user to a page with this title
    elif result == "wrong password warning" or result == "unregistered account warning":
        # unregistered and wrong password results in the same warning showing up
        time.sleep(3)
        assert context.helperfunc.find_by_xpath("//div[contains(text(),'Warning: No match for E-Mail Address and/or Password.')]") # if entered credentials is wrong a div with this text can be found
