from selenium.webdriver.common.by import By

class SignUpLocators(object):
        signup_page = ("css>>>.navigation_list__1F7tc > li:nth-of-type(6) > a")
        signup_title = ("css>>>.SignUpContainer_title__2OLam")
        fullname_field = ("css>>>[name='name']")
        email_field = ("css>>>[name='email']")
        username_field = ("css>>>[name='username']")
        password_field = ("css>>>[name='password']")
        confirm_password_field = ("css>>>[name='confirmPassword']")

class SignInLocators(object):
        signin_page = ("xpath>>>//a[text()='Sign In']")
        signin_title = ("css>>>.LoginContainer_title__2wHsq")
        email_field = ("css>>>[name='email']")
        password_field = ("css>>>[name='password']")



