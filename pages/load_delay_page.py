import allure
from selenium.common import NoSuchElementException
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.base_page import BasePage
from utils.locators import LoadDelayPageLocators


class LoadDelayPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)
        self.locators = LoadDelayPageLocators()

    def wait_for_button_to_appear(self):
        try:
            WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable(self.locators.button_appearing_after_delay)
            )
        except TimeoutError as e:
            allure.attach(f"Timeout while waiting for button to appear: {e}", name="Button Timeout",
                          attachment_type=allure.attachment_type.TEXT)
            raise

    def click_on_button_appearing_after_delay(self):
        try:
            self.click(locator=self.locators.button_appearing_after_delay)
        except NoSuchElementException as e:
            allure.attach(f"Failed to find button: {e}", name="Button Not Found",
                          attachment_type=allure.attachment_type.TEXT)
            raise
