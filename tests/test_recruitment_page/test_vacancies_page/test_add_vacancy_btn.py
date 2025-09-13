import pytest
from base.base_test import BaseTest
from pages.recruitment_page.add_vacancy_page import AddVacancyPage
from pages.recruitment_page.vacancies_page import VacanciesPage

class TestAddVacancy(BaseTest):
    
    @pytest.mark.usefixtures("setup_driver")
    def test_add_vacancy_button(self):
        AddVacancyPage(self.driver).click_add_vacancy()
        assert "Add Job Vacancy" in self.driver.title
        print("Add Vacancy page opened successfully. Title:", self.driver.title)
