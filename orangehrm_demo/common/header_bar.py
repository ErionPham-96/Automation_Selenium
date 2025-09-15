from base.base_page import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

class HeaderBar(BasePage):
    
    PROFILE_NAME = (By.XPATH, "//p[contains(@class, 'oxd-userdropdown-name')]")
    
    def get_profile_name(self):
        profile_name = self.wait.until(EC.visibility_of_element_located(self.PROFILE_NAME))
        return profile_name.text.strip()