# -*- coding:utf-8 -*-


class BasePage(object):
    """
    This is a base page class for Page Object.
    """
    def __init__(self, driver):
        self.driver = driver
