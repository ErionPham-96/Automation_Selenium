import pytest
from base.base_test import BaseTest
from pages.login_page import LoginPage

@pytest.mark.usefixtures("setup_driver")
class TestLogin(BaseTest):
    
    def test_valid_login(self):
        lp = LoginPage(self.driver) 
        dashboard = lp.login(self.config["username"], self.config["password"])  
        
        # Assertion: verify that the dashboard is displayed after login
        assert dashboard.is_displayed() 
        # Print a success message with the dashboard header text
        print("Login successful! Checkpoint:", dashboard.get_header_text()) 
