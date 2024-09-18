import allure
import pytest
from tests.base_test import BaseTest


@pytest.mark.TestLoadDelay
@allure.title("Test Load Delay")
@allure.description("Tests for Overlapped Element page")
@pytest.mark.normal
class TestLoadDelay(BaseTest):
    @allure.step("Click on Load Delay link"
                 "Wait till the page is loaded"
                 "Click on Button Appearing After Delay")
    def test_click_on_load_delay_link(self):
        # Click on the "Load Delay" link
        load_delay_page = self.home_page.click_on_load_delay_menu()

        # Wait for the button and click it
        load_delay_page.wait_for_button_to_appear()
        load_delay_page.click_on_button_appearing_after_delay()

        # Verify that the current url is the expected url
        assert "http://uitestingplayground.com/loaddelay" in self.browser.current_url
