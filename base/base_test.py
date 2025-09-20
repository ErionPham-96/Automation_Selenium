import pytest, json, importlib.resources as res
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options

class BaseTest:
    
    @pytest.fixture(scope="session")
    def config(self):
        # Đọc file config/config.json như resource
        with res.files("config").joinpath("config.json").open("r", encoding="utf-8") as f:
            return json.load(f)
    
    @pytest.fixture(scope="class", autouse=True)
    
    def setup_driver(self, request, config):
        options = webdriver.ChromeOptions()
        options.add_argument("--headless")         
        options.add_argument("--no-sandbox")
        options.add_argument("--disable-dev-shm-usage")
        driver = webdriver.Chrome()
        driver.maximize_window()
        
        driver.get(config["base_url"])
        
        # wait ultimately for the username field to be present
        WebDriverWait(driver, 15).until(EC.presence_of_element_located((By.NAME, "username")))
        
        request.cls.driver = driver
        request.cls.config = config
        
        yield
        driver.quit()