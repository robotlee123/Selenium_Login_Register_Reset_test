import os
from configparser import ConfigParser
from helper.helper_web import get_browser
import uuid

    
def before_scenario(context, scenario):
    #before each scenario run this
    # loads setup.cfg and parses it
    config = ConfigParser()
    print((os.path.join(os.getcwd(), 'setup.cfg')))
    my_file = (os.path.join(os.getcwd(), 'setup.cfg'))
    config.read(my_file)

    # Reading the browser type from the configuration file
    helper_func = get_browser(config.get('Environment', 'Browser'))#find value of Browser under the Environment tag passes it to get_browser in helper_web.py, initialises helperfunc class with the chrome driver.
    context.helperfunc = helper_func # passes the helperfunc object to the context to be used by the scenarios

    random_string = str(uuid.uuid4()).replace('-', '') #generate random strings with no -
    context.email = "notregisteredyet_email" + random_string[:4] + "@email.com" #creates email address that will be registered

    context.registered_email = "registered_user_oieko30u0j@example.com" #pre registered email and password
    context.registered_password = "12345678"

    context.unregistered_email = "unregistered_email" + random_string[:4] + "@email.com" #creates email address that will not be registered
    context.password = random_string[:10] #from the random_string select 10 character to be a password
    context.longpassword = random_string[:21] #from the random_string select 21 character to be a password
    
def after_scenario(context, scenario):
    #after each scenario quit the driver
    context.helperfunc.close() 