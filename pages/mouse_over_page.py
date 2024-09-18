import allure
from selenium.common import NoSuchElementException
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.base_page import BasePage
from utils.locators import MouseOverPageLocators


class MouseOverPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)
        self.locators = MouseOverPageLocators()

    def wait_for_mouse_over_header(self):
        try:
            WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located(self.locators.mouse_over_header)
            )
        except TimeoutError as e:
            allure.attach(f"Timeout while waiting the Mouse over page to be loaded: {e}",
                          name="Mouse Over page Timeout",
                          attachment_type=allure.attachment_type.TEXT)
            raise

    def click_on_click_me_link(self, clicked_times):
        try:
            for _ in range(clicked_times):
                self.click(locator=self.locators.mouse_over_click_me_link)
        except NoSuchElementException as e:
            allure.attach(f"Failed to find the element: {e}", name="Element Not Found",
                          attachment_type=allure.attachment_type.TEXT)
            raise

    def get_the_click_me_clicked_number(self):
        clicked_number = self.get_text(locator=self.locators.mouse_over_click_me_clicked_numbers)
        return int(clicked_number)

    def click_on_link_button_link(self, clicked_times):
        try:
            for _ in range(clicked_times):
                self.click(locator=self.locators.mouse_over_link_button_link)
        except NoSuchElementException as e:
            allure.attach(f"Failed to find the element: {e}", name="Element Not Found",
                          attachment_type=allure.attachment_type.TEXT)
            raise

    def get_the_link_button_clicked_number(self):
        clicked_number = self.get_text(locator=self.locators.mouse_over_link_button_clicked_numbers)
        return int(clicked_number)
