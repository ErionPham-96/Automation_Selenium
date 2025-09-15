from selenium.webdriver.common.by import By
from base.base_page import BasePage


class LoginPage(BasePage):
    
    EMAIL_FLIED = (By.XPATH, "//input//[@name = 'email']")
    PASSWORD_FLIED = (By.XPATH, "//input//[@name = 'password']")
    LOGIN_BUTTON = (By.XPATH, "//button[@type='submit']")
    TOGGLE_BUTTON = (By.XPATH, "//i[contains(@class,'password-toggle')]")
    DASHBOARD_HERE = (By.XPATH, "//div[contains(@class,'aiz-topbar')]//a[normalize-space()='Dashboard']")
    
    def toggle_password(self, show = True):
        element = self.find(self.PASSWORD_FLIED)
        current_type = element.get_attribute("type")
        if (show and current_type == "password"):
            self.click(self.TOGGLE_BUTTON)
        elif (not show and current_type == "text"):
            self.click(self.TOGGLE_BUTTON)
            
    def login(self, email, password):
        email = self.type(self.EMAIL_FLIED, email)
        password = self.type(self.PASSWORD_FLIED, password)
        self.click(self.LOGIN_BUTTON)