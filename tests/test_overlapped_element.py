import allure
import pytest

from tests.base_test import BaseTest


@pytest.mark.TestOverlappedElement
@allure.title("Test Overlapped Element")
@allure.description("Tests for Overlapped Element page")
@pytest.mark.normal
class TestOverlappedElement(BaseTest):
    @allure.step("Click on Overlapped Element link"
                 "Wait till page is loaded")
    def test_click_on_overlapped_element_link(self):
        # Click on the "Load Delay" link
        overlapped_element = self.home_page.click_on_overlapped_element_menu()

        # Wait till page is loaded
        overlapped_element.wait_for_overlapped_element_header()

        # Verify that the current url is the expected url
        assert "http://uitestingplayground.com/overlapped" in self.browser.current_url

    @allure.description("After loading the Overlapped Element page:"
                        "Enter an id input"
                        "Scroll till the name field is visible"
                        "Enter a name input")
    def test_enter_id_and_name(self):

        # Click on the "Load Delay" link
        overlapped_element = self.home_page.click_on_overlapped_element_menu()

        # Wait till page is loaded
        overlapped_element.wait_for_overlapped_element_header()

        # Verify that the current url is the expected url
        assert "http://uitestingplayground.com/overlapped" in self.browser.current_url

        overlapped_element.enter_id_and_name(id_input="123", name_input="TestTest")
