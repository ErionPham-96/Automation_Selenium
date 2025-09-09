from selenium.webdriver.common.by import By
import time
import pytest
from base.base_test import BaseTest as basetest

def test_add_vacancy():
    self.driver.find_element(ByXPATH, "//a[contains(@href, 'viewRecruitmentModule')]").click()
    time.sleep(3)
    
    
