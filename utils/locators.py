from selenium.webdriver.common.by import By


class HomePageLocators:
    load_delay_menu = (By.LINK_TEXT, "Load Delay")
    sample_app_menu = (By.LINK_TEXT, "Sample App")
    overlapped_elements_menu = (By.LINK_TEXT, "Overlapped Element")
    text_input_menu = (By.LINK_TEXT, "Text Input")
    mouse_over_menu = (By.LINK_TEXT, "Mouse Over")


class LoadDelayPageLocators:
    button_appearing_after_delay = (By.XPATH, "//button[text()='Button Appearing After Delay']")


class SampleAppPageLocators:
    sample_app_header = (By.XPATH, "/html/body/section/div/h3")
    sample_app_user_name_field = (By.NAME, "UserName")
    sample_app_password_field = (By.NAME, "Password")
    sample_app_login_button = (By.ID, "login")
    sample_app_loginstatus = (By.ID, "loginstatus")


class OverlappedElementPageLocators:
    overlapped_element_header = (By.XPATH, "/html/body/section/div/h3")
    overlapped_element_id_field = (By.ID, "id")
    overlapped_element_name_field = (By.ID, "name")
    overlapped_element_scroll = (By.XPATH, "/ html / body / section / div / div / div[1]")


class TextInputPageLocators:
    text_input_header = (By.XPATH, "/html/body/section/div/h3")
    text_input_my_button_field = (By.ID, "newButtonName")
    text_input_button_that_should_change_name = (By.ID, "updatingButton")


class MouseOverPageLocators:
    mouse_over_header = (By.XPATH, "/html/body/section/div/h3")
    mouse_over_click_me_link = (By.LINK_TEXT, "Click me")
    mouse_over_click_me_clicked_numbers = (By.ID, "clickCount")
    mouse_over_link_button_link = (By.LINK_TEXT, "Link Button")
    mouse_over_link_button_clicked_numbers = (By.ID, "clickButtonCount")

