from appium import webdriver
from nose.tools import assert_true

class TestLogin():

    # Set desired capabilities
    desired_caps = {}
    desired_caps['app'] = '/Users/majdukovic/Documents/MB_4_1_1.apk'
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
        self.driver.implicitly_wait(5)

    def test_01_login(self):
        # Execute test
        self.driver.find_element_by_id('com.matchbook.client:id/tvButton').click()
        self.driver.find_element_by_id('com.matchbook.client:id/loginButton').click()
        self.driver.find_element_by_id('com.matchbook.client:id/editTextUsername').click()
        self.driver.find_element_by_id('com.matchbook.client:id/editTextUsername').send_keys('majdukovic')
        self.driver.find_element_by_id('com.matchbook.client:id/editTextPassword').click()
        self.driver.find_element_by_id('com.matchbook.client:id/editTextPassword').send_keys('password1')
        self.driver.hide_keyboard()
        self.driver.find_element_by_id('com.matchbook.client:id/buttonLogIn').click()
        assert_true(self.driver.find_element_by_id('com.matchbook.client:id/activatePin').is_displayed(),
                    "'Activate PIN login' button is not displayed. User is not logged in.")
        print "User is logged in."

    def teardown(self):
        # Quit session
        self.driver.quit()
