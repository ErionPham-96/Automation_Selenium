from selenium import webdriver
import time
from selenium.webdriver.common.by import By
import pytest

class BaseTest:
    @pytest.fixture(scope="class", autouse=True)
    def setup_driver(self, request):
        driver = webdriver.Chrome()
        driver.maximize_window()
        driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
        time.sleep(3)
        request.cls.driver = driver
        yield
        driver.quit()
        