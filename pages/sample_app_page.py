import allure
from selenium.common import NoSuchElementException
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.base_page import BasePage
from utils.locators import SampleAppPageLocators


class SampleAppPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)
        self.locators = SampleAppPageLocators()

    def wait_for_sample_app_header(self):
        try:
            WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located(self.locators.sample_app_header)
            )
        except TimeoutError as e:
            allure.attach(f"Timeout while waiting the Sample App page to be loaded: {e}", name="Sample App Timeout",
                          attachment_type=allure.attachment_type.TEXT)
            raise

    def login(self, username, password):
        try:
            self.set(locator=self.locators.sample_app_user_name_field, value=username)
            self.set(locator=self.locators.sample_app_password_field, value=password)
            self.click(locator=self.locators.sample_app_login_button)
        except NoSuchElementException as e:
            allure.attach(f"Failed to find the element: {e}", name="Element Not Found",
                          attachment_type=allure.attachment_type.TEXT)
            raise

    def get_login_message(self):
        login_message = self.get_text(locator=self.locators.sample_app_loginstatus)
        return login_message

