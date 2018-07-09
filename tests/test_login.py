# -*- coding: utf-8 -*-
from tests.base_test import BaseTest
from pages.modals.pin_modal import PinModal
from pages.login import LoginPage
from pages.exchange import ExchangePage
from config.input_data import input_data
from nose.tools import assert_true

class TestLogin(BaseTest):

    def test_01_login_and_logout_with_credentials(self):
        '''
                Login with username/password
        '''
        self.login_page = LoginPage(self.driver)
        self.exchange_page = ExchangePage(self.driver)
        self.pin_modal = PinModal(self.driver)
        self.os = str(self.driver.desired_capabilities['platformName']).lower()

        self.exchange_page.openLoginPage().login_with_credentials(input_data['correct_username_production'],
                                                                  input_data['correct_password_production'])
        assert_true(self.pin_modal.is_element_visible(*getattr(self.pin_modal, '_enable_pin_activate_button_' + self.os)),"PIN activation button is not visible")
        print "User is logged in."
        self.pin_modal.dismiss_pin().openAccountPage().logout()
        assert_true(self.exchange_page.is_element_visible(*getattr(self.exchange_page, '_join_login_button_' + self.os)), "JOIN/LOGIN button is not visible")
        print "User is logged out."