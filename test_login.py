from appium import webdriver
from nose.tools import assert_true
import time

class TestLogin():

    # Set desired capabilities
    desired_caps = {}
    desired_caps['app'] = 'app_location' #change (credentials.txt)
    desired_caps['platformName'] = 'Android'
    desired_caps['platformVersion'] = '7.0'
    desired_caps['deviceName'] = 'Samsung Galaxy S8'
    desired_caps['appWaitPackage'] = 'com.matchbook.client'
    desired_caps['appWaitActivity'] = 'com.android.xanadu.matchbook.MainActivity'
    desired_caps['autoGrantPermissions'] = True
    desired_caps['browserstack.idleTimeout'] = '10'

    def setup(self):
        # Start webdriver
        self.driver = webdriver.Remote('server_location', self.desired_caps) #change (credentials.txt)
        self.driver.implicitly_wait(10)

    def test_01_login(self):
        # Execute test
        self.driver.find_element_by_id('com.matchbook.client:id/tvButton').click()
        #time.sleep(2)
        self.driver.find_element_by_id('com.matchbook.client:id/loginButton').click()
        #time.sleep(2)
        self.driver.find_element_by_id('com.matchbook.client:id/editTextUsername').click()
        self.driver.find_element_by_id('com.matchbook.client:id/editTextUsername').send_keys('majdukovic')
        self.driver.find_element_by_id('com.matchbook.client:id/editTextPassword').click()
        #time.sleep(1)
        self.driver.find_element_by_id('com.matchbook.client:id/editTextPassword').send_keys('lozinka1')
        self.driver.hide_keyboard()
        #time.sleep(2)
        self.driver.find_element_by_id('com.matchbook.client:id/buttonLogIn').click()
        #time.sleep(2)
        self.driver.find_element_by_id('com.matchbook.client:id/activatePin').click()
        self.driver.find_element_by_id('com.matchbook.client:id/pin1').send_keys('1111')
        #time.sleep(1)
        self.driver.find_element_by_id('com.matchbook.client:id/pin1').send_keys('1111')
        #time.sleep(2)
        self.driver.find_element_by_id('com.matchbook.client:id/pinPwd').click()
        self.driver.find_element_by_id('com.matchbook.client:id/pinPwd').send_keys('lozinka1')
        #time.sleep(2)
        self.driver.find_element_by_id('com.matchbook.client:id/okButton').click()
        #time.sleep(2)
        self.driver.find_element_by_id('com.matchbook.client:id/okButton').click()
        #time.sleep(1)
        self.driver.find_element_by_id('com.matchbook.client:id/ivAccount').click()
        self.driver.find_element_by_id('com.matchbook.client:id/ivLogout').click()
        self.driver.find_element_by_id('com.matchbook.client:id/loginButton').click()
        self.driver.find_element_by_id('com.matchbook.client:id/pin1').send_keys('1111')
        assert_true(self.driver.find_element_by_id('com.matchbook.client:id/ivAccount').is_displayed(),
        "Account button is not displayed, user is not logged in.")
        print "User is logged in with PIN."
        time.sleep(2)

    def teardown(self):
        # Quit session
        self.driver.quit()
