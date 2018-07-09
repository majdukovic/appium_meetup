from appium import webdriver
from testconfig import config
import time
from appium.webdriver.common.mobileby import By

class BaseTest(object):
    '''
        This class deals with starting Appium server and setting the Matchbook app to the initial state
    '''

    _privacy_policy_accept_button_android = (By.ID, 'com.matchbook.client:id/tvButton')
    _exchange_button_android = (By.ID, 'com.matchbook.client:id/action_exchange')
    _exchange_button_ios = (By.ID, 'com.matchbook.client:id/action_exchange')

    def setUp(self):
        '''
            Set up method, executed at the beginning of every test case.
            User should be on the Exchange tab if method is executed successfully
        '''
        self.driver = webdriver.Remote(config['server_url'], config['device_config'])
        self.driver.implicitly_wait(15)
        self.os = str(self.driver.desired_capabilities['platformName']).lower()
        if self.os == 'android':
            try:
                self.driver.find_element(*self._privacy_policy_accept_button_android).click()
            except:
                try:
                    self.driver.find_element(*self._exchange_button_android).click()
                except:
                    print "Exchange button is not visible"
        else:
            time.sleep(5)
            try:
                self.driver.switch_to.alert.accept()
            except:
                print "Unable to switch and accept alert"
                try:
                    self.driver.find_element(*self._exchange_button_ios).click()
                except:
                    print "Exchange button is not visible"

    def tearDown(self):
        self.driver.quit()
