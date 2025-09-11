from selenium.webdriver.common.by import By
from base.base_page import BasePage

class VacanciesPage(BasePage):
    
    VACANCIES_HERE = (By.XPATH, "//a[contains(@class,'oxd-topbar-body-nav-tab-item') and normalize-space()='Vacancies']")
    
    def get_header_text(self):
        # Return the text of the vacancies header
        return self.find(self.VACANCIES_HERE).text
    def is_displayed(self):
        # Return True if vacancies header is visible
        header = self.find(self.VACANCIES_HERE)
        return header.is_displayed()
        