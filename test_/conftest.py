import pytest
from selenium import webdriver

@pytest.fixture
def driver_setup():
    opt = webdriver.ChromeOptions()
    opt.add_experimental_option('detach', True)
    driver = webdriver.Chrome(options=opt)
    driver.maximize_window()
    driver.get('https://demowebshop.tricentis.com/')
    yield driver
    driver.quit()
