import pytest
from selenium import webdriver


@pytest.fixture(scope="session")
def browser():
    driver = webdriver.Chrome()
    driver.set_window_size(2000, 2000)
    yield driver
    driver.quit()



