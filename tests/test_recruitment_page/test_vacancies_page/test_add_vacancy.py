import pytest
from config import USERNAME, PASSWORD
from pages.login_page import LoginPage
from base.base_test import BaseTest
from pages.recruitment_page.add_vacancy_page import AddVacancyPage
from pages.recruitment_page.recruitment_page import RecruitmentPage
from pages.recruitment_page.vacancies_page import VacanciesPage
from pages.recruitment_page.add_vacancy_page import AddVacancyPage
from tests.test_data.vacancy_data import valid_vacancy
@pytest.mark.usefixtures("setup_driver")
class TestFlow(BaseTest):
    
    def test_login(self):
        LoginPage(self.driver).login(USERNAME, PASSWORD)
        assert "dashboard" in self.driver.current_url
        print("Login successful. Current URL:", self.driver.current_url)
    
    def test_open_recruitment(self):
        RecruitmentPage(self.driver).click_recruitment_menu()
        assert "recruitment" in self.driver.current_url
        print("Navigated to Recruitment page. Current URL:", self.driver.current_url)
    
    def test_open_vacancies(self):
        VacanciesPage(self.driver).click_vacancies_here()
        assert "viewJobVacancy" in self.driver.current_url
        print("Navigated to Vacancies page. Current URL:", self.driver.current_url) 
    
    def test_add_vacancy(self):
        add_vacancy_page = AddVacancyPage(self.driver)
        add_vacancy_page.click_add_vacancy()
        add_vacancy_page.fill_vacancy_form(valid_vacancy)
        print("Vacancy added successfully with data:", valid_vacancy)
