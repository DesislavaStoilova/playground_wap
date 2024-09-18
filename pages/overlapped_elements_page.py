import allure
from selenium.common import NoSuchElementException
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.base_page import BasePage
from utils.locators import OverlappedElementPageLocators


class OverlappedElementPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)
        self.locators = OverlappedElementPageLocators()

    def wait_for_overlapped_element_header(self):
        try:
            WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located(self.locators.overlapped_element_header)
            )
        except TimeoutError as e:
            allure.attach(f"Timeout while waiting the Overlapped Element page to be loaded: {e}",
                          name="Overlapped Element Timeout",
                          attachment_type=allure.attachment_type.TEXT)
            raise

    def enter_id_and_name(self, id_input, name_input):
        try:
            self.set(locator=self.locators.overlapped_element_id_field, value=id_input)
            self.scroll(locator=self.locators.overlapped_element_scroll, scroll_amount=5)
            self.set(locator=self.locators.overlapped_element_name_field, value=name_input)
        except NoSuchElementException as e:
            allure.attach(f"Failed to find the element: {e}", name="Element Not Found",
                          attachment_type=allure.attachment_type.TEXT)
            raise

