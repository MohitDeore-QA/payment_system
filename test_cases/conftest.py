import pytest
from selenium import webdriver
from pytest_metadata.plugin import metadata_key #for customize html report

def pytest_addoption(parser):
    parser.addoption("--browser", action="store", default="chrome",help="specify the browser: chrome or firefox or edge")

@pytest.fixture()
def browser(request):
    return request.config.getoption("--browser")

@pytest.fixture()
def setup_driver(browser):
    global driver
    if browser == "chrome":
        driver = webdriver.Chrome()
    elif browser == "firefox":
        driver = webdriver.Firefox()
    elif browser == "edge":
        driver = webdriver.Edge()
    else:
        raise ValueError("browser must be 'chrome' or 'firefox'")
    return driver

###################################### for adding custom parameters to change or customize the html report

def pytest_configure(config):
    config.stash[metadata_key] ["Project Name"]="Banking Payment Project"
    config.stash[metadata_key] ["Test Module Name"]="Customer Login Test"
    config.stash[metadata_key] ["Assignee QA"]="Mohit"
    config.stash[metadata_key] ["Framework Type"]="Hybrid Framework"
    config.stash[metadata_key] ["Tech Used"]="Python-Selenium-POM-Pytest"

#hook for delete modify environment info in html report
@pytest.mark.optionalhook
def pytest_metadata(metadata):
    metadata.pop('Packages',None)

