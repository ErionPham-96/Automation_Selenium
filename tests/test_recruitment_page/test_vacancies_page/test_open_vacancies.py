import pytest
from base.base_test import BaseTest
from pages.recruitment_page.recruitment_page import RecruitmentPage
from pages.recruitment_page.vacancies_page import VacanciesPage

class TestOpenVacancies(BaseTest):
    
    @pytest.mark.usefixtures("setup_driver")
    def test_open_vacancies(self):
        VacanciesPage(self.driver).click_vacancies_here()
        assert "viewJobVacancy" in self.driver.current_url
        print("Navigated to Vacancies page. Current URL:", self.driver.current_url) 
        