from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import pytest
from config import BASE_URL, DEFAULT_TIMEOUT

class BaseTest:
    
    @pytest.fixture(scope="class", autouse=True)
    
    def setup_driver(self, request):
        driver = webdriver.Chrome()
        driver.maximize_window()
        
        driver.get(BASE_URL)
        
        # wait ultimately for the username field to be present
        WebDriverWait(driver, DEFAULT_TIMEOUT).until(EC.presence_of_element_located((By.NAME, "username")))
        
        request.cls.driver = driver
        yield
        driver.quit()