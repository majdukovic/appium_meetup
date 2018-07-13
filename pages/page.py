class Page(object):

    def __init__(self, driver):
        '''
            Constructor
        '''
        self.driver = driver

    def is_element_visible(self, *locator):
        '''
            Check if element is visible.
        '''
        try:
            return self.driver.find_element(*locator).is_displayed()
        except:
            return False