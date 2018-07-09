class PinModal():
    '''
            This class contains element locators and action methods for the PIN modal
    '''

    def __init__(self, driver):
        super(PinModal, self).__init__(driver)
        self.os = str(self.driver.desired_capabilities['platformName']).lower()