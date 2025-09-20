from selenium.webdriver.common.by import By
from base.base_page import BasePage

class VacanciesPage(BasePage):
    
    VACANCIES_HERE = (By.XPATH, "//a[contains(@class,'oxd-topbar-body-nav-tab-item') and normalize-space()='Vacancies']")
    
    SEARCH_JOB_TITLE = (By.XPATH, "//label[normalize-space()='Job Title']"
                        "/ancestor::div[contains(@class,'oxd-grid-item')]"
                        "//div[contains(@class,'oxd-select-text-input')]")
    
    SEARCH_BTN = (By.XPATH, "//button[@type = 'submit' and normalize-space() = 'Search']")
    VACANCY_ROWS = (By.XPATH, "//div[contains(@class,'oxd-table-body')]//div[contains(@class,'oxd-table-card')]")
    NO_RECORDS = (By.XPATH, "//*[normalize-space(.)='No Records Found']")
    
    def click_vacancies_here(self):
        # Click on the Vacancies link in the recruitment page
        self.click(self.VACANCIES_HERE)
    def get_header_text(self):
        # Return the text of the vacancies header
        return self.find(self.VACANCIES_HERE).text
    def is_displayed(self):
        # Return True if vacancies header is visible
        header = self.find(self.VACANCIES_HERE)
        return header.is_displayed()
    def row_by_vacancy(self, vacancy_name: str) -> str:
        # Return the locator Vacancy name
        xpath = f"//div[@class='oxd-table-card']//div[@role='cell']//div[normalize-space()='{vacancy_name}']/ancestor::div[@class='oxd-table-card']"
        return (By.XPATH, xpath)
    def edit_vacancy(self, vacancy_name: str) -> str:
        xpath = self.row_by_vacancy(vacancy_name) + "//button[i[contains(@class,'bi-pencil-fill')]]"
        return self.find((By.XPATH, xpath)).click()
    def job_title_option(self, job_title):
        # Locator for job title option in dropdown
        return (
            By.XPATH, 
            f"//div[contains(@class,'oxd-select-option')][normalize-space()='{job_title}']"
        )
    def search_by_job_title(self, data):
        self.click(self.SEARCH_JOB_TITLE)
        self.scroll_and_click(self.job_title_option(data["job_title"]))
        
    def search_vacancy(self):
        return self.click(self.SEARCH_BTN)
    
    def verify_vacancy_with_data(self, data: dict):
        vacancy_name = data["vacancy_name"]

        # 1. Define row need verify
        row_xpath = (
            f"//div[contains(@class,'oxd-table-card')]"
            f"//div[@role='cell']//div[normalize-space()='{vacancy_name}']"
            f"/ancestor::div[contains(@class,'oxd-table-card')]"
        )
        rows = self.find_elements((By.XPATH, row_xpath))
        if not rows:
            raise AssertionError(f"No records found '{vacancy_name}' in table.")

        # 2. Get row and text
        row = rows[0]
        row_text = row.text.strip()

        # 3. Compare data
        assert data["vacancy_name"]   in row_text, f"Vacancy mismatch. Row: {row_text}"
        assert data["job_title"]      in row_text, f"Job Title mismatch. Row: {row_text}"
        assert data["hiring_manager"] in row_text, f"Hiring Manager mismatch. Row: {row_text}"

        # 4. If all pass.
        print(f"Vacancy '{data['vacancy_name']}' match with data test.")

        return row

        