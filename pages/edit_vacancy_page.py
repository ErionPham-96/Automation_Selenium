from base.base_page import BasePage
from vacancies_page import VacanciesPage
from selenium.webdriver.common.by import By

class EditVacancyPage(BasePage):
    
    CANCEL_BTN = (By.XPATH, "//button[@type='button' and normalize-space()='Cancel']")
    
    def cancel_edit(self):
        self.click(self.CANCEL_BTN)
        return VacanciesPage(self.driver)