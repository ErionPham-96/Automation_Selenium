import pytest
from base.base_test import BaseTest
from pages.login_page import LoginPage
from config import USERNAME, PASSWORD

@pytest.mark.usefixtures("setup_driver")
class TestLogin(BaseTest):
    
    def test_valid_login(self):
        # Create a LoginPage object and pass the driver to interact with the browser
        lp = LoginPage(self.driver) 
        # Call the login() method, which enters username + password and clicks the login button
        dashboard = lp.login(USERNAME, PASSWORD)  
        # Assertion: verify that the dashboard is displayed after login
        assert dashboard.is_displayed() 
        # Print a success message with the dashboard header text
        print("Login successful! Checkpoint:", dashboard.get_header_text()) 
