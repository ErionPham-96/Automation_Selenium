import pytest
from base.base_test import BaseTest
from pages.login_page import LoginPage
from pages.recruitment_page import RecruitmentPage
from pages.candidates_page import CandidatesPage
from pages.add_candidate_page import AddCandidatePage
from tests.test_data.candidate_data import valid_candidate

class TestAddCandidate(BaseTest):
    
    @pytest.mark.usefixtures("setup_driver")
    def test_add_candidate(self):
        
        # Step 1: Login
        LoginPage(self.driver).login(self.config["username"], self.config["password"])
        print("Login successful. Current URL:", self.driver.current_url)
        
        # Step 2: Navigate to Recruitment Page
        RecruitmentPage(self.driver).click_recruitment_menu()
        assert "recruitment" in self.driver.current_url
        print("Navigated to Recruitment page. Current URL:", self.driver.current_url)
        
        # Step 3: Navigate to Candidates Page
        CandidatesPage(self.driver).click_candidates_here()
        assert "viewCandidates" in self.driver.current_url
        
        # Step 4: Add Candidate and Fill Form
        AddCandidatePage(self.driver).click_add_candidate()
        AddCandidatePage(self.driver).fill_candidate_form(valid_candidate)
        print("Candidate added successfully with data:", valid_candidate)
