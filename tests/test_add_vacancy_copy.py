import pytest
from pages.login_page import LoginPage
from base.base_test import BaseTest
from pages.add_vacancy_page import AddVacancyPage
from pages.recruitment_page import RecruitmentPage
from pages.vacancies_page import VacanciesPage
from pages.add_vacancy_page import AddVacancyPage
from tests.test_data.vacancy_data import valid_vacancy
from pages.edit_vacancy_page import EditVacancyPage

@pytest.mark.usefixtures("setup_driver")
class TestFlow(BaseTest):
    
    def test_add_vacancy(self):
        # --- Test data
        data = dict(valid_vacancy)
        
        # 1) Login
        LoginPage(self.driver).login(self.config["username"], self.config["password"])
        assert "dashboard" in self.driver.current_url.lower()

        # 2) Recruitment -> Vacancies
        RecruitmentPage(self.driver).click_recruitment_menu()
        vp = VacanciesPage(self.driver)
        vp.click_vacancies_here()
        assert "viewJobVacancy" in self.driver.current_url

        # 3) Add vacancy
        av = AddVacancyPage(self.driver)
        av.click_add_vacancy()
        av.fill_vacancy_form(data)
        ep = EditVacancyPage(self.driver)
        ep.cancel_edit()
        vp.search_by_job_title(data)
        vp.search_vacancy()
        vp.verify_vacancy_with_data(data)