import allure
import pytest

from tests.base_test import BaseTest


@pytest.mark.TestMouseOver
@allure.title("Test Mouse Over")
@allure.description("Tests for Mouse Over page")
@pytest.mark.normal
class TestMouseOver(BaseTest):
    @allure.step("Click on Mouse Over link"
                 "Wait till page is loaded")
    def test_click_on_mouse_over_link(self):
        # Click on the "Mouse Over" link
        mouse_over = self.home_page.click_on_mouse_over_menu()

        # Wait till page is loaded
        mouse_over.wait_for_mouse_over_header()

        # Verify that the current url is the expected url
        assert "http://uitestingplayground.com/mouseover" in self.browser.current_url

    @allure.step("Click on Click Me link 2 times"
                 "Verify the number of clicked times")
    def test_click_on_click_me_link(self):
        # Click on the "Mouse Over" link
        mouse_over = self.home_page.click_on_mouse_over_menu()

        # Wait till page is loaded
        mouse_over.wait_for_mouse_over_header()
        # Click on click me link 2 times
        number_of_clicked_times = 2
        mouse_over.click_on_click_me_link(clicked_times=number_of_clicked_times)
        # Verify the number of clicked times
        assert mouse_over.get_the_click_me_clicked_number() == number_of_clicked_times

    @allure.step("Click on Link Button link 2 times"
                 "Verify the number of clicked times")
    def test_click_on_link_button_link(self):
        # Click on the "Mouse Over" link
        mouse_over = self.home_page.click_on_mouse_over_menu()

        # Wait till page is loaded
        mouse_over.wait_for_mouse_over_header()
        # Click on Link button link 2 times
        number_of_clicked_times = 2
        mouse_over.click_on_link_button_link(clicked_times=number_of_clicked_times)
        # Verify the number of clicked times
        assert mouse_over.get_the_link_button_clicked_number() == number_of_clicked_times
