from selenium.webdriver.common.by import By
from base.base_page import BasePage

class DashboardPage(BasePage):
    
    DASHBOARD_HERE = (By.XPATH, "//h6[contains(@class,'oxd-text--h6')]")
    
    def get_header_text(self):
        # Return the text of the dashboard header
        return self.find(self.DASHBOARD_HERE).text

    def is_displayed(self):
        # Return True if dashboard header is visible
        header = self.find(self.DASHBOARD_HERE)
        return header.is_displayed