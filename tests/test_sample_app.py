import allure
import pytest

from tests.base_test import BaseTest


@pytest.mark.TestSampleApp
@allure.title("Test Sample App")
@allure.description("Tests for Sample App page")
@pytest.mark.normal
class TestSampleApp(BaseTest):
    @allure.step("Click on Sample App link"
                 "Wait till page is loaded")
    def test_click_on_sample_app_link(self):

        # Click on the "Load Delay" link
        sample_app = self.home_page.click_on_sample_app_menu()

        # Wait till page is loaded
        sample_app.wait_for_sample_app_header()

        # Verify that the current url is the expected url
        assert "http://uitestingplayground.com/sampleapp" in self.browser.current_url

    @allure.step("Login with valid credentials")
    def test_sample_app_login_with_valid_credentials(self):

        # Click on the "Load Delay" link
        sample_app = self.home_page.click_on_sample_app_menu()

        # Wait till page is loaded
        sample_app.wait_for_sample_app_header()

        username = "Testuser"
        password = "pwd"
        sample_app.login(username=username, password=password)
        assert sample_app.get_login_message() == f"Welcome, {username}!"

    @allure.step("Login with invalid credentials")
    def test_sample_app_login_with_invalid_credentials(self):

        # Click on the "Load Delay" link
        sample_app = self.home_page.click_on_sample_app_menu()

        # Wait till page is loaded
        sample_app.wait_for_sample_app_header()

        username = "Testuser"
        password = "password"
        sample_app.login(username=username, password=password)
        assert sample_app.get_login_message() == "Invalid username/password"
