import pytest
from base.base_test import BaseTest
from pages.recruitment_page import RecruitmentPage

@pytest.mark.usefixtures("setup_driver")
class TestRecruitment(BaseTest):
    
    def test_open_recruitment(self):
        
        rp = RecruitmentPage(self.driver)
        
        rp.click_recruitment_menu()
        assert "Recruitment" in self.driver.title
        print("Recruitment page opened successfully. Title:", self.driver.title)