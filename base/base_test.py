import pytest
from selenium import webdriver

class BaseTest:

    @pytest.fixture(scope="class", autouse=True)
    def setup_driver(self, request, config):
        
        options = webdriver.ChromeOptions()
        # options.add_argument("--headless")         
        options.add_argument("--no-sandbox")
        options.add_argument("--disable-dev-shm-usage")
        
        driver = webdriver.Chrome(options=options)
        driver.maximize_window()
        
        driver.get(config["base_url"])
        
        request.cls.driver = driver
        request.cls.config = config
        
        yield
        driver.quit()