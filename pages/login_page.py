from selenium.webdriver.common.by import By
from base.base_page import BasePage
from pages.dashboard_page import DashboardPage

class LoginPage(BasePage):
    USERNAME = (By.NAME, "username")
    PASSWORD = (By.NAME, "password")
    LOGIN_BUTTON = (By.XPATH, "//button[@type='submit']")
    
    def login(self, username, password):
        self.type(self.USERNAME, username)
        self.type(self.PASSWORD, password)
        self.click(self.LOGIN_BUTTON)
        # Return an object after logining successful
        return DashboardPage(self.driver)