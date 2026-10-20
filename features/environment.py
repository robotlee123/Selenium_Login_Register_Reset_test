import os
from configparser import ConfigParser
from helper.helper_web import get_browser
import uuid

def before_all(context):
    random_string = str(uuid.uuid4()).replace('-', '')
    context.email = "unique_email" + random_string[:4] + "@email.com"
    context.unregistered_email = "unregistered_email" + random_string[:4] + "@email.com"
    context.password = random_string[:10]

# def after_all(context):
#     context.helperfunc.close()

def before_scenario(context, scenario):
    config = ConfigParser()
    print((os.path.join(os.getcwd(), 'setup.cfg')))
    my_file = (os.path.join(os.getcwd(), 'setup.cfg'))
    config.read(my_file)

    # Reading the browser type from the configuration file
    helper_func = get_browser(config.get('Environment', 'Browser'))
    context.helperfunc = helper_func

def after_scenario(context, scenario):
    context.helperfunc.close()