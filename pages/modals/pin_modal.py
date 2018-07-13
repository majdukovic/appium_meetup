# -*- coding: utf-8 -*-
from appium.webdriver.common.mobileby import By
from pages.page import Page
import time


class PinModal(Page):
    '''
            This class contains element locators and action methods for the PIN modal
    '''

    def __init__(self, driver):
        super(PinModal, self).__init__(driver)
        self.os = str(self.driver.desired_capabilities['platformName']).lower()

    # PIN modal Android
    _enable_pin_activate_button_android = (By.ID, 'com.matchbook.client:id/activatePin')
    _enable_pin_no_tnx_button_android = (By.ID, 'com.matchbook.client:id/noThxButton')
    _enter_pin_field_android = (By.ID, 'com.matchbook.client:id/pin1')

    _pins_dont_match_expected_message_android = 'PINs donâ€™t match. Please try again'
    _first_wrong_password_expected_message_android = 'Incorrect password, please try again. Attempts left: 2.'
    _second_wrong_password_expected_message_android = 'Incorrect password, please try again. Attempts left: 1.'
    _pin_enabled_expected_message_android = 'You can now login to your Matchbook account with PIN Login.'

    _pin_enabled_actual_message_android = (By.ID, 'com.matchbook.client:id/tvPinMessage')
    _first_wrong_password_actual_message_android = (By.ID, 'com.matchbook.client:id/tvPinMessage')
    _second_wrong_password_actual_message_android = (By.ID, 'com.matchbook.client:id/tvPinMessage')
    _pin_enabled_actual_message_android = (By.ID, 'com.matchbook.client:id/tvPinMessage')

    _enter_pwd_field_android = (By.ID, 'com.matchbook.client:id/pinPwd')
    _cancel_button_android = (By.ID, 'com.matchbook.client:id/cancelButton')
    _ok_button_android = (By.ID, 'com.matchbook.client:id/okButton')

    # PIN modal iOS
    _enable_pin_dialog_ios = (By.NAME, 'Enable PIN Login')
    _enable_pin_activate_button_ios = (By.NAME, 'Activate PIN Login')
    _enable_pin_no_tnx_button_ios = (By.NAME, 'No thanks')
    _set_pin_field_home_1_ios = (By.XPATH,
                                 '//XCUIElementTypeApplication[@name="Matchbook"]/XCUIElementTypeWindow[1]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther[1]/XCUIElementTypeOther[2]/XCUIElementTypeOther[2]/XCUIElementTypeOther[1]/XCUIElementTypeTextField')
    _set_pin_field_home_2_ios = (By.XPATH,
                                 '//XCUIElementTypeApplication[@name="Matchbook"]/XCUIElementTypeWindow[1]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther[1]/XCUIElementTypeOther[2]/XCUIElementTypeOther[2]/XCUIElementTypeOther[2]/XCUIElementTypeTextField')
    _set_pin_field_home_3_ios = (By.XPATH,
                                 '//XCUIElementTypeApplication[@name="Matchbook"]/XCUIElementTypeWindow[1]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther[1]/XCUIElementTypeOther[2]/XCUIElementTypeOther[2]/XCUIElementTypeOther[3]/XCUIElementTypeTextField')
    _set_pin_field_home_4_ios = (By.XPATH,
                                 '//XCUIElementTypeApplication[@name="Matchbook"]/XCUIElementTypeWindow[1]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther[1]/XCUIElementTypeOther[2]/XCUIElementTypeOther[2]/XCUIElementTypeOther[4]/XCUIElementTypeTextField')
    _enter_pin_field_1_ios = (By.XPATH,
                              '//XCUIElementTypeApplication[@name="Matchbook"]/XCUIElementTypeWindow[1]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeScrollView/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther[1]')
    _enter_pin_field_2_ios = (By.XPATH,
                              '//XCUIElementTypeApplication[@name="Matchbook"]/XCUIElementTypeWindow[1]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeScrollView/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther[2]')
    _enter_pin_field_3_ios = (By.XPATH,
                              '//XCUIElementTypeApplication[@name="Matchbook"]/XCUIElementTypeWindow[1]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeScrollView/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther[3]')
    _enter_pin_field_4_ios = (By.XPATH,
                              '//XCUIElementTypeApplication[@name="Matchbook"]/XCUIElementTypeWindow[1]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeScrollView/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther[4]')
    _set_pin_field_settings_1_ios = (By.XPATH,
                                     '//XCUIElementTypeApplication[@name="Matchbook"]/XCUIElementTypeWindow[1]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther[1]/XCUIElementTypeOther[2]/XCUIElementTypeOther[2]/XCUIElementTypeOther[1]')
    _set_pin_field_settings_2_ios = (By.XPATH,
                                     '//XCUIElementTypeApplication[@name="Matchbook"]/XCUIElementTypeWindow[1]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther[1]/XCUIElementTypeOther[2]/XCUIElementTypeOther[2]/XCUIElementTypeOther[2]')
    _set_pin_field_settings_3_ios = (By.XPATH,
                                     '//XCUIElementTypeApplication[@name="Matchbook"]/XCUIElementTypeWindow[1]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther[1]/XCUIElementTypeOther[2]/XCUIElementTypeOther[2]/XCUIElementTypeOther[3]')
    _set_pin_field_settings_4_ios = (By.XPATH,
                                     '//XCUIElementTypeApplication[@name="Matchbook"]/XCUIElementTypeWindow[1]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther[1]/XCUIElementTypeOther[2]/XCUIElementTypeOther[2]/XCUIElementTypeOther[4]')
    _pin_title_text_ios = (By.NAME, 'Please enter a 4-digit PIN')

    _enter_pin_text_ios = 'Please enter a 4-digit PIN'
    _confirm_pin_text_ios = 'Please confirm your 4-digit PIN'
    _pins_dont_match_text_ios = 'PINs donâ€™t match. Please try again'
    _first_wrong_password_text_ios = 'Incorrect password, please try again. Attempts left: 2.'
    _second_wrong_password_text_ios = 'Incorrect password, please try again. Attempts left: 1.'
    _pin_enabled_text_ios = 'You can now login to your Matchbook account with PIN Login.'

    _enter_pwd_field_ios = (By.XPATH,
                            '//XCUIElementTypeAlert[@name="Enable PIN Login"]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeOther[1]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeCollectionView/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeSecureTextField')
    _cancel_button_ios = (By.NAME, 'Cancel')
    _ok_button_ios = (By.NAME, 'OK')

    def enable_pin(self, pin, password):
        ''' Method for enabling PIN and logging in with a PIN.
                @param pin: string - PIN provided will be used during PIN setup
                @param password: string - Password provided will be used during PIN setup
        '''
        from pages.login import LoginPage
        from pages.exchange import ExchangePage
        self.login_page = LoginPage(self.driver)
        self.exchange_page = ExchangePage(self.driver)
        self.driver.find_element(*getattr(self, '_enable_pin_activate_button_' + self.os)).click()
        if self.os == 'android':
            self.driver.find_element(*getattr(self, '_enter_pin_field_' + self.os)).send_keys(pin)
            self.driver.find_element(*getattr(self, '_enter_pin_field_' + self.os)).send_keys(pin)
        else:
            self.driver.find_element(*getattr(self, '_set_pin_field_home_1_' + self.os)).send_keys(pin[0])
            self.driver.find_element(*getattr(self, '_set_pin_field_home_2_' + self.os)).send_keys(pin[1])
            self.driver.find_element(*getattr(self, '_set_pin_field_home_3_' + self.os)).send_keys(pin[2])
            self.driver.find_element(*getattr(self, '_set_pin_field_home_4_' + self.os)).send_keys(pin[3])
            time.sleep(2)
            self.driver.find_element(*getattr(self, '_set_pin_field_home_1_' + self.os)).send_keys(pin[0])
            self.driver.find_element(*getattr(self, '_set_pin_field_home_2_' + self.os)).send_keys(pin[1])
            self.driver.find_element(*getattr(self, '_set_pin_field_home_3_' + self.os)).send_keys(pin[2])
            self.driver.find_element(*getattr(self, '_set_pin_field_home_4_' + self.os)).send_keys(pin[3])
        self.driver.find_element(*getattr(self, '_enter_pwd_field_' + self.os)).send_keys(password)
        time.sleep(3)
        self.driver.find_element(*getattr(self, '_ok_button_' + self.os)).click()
        time.sleep(4)
        self.driver.find_element(*getattr(self, '_ok_button_' + self.os)).click()
        return self.exchange_page

    def dismiss_pin(self):
        ''' Method for dismissing PIN modal. '''
        from pages.exchange import ExchangePage
        self.exchange_page = ExchangePage(self.driver)
        self.driver.find_element(*getattr(self, '_enable_pin_no_tnx_button_' + self.os)).click()
        return self.exchange_page