import allure
import pytest
from pages.home_page import HomePage


@pytest.mark.BaseTest
@allure.title("Base Test")
@allure.description("Base test for initializing the HomePage in the setup")
@pytest.mark.critical
class BaseTest:
    @allure.step("Navigate to http://uitestingplayground.com/")
    @pytest.fixture(autouse=True)
    def test_open_home_page(self, browser):
        self.browser = browser

        # Initialize HomePage and open it
        self.home_page = HomePage(browser)
        self.home_page.load()

        # Verify that the current url is the expected url
        assert "http://uitestingplayground.com" in browser.current_url
