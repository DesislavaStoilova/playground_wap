import allure
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from config.configuration import Configuration


def get_driver():
    chrome_options = webdriver.ChromeOptions()

    # Enable mobile emulation for the selected device
    device = Configuration().get_device_name()
    mobile_emulation = {
        "deviceName": device
    }

    chrome_options.add_experimental_option("mobileEmulation", mobile_emulation)

    chrome_options.add_experimental_option("excludeSwitches", ["enable-automation"])
    chrome_options.add_argument("--disable-popup-blocking")
    chrome_options.add_argument("--disable-search-engine-choice-screen")
    chrome_options.add_argument("--no-default-browser-check")

    # Initialize Chrome WebDriver with options
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)
    driver.maximize_window()
    return driver


@allure.step("Browser setup and teardown")
@pytest.fixture(scope="function")
def browser():
    driver = get_driver()
    yield driver
    driver.quit()
