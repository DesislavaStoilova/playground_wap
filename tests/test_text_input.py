import allure
import pytest

from tests.base_test import BaseTest


@pytest.mark.TestOverlappedElement
@allure.title("Test Overlapped Element")
@allure.description("Tests for Overlapped Element page")
@pytest.mark.normal
class TestTextInput(BaseTest):
    @allure.step("Click on Text Input link"
                 "Wait till page is loaded")
    def test_click_on_text_input_link(self):
        # Click on the "Load Delay" link
        text_input = self.home_page.click_on_text_input_menu()

        # Wait till page is loaded
        text_input.wait_for_text_input_header()
        # Verify that the current url is the expected url
        assert "http://uitestingplayground.com/textinput" in self.browser.current_url

    @allure.step("After loading the Text Input page:"
                 "Locate the MyButton input field"
                 "Set a new name"
                 "Check the new button name")
    def test_set_new_button_name(self):
        # Click on the "Load Delay" link
        text_input = self.home_page.click_on_text_input_menu()

        # Wait till page is loaded
        text_input.wait_for_text_input_header()
        # Set a button's new name
        new_name = "Button's new name"
        text_input.set_new_button_name(new_name=new_name)

        # Verify the new button's name
        assert text_input.get_button_name_after_update() == new_name
