import pytest
from from base.base_page import BasePage
from base.base_test import BaseTest
from pages.login_page import LoginPage
from config import USERNAME, PASSWORD
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

@pytest.mark.usefixtures("setup_driver")
class TestLogin(BaseTest):
    
    def test_login(self):
        lp = LoginPage(self.driver)
        lp.login(USERNAME, PASSWORD)
        WebDriverWait(self.driver, 10).until(EC.url_contains("/dashboard"))
        assert "dashboard" in self.driver.current_url