'''
By using scenario outline diffrent sets of input could be tested easily. Behave will iterate through the table and the inputs and outputs sets is then inputed to the _steps.py.
The _steps.py takes in the inputs and outputs producing diffrent behaviours that is entered to the website (registering a registered email, wrong password, resetting password) this produces diffrent results -
which is then compared to the expected output from the _steps.py table using assert, if the expected output and output disagree the test fails.
'''
import time
from behave import given, when, then, use_step_matcher

use_step_matcher("re") # use regex so that table values could be substituted in

@given('the user goes to the registration page of the ecommerce website')
def step(context):
    context.helperfunc.open('https://ecommerce-playground.lambdatest.io/index.php?route=account/register')# open registration page
    # context.helperfunc.maximize()

@when('the user enters their credentials: "([^"]*)", "([^"]*)"') #regex so that values from the table in feature could be inputted to the function
def enter_user_credentials(context,email,password): #the values from the table is inputted as email and password
    # input a name and phone number
    # same name and phone number can be used multiple times
    context.helperfunc.find_by_id('input-firstname').send_keys("Iam")
    context.helperfunc.find_by_id('input-lastname').send_keys("AtestUser")
    context.helperfunc.find_by_id('input-telephone').send_keys("324235523")
    # this is because the website determines if a credential have been registered or not only by using the email
    if email == "unregistered_email":
        context.helperfunc.find_by_id('input-email').send_keys(context.email) # find email field by using its id, enters random unregistered email address
        if password == "validpassword":
            context.helperfunc.find_by_id('input-password').send_keys(context.password)# find password field by using its id, enters random string as password
            context.helperfunc.find_by_id('input-confirm').send_keys(context.password)# same password to confirm
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

@when('the user click continue button to register')
def click_on_continue_register_button(context):
    context.helperfunc.find_by_xpath("//input[@value='Continue']").click()#find continue button via xpath (searches for an "input" with "value" attribute equal to "Continue") and click it
    time.sleep(3) # pauses so i could see whats going on

@then('the register result should be "([^"]*)"')
def check_registration_result(context, result):
    #result is the expected result from the table located in 1_register.feature file
    if result == "success":
        title = context.helperfunc.get_title()
        assert(title == "Your Account Has Been Created!") # if success in creating an account the user redirected to a page with this title
    elif result == "password too short warning":
        assert context.helperfunc.find_by_xpath("//div[contains(text(),'Password must be between 4 and 20 characters!')]") # if entered password is too short a div with this text can be found
    elif result == "credentials already registered warning":
        assert context.helperfunc.find_by_xpath("//div[contains(text(),'Warning: E-Mail Address is already registered!')]") # if entered credentials is registered a div with this text can be found
        