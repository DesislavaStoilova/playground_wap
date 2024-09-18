import allure
from selenium.common import WebDriverException

from config.configuration import Configuration
from pages.base_page import BasePage
from pages.load_delay_page import LoadDelayPage
from pages.mouse_over_page import MouseOverPage
from pages.overlapped_elements_page import OverlappedElementPage
from pages.sample_app_page import SampleAppPage
from pages.text_input_page import TextInputPage
from utils.locators import HomePageLocators


class HomePage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)
        """Initialize BaseUrls and get the URL for the HomePage"""
        try:
            self.base_url = Configuration().get_ui_test_automation_playground_base_url()
        except FileNotFoundError as e:
            allure.attach(f"Error loading base URL from config: {e}", name="Config Load Error",
                          attachment_type=allure.attachment_type.TEXT)
            raise
        self.locators = HomePageLocators()

    def load(self):
        """Opens the HomePage using the base URL."""
        try:
            self.driver.get(self.base_url)
        except WebDriverException as e:
            allure.attach(f"Failed to load the page: {e}", name="Page Load Error",
                          attachment_type=allure.attachment_type.TEXT)
            raise

    def click_on_load_delay_menu(self):
        """Clicks the 'Load Delay' link on the HomePage."""
        try:
            self.click(locator=self.locators.load_delay_menu)
        except WebDriverException as e:
            allure.attach(f"Failed to click on Load Delay link: {e}", name="Click on Load Delay link Error",
                          attachment_type=allure.attachment_type.TEXT)
            raise
        return LoadDelayPage(self.driver)

    def click_on_sample_app_menu(self):
        """Clicks the 'Sample App' link on the HomePage."""
        try:
            self.click(locator=self.locators.sample_app_menu)
        except WebDriverException as e:
            allure.attach(f"Failed to click on Sample app link: {e}", name="Click on Sample App link Error",
                          attachment_type=allure.attachment_type.TEXT)
            raise
        return SampleAppPage(self.driver)

    def click_on_overlapped_element_menu(self):
        """Clicks the 'Overlapped Elements' link on the HomePage."""
        try:
            self.click(locator=self.locators.overlapped_elements_menu)
        except WebDriverException as e:
            allure.attach(f"Failed to click on Overlapped Element link: {e}",
                          name="Click on Overlapped Elements link Error",
                          attachment_type=allure.attachment_type.TEXT)
            raise
        return OverlappedElementPage(self.driver)

    def click_on_text_input_menu(self):
        """Clicks the 'Text Input' link on the HomePage."""
        try:
            self.click(locator=self.locators.text_input_menu)
        except WebDriverException as e:
            allure.attach(f"Failed to click on Text Input link: {e}",
                          name="Click on Text Input link Error",
                          attachment_type=allure.attachment_type.TEXT)
            raise
        return TextInputPage(self.driver)

    def click_on_mouse_over_menu(self):
        """Clicks the 'Mouse Over' link on the HomePage."""
        try:
            self.click(locator=self.locators.mouse_over_menu)
        except WebDriverException as e:
            allure.attach(f"Failed to click on Mouse Over link: {e}",
                          name="Click on Mouse Over link Error",
                          attachment_type=allure.attachment_type.TEXT)
            raise
        return MouseOverPage(self.driver)
