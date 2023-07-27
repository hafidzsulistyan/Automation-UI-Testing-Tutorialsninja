from pages.BasePage import BasePage


class AccountSuccessPage(BasePage):
    account_creation_message_xpath = "//div[@id='content']/h1"

    def __init__(self, driver):
        super().__init__(driver)

    def retrieve_account_creation_message(self):
        return self.retrieve_element_text("account_creation_message_xpath", self.account_creation_message_xpath)
