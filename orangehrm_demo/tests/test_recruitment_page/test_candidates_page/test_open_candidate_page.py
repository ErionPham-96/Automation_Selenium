import pytest
from base.base_test import BaseTest
from pages.recruitment_page.candidates_page.candidates_page import CandidatesPage

class TestCandidatesPage(BaseTest):
    @pytest.mark.usefixtures("setup_driver")
    
    def test_open_candidate_page(self):
        CandidatesPage(self.driver).click_candidates_here()
        assert "viewCandidates" in self.driver.current_url, "Not on Candidates Page"