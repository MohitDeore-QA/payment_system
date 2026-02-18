from datetime import datetime
import os
from selenium import webdriver
from pytest_metadata.plugin import metadata_key
import pytest
from utils.config_reader import Read_config
from pages.admin_login_page import AdminLoginPage


# ---------------- Browser Option ---------------- #

def pytest_addoption(parser):
    parser.addoption("--browser", action="store", default="chrome",
                     help="Options: chrome, firefox, edge")


# ---------------- Driver Fixture ---------------- #

@pytest.fixture()
def setup_driver(request):
    browser_name = request.config.getoption("--browser")

    if browser_name == "chrome":
        driver = webdriver.Chrome()
    elif browser_name == "firefox":
        driver = webdriver.Firefox()
    elif browser_name == "edge":
        driver = webdriver.Edge()
    else:
        driver = webdriver.Chrome()
        # we need to put error here - ("Browser value is not provided")

    driver.maximize_window()
    driver.implicitly_wait(10)

    yield driver

    print("\n--- Closing Browser ---")
    driver.quit()


# ---------------- Test Data Fixture ---------------- #

@pytest.fixture(scope="class")
def test_data():
    return {
        "url": Read_config.get_project_url(),
        "username": Read_config.get_username(),
        "password": Read_config.get_password(),
        "invalid_username": Read_config.get_invalid_username()
    }


# ---------------- Login Fixture ---------------- #

@pytest.fixture()
def login(setup_driver, test_data):
    driver = setup_driver
    driver.get(test_data["url"])

    login_page = AdminLoginPage(driver)
    login_page.login(test_data["username"], test_data["password"])

    return driver


# ---------------- Screenshot Hook ---------------- #

@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    rep = outcome.get_result()

    if rep.when == "call" and rep.failed:
        driver = item.funcargs.get("setup_driver")
        if driver:
            if not os.path.exists("screenshots"):
                os.makedirs("screenshots")

            file_name = f"fail_{item.name}_{datetime.now().strftime('%H%M%S')}.png"
            driver.save_screenshot(f"screenshots/{file_name}")


# ---------------- HTML Metadata ---------------- #

def pytest_configure(config):
    config.stash[metadata_key]["Project Name"] = "Banking Payment Project"
    config.stash[metadata_key]["Framework"] = "Hybrid Framework"
    config.stash[metadata_key]["Tech Stack"] = "Python-Selenium-POM-Pytest"


@pytest.mark.optionalhook
def pytest_metadata(metadata):
    metadata.pop("Packages", None)
