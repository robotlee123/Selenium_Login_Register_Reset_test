import time
from behave import given, when, then

@given('the user goes to the registration page of the ecommerce website')
def step(context):
    context.helperfunc.open('https://ecommerce-playground.lambdatest.io/index.php?route=account/register')
    # context.helperfunc.maximize()

@when('the user enters their credentials')
def enter_user_credentials(context):
    context.helperfunc.find_by_id('input-firstname').send_keys("Iam")
    context.helperfunc.find_by_id('input-lastname').send_keys("AtestUser")
    context.helperfunc.find_by_id('input-email').send_keys("iamtest23ing83e829w42@gmail.com")
    context.helperfunc.find_by_id('input-telephone').send_keys("324235523")
    context.helperfunc.find_by_id('input-password').send_keys("asdfghjkl")
    context.helperfunc.find_by_id('input-confirm').send_keys("asdfghjkl")

@when('the user click the privacy policy checkbox')
def click_policy_checkbox(context):
    context.helperfunc.find_by_css_selector("label[for='input-agree']").click()

@when('the user click continue button')
def click_on_continue_button(context):
    context.helperfunc.find_by_xpath('/html/body/div[1]/div[5]/div[1]/div/div/form/div/div/input').click()

@then('the user should be redirected to success page')
def check_succesfull_registration(context):
    title = context.helperfunc.get_title()
    time.sleep(3)
    assert(title == "Your Account Has Been Created!")
    