import pytest
from selenium import webdriver
from utilities import ReadConfig as Configs


@pytest.fixture()
def setup_and_teardown(request):
    browser = Configs.read_configuration("common info", "browser")
    driver = None
    if browser.__eq__("chrome"):
        driver = webdriver.Chrome()
    elif browser.__eq__("firefox"):
        driver = webdriver.Firefox()
    elif browser.__eq__("edge"):
        driver = webdriver.Edge()
    else:
        print("Provide a valid browser name from this list [Chrome/Firefox/Edge]")

    request.cls.driver = driver
    driver.maximize_window()
    app_url = Configs.read_configuration("common info", "url")
    driver.get(app_url)
    yield
    driver.quit()
