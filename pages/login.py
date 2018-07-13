# -*- coding: utf-8 -*-
from appium.webdriver.common.mobileby import By, MobileBy
from pages.page import Page


class LoginPage(Page):
    '''
           This class contains element locators and action methods for the Login page
    '''

    def __init__(self, driver):
        super(LoginPage, self).__init__(driver)
        self.os = str(self.driver.desired_capabilities['platformName']).lower()

    # Login page Android
    _username_field_android = (By.ID, 'com.matchbook.client:id/editTextUsername')
    _password_field_android = (By.ID, 'com.matchbook.client:id/editTextPassword')
    _login_button_android = (By.ID, 'com.matchbook.client:id/buttonLogIn')
    _forgot_password_link_android = (By.ID, 'com.matchbook.client:id/forgotPwd')
    _join_now_button_android = (By.ID, 'com.matchbook.client:id/btnViewReg')
    _enter_pin_login_android = (By.ID, 'com.matchbook.client:id/pin1')

    _incorrect_username_actual_message_android = (By.ID, 'android:id/message')
    _incorrect_password_actual_message_android = (By.ID, 'android:id/message')
    _incorrect_username_expected_message_android = 'Cannot login, username or password is incorrect, please contact Customer Service for assistance.'
    _incorrect_password_expected_message_android = 'Attempts left'
    _incorrect_credentials_dialog_ok_button_android = (By.ID, 'android:id/button1')

    # Login page iOS
    _username_field_populated = (By.XPATH,
                                 '//XCUIElementTypeApplication[@name="Matchbook"]/XCUIElementTypeWindow[1]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeScrollView/XCUIElementTypeOther/XCUIElementTypeOther[1]/XCUIElementTypeTextField')
    # _username_field_empty = (MobileBy.ACCESSIBILITY_ID, 'Username')
    _username_field_empty = (By.XPATH, '//XCUIElementTypeStaticText[@name="Username"]')
    _password_field_ios = (By.NAME, 'Password')
    _login_button_ios = (By.NAME, 'LOGIN')
    _forgot_password_link_ios = (By.NAME, 'Forgot Password?')
    _join_now_button_ios = (By.NAME, 'JOIN NOW')
    _delete_button = (MobileBy.ACCESSIBILITY_ID, 'delete')
    _select_all_button = (MobileBy.ACCESSIBILITY_ID, 'Select All')

    _incorrect_username_actual_message_ios = (
    By.NAME, 'Cannot login, username or password is incorrect, please contact Customer Service for assistance.')
    _incorrect_password_actual_message_ios = (By.NAME,
                                              'Cannot login, username or password is incorrect, please contact Customer Service for assistance. Attempts left: 2.')
    _incorrect_username_expected_message_ios = 'Cannot login, username or password is incorrect, please contact Customer Service for assistance.'
    _incorrect_password_expected_message_ios = 'Attempts left'
    _incorrect_credentials_dialog_ok_button_ios = (By.NAME, 'OK')

    def login_with_credentials(self, username, password):
        ''' Method for logging in with credentials.
                @param username: string - Username provided will be used while logging in
                @param password: string - Password provided will be used while logging in
        '''
        from pages.exchange import ExchangePage
        self.exchange_page = ExchangePage(self.driver)
        if self.os == 'android':
            self.driver.find_element(*getattr(self, '_username_field_' + self.os)).send_keys(username)
        elif self.os == 'ios':
            ''' 
                For iOS we need to check if 'username' field is empty or not. If user logged in before, 'username' field will be populated.
                If 'username' field is empty then enter username, else delete content and enter username
            '''
            if not self.driver.find_element(*self._username_field_populated).is_displayed():
                self.driver.find_element(*self._username_field_empty).send_keys(username)
            else:
                self.driver.find_element(*self._username_field_populated).click()
                self.driver.find_element(*self._username_field_populated).click()
                self.driver.find_element(*self._select_all_button).click()
                self.driver.find_element(*self._delete_button).click()
                self.driver.find_element(*self._username_field_populated).send_keys(username)
        self.driver.find_element(*getattr(self, '_password_field_' + self.os)).send_keys(password)
        try:
            self.driver.hide_keyboard()
        except:
            pass
        self.driver.find_element(*getattr(self, '_login_button_' + self.os)).click()
        return self.exchange_page

    def login_with_pin(self, pin):
        ''' Method for logging in with PIN.
                @param pin: string - pin provided will be used while logging in
        '''
        if self.os == 'android':
            self.driver.find_element(*getattr(self.login_page, '_enter_pin_login_' + self.os)).send_keys(pin)
        elif self.os == 'ios':
            self.driver.find_element(*getattr(self, '_enter_pin_field_1_' + self.os)).send_keys(pin[0])
            self.driver.find_element(*getattr(self, '_enter_pin_field_2_' + self.os)).send_keys(pin[1])
            self.driver.find_element(*getattr(self, '_enter_pin_field_3_' + self.os)).send_keys(pin[2])
            self.driver.find_element(*getattr(self, '_enter_pin_field_4_' + self.os)).send_keys(pin[3])
        return self.exchange_page