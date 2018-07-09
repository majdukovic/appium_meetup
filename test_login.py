from appium import webdriver
from nose.tools import assert_true
import time

class TestLogin():

    # Set desired capabilities
    desired_caps = {}
    desired_caps['app'] = '/Users/majdukovic/Documents/MB_4_1_1_app.apk'
    desired_caps['platformName'] = 'Android'
    desired_caps['platformVersion'] = '7.0'
    desired_caps['deviceName'] = 'Galaxy Nexus 7.0'
    desired_caps['avd'] = 'Galaxy_Nexus_7.0'
    desired_caps['appWaitPackage'] = 'com.matchbook.client'
    desired_caps['appWaitActivity'] = 'com.android.xanadu.matchbook.MainActivity'
    desired_caps['autoGrantPermissions'] = True

    def setup(self):
        # Start webdriver
        self.driver = webdriver.Remote('http://localhost:4723/wd/hub', self.desired_caps)
        self.driver.implicitly_wait(10)

    def test_01_login(self):
        # Execute test
        time.sleep(5)
        self.driver.find_element_by_id('com.matchbook.client:id/tvButton').click()
        time.sleep(3)
        self.driver.find_element_by_id('com.matchbook.client:id/loginButton').click()
        time.sleep(2)
        self.driver.find_element_by_id('com.matchbook.client:id/editTextUsername').click()
        self.driver.find_element_by_id('com.matchbook.client:id/editTextUsername').send_keys('username')
        self.driver.find_element_by_id('com.matchbook.client:id/editTextPassword').click()
        time.sleep(1)
        self.driver.find_element_by_id('com.matchbook.client:id/editTextPassword').send_keys('password')
        self.driver.hide_keyboard()
        time.sleep(2)
        self.driver.find_element_by_id('com.matchbook.client:id/buttonLogIn').click()
        time.sleep(10)
        self.driver.find_element_by_id('com.matchbook.client:id/activatePin').click()
        self.driver.find_element_by_id('com.matchbook.client:id/pin1').send_keys('1111')
        time.sleep(1)
        self.driver.find_element_by_id('com.matchbook.client:id/pin1').send_keys('1111')
        time.sleep(2)
        self.driver.find_element_by_id('com.matchbook.client:id/pinPwd').click()
        self.driver.find_element_by_id('com.matchbook.client:id/pinPwd').send_keys('password')
        time.sleep(2)
        self.driver.find_element_by_id('com.matchbook.client:id/okButton').click()
        time.sleep(8)
        self.driver.find_element_by_id('com.matchbook.client:id/okButton').click()
        time.sleep(1)
        assert_true(self.driver.find_element_by_id('com.matchbook.client:id/ivAccount').is_displayed(),
        "Account button is not displayed, user is not logged in.")
        print "User is logged in."
        time.sleep(5)

    def teardown(self):
        # Quit session
        self.driver.quit()
