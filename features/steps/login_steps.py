import time
from behave import given, when, then, use_step_matcher

use_step_matcher("re")

@given('the user goes to the login page of the ecommerce website')
def step(context):
    context.helperfunc.open('https://opencart.abstracta.us/index.php?route=account/login') # goes to the login page
    # context.helperfunc.maximize()

@when('the user enters their login credentials: "([^"]*)", "([^"]*)"') #regex so that values from the table in feature could be inputted to the function
def enter_user_login_credentials(context,email,password): #the values from the table is inputted as email and password
    if email == "registered_email":
        #uses a pre registered email
        context.helperfunc.find_by_id('input-email').send_keys(context.registered_email) # find email field by using its id, enters registered email address
        if password == "validpassword":
            context.helperfunc.find_by_id('input-password').send_keys(context.registered_password)# find password field by using its id, enters correct&valid password
        else:
            context.helperfunc.find_by_id('input-password').send_keys(context.password)# enters wrong password
    else:
        context.helperfunc.find_by_id('input-email').send_keys(context.unregistered_email) # enters the unregistered email address
        context.helperfunc.find_by_id('input-password').send_keys(context.password)
    # time.sleep(3)

@when('the user click login button')
def click_on_login_button(context):
    context.helperfunc.find_by_xpath("//input[@value='Login']").click() #find login button using xpath ("input" with "value" attribute equals to "login") and click it


@then('the login result should be "([^"]*)"')
def check_succesfull_login(context, result):
    #result is the expected result from the table located in 2_login.feature file
    if result == "success":
        title = context.helperfunc.get_title()
        assert(title == "My Account") # successfull login redirects user to a page with this title
    elif result == "fail":
        # unregistered and wrong password results in the same warning showing up
        assert context.helperfunc.find_by_xpath("//div[contains(text(),'Warning: No match for E-Mail Address and/or Password.')]") # if entered credentials is wrong (email or password) a div with this text can be found
