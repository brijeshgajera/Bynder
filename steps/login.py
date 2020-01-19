from behave import given, when, then, step, fixture
from framework.library import CommonClass

commonClass = CommonClass()


@given(u'I load the website and I go to "{pagename}" page')
def step_impl(context, pagename):
    commonClass.load_website()


@when(u'I Enter "{username}" in username field')
def step_impl(context, username):
    if username != "":
        commonClass.input_text("id", "inputEmail", username)


@step(u'I Enter "{password}" in password field')
def step_impl(context, password):
    if password != "":
        commonClass.input_text("id", "inputPassword", password)


@step(u'I press the "{button}" button')
def step_impl(context, button):
    commonClass.input_click("class", "login-btn")


@then(u'Login should be success and user should be redirected to "{dashboard}" page')
def step_impl(context, dashboard):
    commonClass.login("class", "cbox_messagebox", assert_value=dashboard)


@then(u'Login should fail with error message "{error_message}"')
def step_impl(context, error_message):
    commonClass.login("class", "cbox_messagebox", assert_value="dashboard", error_message=error_message)

@step(u'Logout from portal')
def step_impl(context, error_message):
    commonClass.logout()


def after_all(context):
    commonClass.closeBrowser()
