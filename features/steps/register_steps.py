import time
from behave import given, when, then, use_step_matcher

use_step_matcher("re")

@given('the user goes to the registration page of the ecommerce website')
def step(context):
    context.helperfunc.open('https://ecommerce-playground.lambdatest.io/index.php?route=account/register')# open registration page
    # context.helperfunc.maximize()

@when('the user enters their credentials: "([^"]*)", "([^"]*)"')
def enter_user_credentials(context,email,password):
    context.helperfunc.find_by_id('input-firstname').send_keys("Iam")
    context.helperfunc.find_by_id('input-lastname').send_keys("AtestUser")
    context.helperfunc.find_by_id('input-telephone').send_keys("324235523")
    # the website determines if a credential have been registered or not only by using the email
    if email == "unregistered_email":
        context.helperfunc.find_by_id('input-email').send_keys(context.email) # find email field by using its id, enters random unregistered email address
        if password == "validpassword":
            context.helperfunc.find_by_id('input-password').send_keys(context.password)# find password field by using its id, enters random string as password
            context.helperfunc.find_by_id('input-confirm').send_keys(context.password)
        else:
            context.helperfunc.find_by_id('input-password').send_keys(context.password[:1])# enters random string of length 1 as password
            context.helperfunc.find_by_id('input-confirm').send_keys(context.password[:1])
    else:
        context.helperfunc.find_by_id('input-email').send_keys(context.email) # enters the email address that was just registered
        context.helperfunc.find_by_id('input-password').send_keys(context.password)
        context.helperfunc.find_by_id('input-confirm').send_keys(context.password)

@when('the user click the privacy policy checkbox')
def click_policy_checkbox(context):
    context.helperfunc.find_by_xpath("//label[@for='input-agree']").click()#find checkbox via xpath (searches for a "label" with "for" attribute equal to "input-agree") and click it

@when('the user click continue button')
def click_on_continue_button(context):
    context.helperfunc.find_by_xpath("//input[@value='Continue']").click()#find continue button via xpath (searches for an "input" with "value" attribute equal to "Continue") and click it

@then('the user should see "([^"]*)"')
def check_registration_result(context, result):
    #result is the expected result from the table located in 1_register.feature file
    if result == "success page":
        title = context.helperfunc.get_title()
        time.sleep(3)
        assert(title == "Your Account Has Been Created!") # if success in creating an account the user redirected to a page with this title
    elif result == "password too short warning":
        assert context.helperfunc.find_by_xpath("//div[contains(text(),'Password must be between 4 and 20 characters!')]") # if entered password is too short a div with this text can be found
        time.sleep(3)
    elif result == "credentials already registered warning":
        time.sleep(3)
        assert context.helperfunc.find_by_xpath("//div[contains(text(),'Warning: E-Mail Address is already registered!')]") # if entered credentials is registered a div with this text can be found
        