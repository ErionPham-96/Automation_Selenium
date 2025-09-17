import pytest
from base.base_test import BaseTest
from pages.recruitment_page.recruitment_page import RecruitmentPage

@pytest.mark.usefixtures("setup_driver")
class TestRecruitment(BaseTest):
    
    def test_open_recruitment(self):
        
        RecruitmentPage(self.driver).click_recruitment_menu()
        # Assert that the Recruitment page is opened by checking the
        assert "recruitment" in self.driver.current_url
        print("Navigated to Recruitment page. Current URL:", self.driver.current_url)