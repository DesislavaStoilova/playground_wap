import allure
from selenium.common import NoSuchElementException
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.base_page import BasePage
from utils.locators import TextInputPageLocators


class TextInputPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)
        self.locators = TextInputPageLocators()

    def wait_for_text_input_header(self):
        try:
            WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located(self.locators.text_input_header)
            )
        except TimeoutError as e:
            allure.attach(f"Timeout while waiting the Text Input page to be loaded: {e}", name="Text Input Timeout",
                          attachment_type=allure.attachment_type.TEXT)
            raise

    def set_new_button_name(self, new_name):
        try:
            self.set(locator=self.locators.text_input_my_button_field, value=new_name)
            self.click(locator=self.locators.text_input_button_that_should_change_name)
        except NoSuchElementException as e:
            allure.attach(f"Failed to find the element: {e}", name="Element Not Found",
                          attachment_type=allure.attachment_type.TEXT)
            raise

    def get_button_name_after_update(self):
        text_input_button_name_after_update = self.get_text(locator=self.locators.text_input_button_that_should_change_name)
        return text_input_button_name_after_update

