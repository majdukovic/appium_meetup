# -*- coding: utf-8 -*-
from appium.webdriver.common.mobileby import By
from pages.login import LoginPage
from pages.page import Page


class ExchangePage(Page):
    '''
           This class contains element locators and action methods for the Login page
    '''

    def __init__(self, driver):
        super(ExchangePage, self).__init__(driver)
        self.login_page = LoginPage(self.driver)
        self.os = str(self.driver.desired_capabilities['platformName']).lower()

    # Exchange Android
    _join_login_button_android = (By.ID, 'com.matchbook.client:id/loginButton')
    _menu_button_android = (By.XPATH, '//android.widget.ImageButton[@content-desc="Navigate up"]')
    _my_bets_button_android = (By.XPATH, '//android.widget.RelativeLayout[@resource-id="com.matchbook.client:id/action_betslip"]')
    _account_button_android = (By.ID, 'com.matchbook.client:id/action_account')
    _account_balance_android = (By.ID, 'com.matchbook.client:id/account_balance')
    _back_offer_buttons_android = (By.XPATH, '//android.widget.RelativeLayout[@resource-id="com.matchbook.client:id/rlRunnerB"]')
