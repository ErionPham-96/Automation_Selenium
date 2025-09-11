from selenium.webdriver.common.by import By
from base.base_page import BasePage

class AddVacanciesPage(BasePage):
    ADD_VACANCY_BUTTON = (By.XPATH, "//button[contains(@class,'oxd-button') and normalize-space()='Add']")
    
    def click_add_vacancy(self):
        # Click the "Add Vacancy" button
        self.click(self.ADD_VACANCY_BUTTON)
        
    def is_displayed(self):
            button = self.find(self.ADD_VACANCY_BUTTON)
            return button.is_displayed()