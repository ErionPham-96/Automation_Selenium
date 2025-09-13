from selenium.webdriver.common.by import By
from base.base_page import BasePage
from selenium.webdriver.support import expected_conditions as EC


class AddCandidatePage(BasePage):
    
    # Buttons
    ADD_CANDIDATE_BUTTON = (By.XPATH, "//button[contains(@class,'oxd-button') and normalize-space()='Add']")
    SAVE_BUTTON = (By.XPATH, "//button[@type='submit' and normalize-space()='Save']")
    CANCEL_BUTTON = (By.XPATH, "//button[@type='button' and normalize-space()='Cancel']")
    
    # Name fields
    FIRST_NAME_FIELD = (By.XPATH, "//input[contains(@class, 'orangehrm-firstname')]")
    MIDDLE_NAME_FIELD = (By.XPATH, "//input[contains(@class, 'orangehrm-middlename')]")
    LAST_NAME_FIELD = (By.XPATH, "//input[contains(@class, 'orangehrm-lastname')]")
    
    # Vacancy field
    VACANCY_TRIGGER = (
        By.XPATH,
        "//label[normalize-space()='Vacancy' or normalize-space()='Job Vacancy']"
        "/ancestor::div[contains(@class,'oxd-input-group')]"
        "//div[contains(@class,'oxd-select-text')]"
    )
    # Panel dropdown is rendered after clicking the trigger
    VACANCY_PANEL = (
        By.XPATH,
        "(//div[contains(@class,'oxd-select-dropdown')] | //div[@role='listbox'])"
    )
    def VACANCY_OPTION(self, text: str):
        return (
            By.XPATH,
            "(//div[contains(@class,'oxd-select-dropdown')] | //div[@role='listbox'])"
            "//div[@role='option']//*[normalize-space()='%s']" % text
        )
    def select_vacancy(self, option_text: str):
        self.click(self.VACANCY_TRIGGER)
        self.wait.until(EC.visibility_of_element_located(self.VACANCY_PANEL))
        self.scroll_and_click(self.VACANCY_OPTION(option_text))
        self.wait.until(EC.invisibility_of_element_located(self.VACANCY_PANEL))
        
    # Contact fileds
    EMAIL_FIELD = (By.XPATH, "//label[normalize-space() = 'Email']/ancestor::div[contains(@class, 'oxd-grid-item')]//input")
    CONTACT_NUMBER_FIELD = (By.XPATH, "//label[normalize-space() = 'Contact Number']/ancestor::div[contains(@class, 'oxd-grid-item')]//input")
    
    # Resume filed
    RESUME_UPLOAD_FIELD = (By.XPATH, "//label[normalize-space()='Resume']/ancestor::div[contains(@class,'oxd-input-group')]//div[contains(@class,'oxd-file-input-div')]")
    
    # Other fields
    KEYWORDS_FIELD = (By.XPATH, "//label[normalize-space() = 'Keywords']/ancestor::div[contains(@class, 'oxd-grid-item')]//input")
    NOTES_FIELD = (By.XPATH, "//label[normalize-space() = 'Notes']/ancestor::div[contains(@class, 'oxd-grid-item')]//textarea")
    DATE_OF_APPLICATION_FIELD = (By.XPATH, "//label[normalize-space() = 'Date of Application']/ancestor::div[contains(@class, 'oxd-grid-item')]//input")
    CONSENT_TO_KEEP_DATA = (
                            By.XPATH, 
                            "//label[normalize-space() = 'Consent to keep data']/ancestor::div[contains(@class, 'oxd-input-group')]//span"
    )
    SAVE_SUCCESS_TOAST = (By.XPATH, "//div[contains(@class,'oxd-toast') and contains(.,'Successfully Saved')]")
    
    
    def click_add_candidate(self):
        # Click the "Add Candidate" button
        self.click(self.ADD_CANDIDATE_BUTTON)
        assert "addCandidate" in self.driver.current_url, "Not on Add Candidate Page"
    
    # Fill in the candidate form
    def fill_candidate_form(self, data):
        
        # Fill full name
        self.type(self.FIRST_NAME_FIELD, data["first_name"])
        if data.get("middle_name") is not None:
            self.type(self.MIDDLE_NAME_FIELD, data["middle_name"])
        self.type(self.LAST_NAME_FIELD, data["last_name"])
    
        # Select vacancy from dropdown
        self.select_vacancy(data["vacancy_option"])
    
        # Fill contact details
        self.type(self.EMAIL_FIELD, data["email"])
        if data.get("contact_number") is not None:
            self.type(self.CONTACT_NUMBER_FIELD, str(data["contact_number"]))
    
        # def upload_resume(self, file_path):
        #    self.upload_file(self.RESUME_UPLOAD_FIELD, file_path)

        # Fill other details
        self.type(self.KEYWORDS_FIELD, data["keywords"])
        self.type(self.DATE_OF_APPLICATION_FIELD, data["date_of_application"])
        self.type(self.NOTES_FIELD, data["notes"])
        
        # Consent to keep data
        # Click vào checkbox hiển thị
        if not self.is_selected(self.CONSENT_TO_KEEP_DATA):
            self.click(self.CONSENT_TO_KEEP_DATA)
        # Save the candidate
        self.click(self.SAVE_BUTTON)
        # Verify success toast
        toast = self.wait.until(EC.visibility_of_element_located(self.SAVE_SUCCESS_TOAST))
        assert "Successfully" in toast.text
        self.wait.until(EC.invisibility_of_element_located(self.SAVE_SUCCESS_TOAST))