from selenium.webdriver.common.by import By
from base.base_page import BasePage
from selenium.webdriver.common.keys import Keys
from selenium.webdriver import ActionChains
from common.header_bar import HeaderBar
class AddVacancyPage(BasePage):
    
    # Static locators:
    ADD_VACANCY_BUTTON = (By.XPATH, "//button[contains(@class,'oxd-button') and normalize-space()='Add']")
    
    VACANCY_NAME_FIELD = (By.XPATH, "//label[contains(text(), 'Vacancy Name')]"
                          "/ancestor::div[contains(@class, 'oxd-grid-item')]"
                          "//input[contains(@class, 'oxd-input') and contains(@class, 'oxd-input--active')]"
    )
    
    JOB_TITLE_DROPDOWN = (By.XPATH, "//i[contains(@class, 'oxd-icon bi-caret-down-fill oxd-select-text--arrow')]")
    DESCRIPTION_FIELD = (By.XPATH, "//textarea[contains(@placeholder, 'Type description here')]")
    HIRING_MANAGER_FIELD = (By.XPATH, "//div[contains(@class,'oxd-autocomplete-text-input')]//input")
    
    NUMBER_OF_POSITIONS_FIELD = (By.XPATH, "//label[contains(text(), 'Number of Positions')]"
                                 "/ancestor::div[contains(@class, 'oxd-grid-item')]"
                                 "//input"
    )
    
    ACTIVE_CHECKBOX = (By.XPATH, "//p[normalize-space()='Active']/ancestor::div[contains(@class,'oxd-grid-item')]//input[@type='checkbox']")
    PUBLISH_CHECKBOX = (By.XPATH, "//p[normalize-space()='Publish in RSS Feed and Web Page']/ancestor::div[contains(@class,'oxd-grid-item')]//input[@type='checkbox']")
    
    SAVE_BUTTON = (By.XPATH, "//button[@type='submit' and normalize-space()='Save']")
    CANCEL_BUTTON = (By.XPATH, "//button[@type='button' and normalize-space()='Cancel']")
    
    def click_add_vacancy(self):
        # Click the "Add Vacancy" button
        self.click(self.ADD_VACANCY_BUTTON)
        
    def is_displayed(self):
        button = self.find(self.ADD_VACANCY_BUTTON)
        return button.is_displayed()
    
    def job_title_option(self, job_title : str):
        # Locator for job title option in dropdown
        return (
            By.XPATH, 
            f"//div[contains(@class,'oxd-select-option')][normalize-space()='{job_title}']"
        )
    
    def hiring_manager_option(self, name: str):
        return (
            By.XPATH,
            f"//div[contains(@class,'oxd-autocomplete-dropdown')]//div[normalize-space()='{name}']"
        )
    
    def fill_hiring_manager(self, profile_name):
        
        self.type(self.HIRING_MANAGER_FIELD, profile_name)
        actions = ActionChains(self.driver)
        actions.send_keys(Keys.ARROW_DOWN).send_keys(Keys.ENTER).perform()
    
    def fill_vacancy_form(self, data):
        
        # Fill in the vacancy form
        self.type(self.VACANCY_NAME_FIELD, str(data['vacancy_name']))
        
        # Select job title from dropdown
        self.click(self.JOB_TITLE_DROPDOWN)
        self.scroll_and_click(self.job_title_option(data["job_title"]))
        
        # Fill in description
        self.type(self.DESCRIPTION_FIELD, data['description'])
        
        # Fill in hiring manager
        header_bar = HeaderBar(self.driver)
        profile_name = header_bar.get_profile_name()
        self.fill_hiring_manager(profile_name)
        
        # Fill in number of positions
        self.type(self.NUMBER_OF_POSITIONS_FIELD, data['number_of_positions'])
        
        # Click acitve checkbox if active is True
        if not self.is_selected(self.ACTIVE_CHECKBOX) and data['active']:
            self.click(self.ACTIVE_CHECKBOX)
            
        # Click publish checkbox if publish is True
        if not self.is_selected(self.PUBLISH_CHECKBOX) and data['publish']:
            self.click(self.PUBLISH_CHECKBOX)
        
        # Click save button
        self.click(self.SAVE_BUTTON)