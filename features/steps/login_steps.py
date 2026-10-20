import time
from behave import given, when, then

@given('the user goes to the login page of the ecommerce website')
def step(context):
    context.helperfunc.open('https://ecommerce-playground.lambdatest.io/index.php?route=account/login')
    # context.helperfunc.maximize()

@when('the user enters their registered credentials')
def enter_user_credentials(context):
    context.helperfunc.find_by_id('input-email').send_keys("iamtest23ing83e829w42@gmail.com")
    context.helperfunc.find_by_id('input-password').send_keys("asdfghjkl")

@when('the user click login button')
def click_on_login_button(context):
    context.helperfunc.find_by_xpath('/html/body/div[1]/div[5]/div[1]/div/div/div/div[2]/div/div/form/input').click()

@then('the user should be redirected to my account page')
def check_succesfull_login(context):
    title = context.helperfunc.get_title()
    time.sleep(3)
    assert(title == "My Account")

    