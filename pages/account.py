from appium.webdriver.common.mobileby import By
from appium.webdriver.common.mobileby import MobileBy
from pages.page import Page

class AccountPage(Page):
    '''
        This class contains element locators and action methods for the Account page
    '''

    def __init__(self, driver):
        super(AccountPage, self).__init__(driver)
        self.os = str(self.driver.desired_capabilities['platformName']).lower()


    #Android
    _logout_button_android = (By.ID, 'com.matchbook.client:id/menu_logout')
    # Casino bonus
    _your_casino_bonus_link_android = (By.ID, "com.matchbook.client:id/rlPendingBonus")
    # Fund
    _deposit_button_android = (By.ID, "com.matchbook.client:id/buttonDeposit_SW")
    _withdraw_button_android = (By.ID, "com.matchbook.client:id/buttonWithdraw_SW")
    # Settings
    _personal_settings_link_android = (By.ID, "com.matchbook.client:id/personalSettings")
    _account_settings_link_android = (By.ID, "com.matchbook.client:id/accountSettings")
    _display_settings_link_android = (By.ID, "com.matchbook.client:id/displaySettings")
    # Reports
    _current_bets_link_android = (By.ID, "com.matchbook.client:id/tvCurrentBets")
    _settled_bets_link_android = (By.ID, "com.matchbook.client:id/tvSettledEdgeBets")
    _transactions_link_android = (By.ID, "com.matchbook.client:id/tvTransactions")
    #Responsible gambling
    _responsible_gambling_link_android = (By.ID, "com.matchbook.client:id/tvResponsableGambling")

    # iOS
    # Casino bonus
    _your_casino_bonus_link_ios = (MobileBy.ACCESSIBILITY_ID, "SELECT YOUR BONUS")
    # Fund
    _deposit_button_ios = (MobileBy.ACCESSIBILITY_ID, "DEPOSIT")
    _withdraw_button_ios = (MobileBy.ACCESSIBILITY_ID, "WITHDRAW")
    # Settings
    _personal_settings_link_ios = (MobileBy.ACCESSIBILITY_ID, "Personal Settings")
    _account_settings_link_ios = (MobileBy.ACCESSIBILITY_ID, "Account Settings")
    _display_settings_link_ios = (MobileBy.ACCESSIBILITY_ID, "Display Settings")
    # Reports
    _current_bets_link_ios = (MobileBy.ACCESSIBILITY_ID, "Current Bets")
    _settled_bets_link_ios = (MobileBy.ACCESSIBILITY_ID, "Settled Bets")
    _transactions_link_ios = (MobileBy.ACCESSIBILITY_ID, "Transactions")
    # Responsible gambling
    _responsible_gambling_link_ios = (MobileBy.ACCESSIBILITY_ID, "Responsible Gambling")

    def logout(self):
        from pages.exchange import ExchangePage
        self.exchange_page = ExchangePage(self.driver)
        self.driver.find_element(*getattr(self, '_logout_button_' + self.os)).click()
        return self.exchange_page