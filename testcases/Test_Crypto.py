# -*- coding:utf-8 -*-
import unittest
from utils.PublicMethod import PublicMethod
from utils.configfile import env_info
from pages.CryptoPage import Crypto_Page
import time
from pages.locators import SignUpLocators
from pages.locators import SignInLocators

homepage_title = u'Crypto.com NFT | Buy, Sell, Discover Exclusive Digital Collectibles'
signup_label = u'Sign Up'
signin_label = u'Sign In'

class CryptoTest(unittest.TestCase):

    def setUp(self):
        global driver
        # 实例化utils下PublicMethod类
        self.driver = PublicMethod(env_info['browser'])
        self.driver.open_link(env_info['url'])
        self.driver.wd.implicitly_wait(10)
        self.driver.max_window()

    def test_01_hompepage(self):
        self._homepage_content(u"Check NFT HomePage",homepage_title)

    def test_02_signuppage(self):
        self._signup_content(u"Check sign up page existing",signup_label)

    def test_03_signinpage(self):
        self._signin_content(u"Check sign in page existing",signin_label)


    def tearDown(self):
        self.driver.close()

    def _homepage_content(self, description, expected):
        print('case description: ', description)
        # cryptopage = Crypto_Page(self.driver)
        self.driver.wd.implicitly_wait(5)
        time.sleep(3)
        self._verify_homepage(expected)

    def _signup_content(self, description, expected):
        print('case description: ', description)
        cryptopage = Crypto_Page(self.driver)
        cryptopage.signup_fields('PaulChen','PaulChen@gmail.com','PaulChen')
        self.driver.wd.implicitly_wait(5)
        time.sleep(3)
        self._verify_signup(expected)

    def _signin_content(self, description, expected):
        print('case description: ', description)
        cryptopage = Crypto_Page(self.driver)
        cryptopage.signin_fields('PaulChen@gmail.com','PaulChen123456')
        self.driver.wd.implicitly_wait(5)
        time.sleep(3)
        self._verify_signin(expected)

    # 验證title首頁
    def _verify_homepage(self, expected):
        actual_text = self.driver.get_title()
        expected_text = expected
        if actual_text == expected_text:
            self.assertEqual(expected_text, actual_text)
            print('PASS-----', 'Expect Result:', expected_text, 'Actual Result:', actual_text)
        else:
            self.assertEqual(expected_text, actual_text)
            print('FAIL-----', 'Expect Result:', expected_text, '***Actual Result:', actual_text)

    # 驗證Signup
    def _verify_signup(self, expected):
        actual_text = self.driver.get_text(SignUpLocators.signup_title)
        expected_text = expected
        if actual_text == expected_text:
            self.assertEqual(expected_text, actual_text)
            print('PASS-----', 'Expect Result:', expected_text, 'Actual Result:', actual_text)
        else:
            self.assertEqual(expected_text, actual_text)
            print('FAIL-----', 'Expect Result:', expected_text, 'Actual Result:', actual_text)

    # 驗證Signin
    def _verify_signin(self, expected):
        actual_text = self.driver.get_text(SignInLocators.signin_title)
        expected_text = expected
        if actual_text == expected_text:
            self.assertEqual(expected_text, actual_text)
            print('PASS-----', 'Expect Result:', expected_text, 'Actual Result:', actual_text)
        else:
            self.assertEqual(expected_text, actual_text)
            print('FAIL-----', 'Expect Result:', expected_text, 'Actual Result:', actual_text)


if __name__ == "__main__":
    suite = unittest.TestSuite()
    suite.addTest(CryptoTest('test_01_hompepage'))
    unittest.TextTestRunner().run(suite)
