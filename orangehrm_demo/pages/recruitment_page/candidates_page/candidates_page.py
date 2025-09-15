from selenium.webdriver.common.by import By
from base.base_page import BasePage

class CandidatesPage(BasePage):
    
    CANDIDATES_HERE = (By.XPATH, "//a[contains(@class, 'oxd-topbar-body-nav-tab-item') and normalize-space() = 'Candidates']")
    
    def click_candidates_here(self):
        self.click(self.CANDIDATES_HERE)
    def get_header_text(self):
        return self.find(self.CANDIDATES_HERE).text
    def is_displayed(self):
        header = self.find(self.CANDIDATES_HERE)
        return header.is_displayed()