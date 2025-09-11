from selenium.webdriver.common.by import By
from base.base_page import BasePage

class RecruitmentPage(BasePage):
    
    RECRUITMENT_HERE = (By.XPATH, "//a[contains(@href,'recruitment/viewRecruitmentModule')]")
    
    # Action: Click on Recruitment menu
    def click_recruitment_menu(self):
        self.click(self.RECRUITMENT_HERE)