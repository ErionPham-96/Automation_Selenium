from selenium.webdriver.common.by import By
from base.base_page import BasePage
from pages.dashboard_page import DashboardPage
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
class LoginPage(BasePage):
    USERNAME = (By.NAME, "username")
    PASSWORD = (By.NAME, "password")
    LOGIN_BUTTON = (By.XPATH, "//button[@type='submit']")
    
    def login(self, username, password):
        self.type(self.USERNAME, username)
        self.type(self.PASSWORD, password)
        self.click(self.LOGIN_BUTTON)
        WebDriverWait(self.driver, 10).until(
            EC.url_contains("/dashboard")
        )
        # Return an object after logining successful
        assert "dashboard" in self.driver.current_url
        return DashboardPage(self.driver)