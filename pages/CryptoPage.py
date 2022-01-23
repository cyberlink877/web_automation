# -*- coding:utf-8 -*-
import BasePage
import locators
from selenium import *
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

class Crypto_Page(BasePage.BasePage):
    # 输入Sign up的欄位
    def signup_fields(self, fullname, email, username):
        input_box = self.driver.get_element(locators.SignUpLocators.signup_page)
        input_box.click()
        input_box = self.driver.get_element(locators.SignUpLocators.fullname_field)
        input_box.click()
        input_box.send_keys(fullname)
        time.sleep(1)
        input_box = self.driver.get_element(locators.SignUpLocators.email_field)
        input_box.click()
        input_box.send_keys(email)
        time.sleep(1)
        input_box = self.driver.get_element(locators.SignUpLocators.username_field)
        input_box.click()
        input_box.send_keys(username)
        time.sleep(1)

    # 输入Sign in的欄位
    def signin_fields(self, email, password):
        input_box = self.driver.get_element(locators.SignInLocators.signin_page)
        input_box.click()
        input_box = self.driver.get_element(locators.SignInLocators.email_field)
        input_box.click()
        input_box.send_keys(email)
        time.sleep(1)
        input_box = self.driver.get_element(locators.SignInLocators.password_field)
        input_box.click()
        input_box.send_keys(password)
        time.sleep(1)






