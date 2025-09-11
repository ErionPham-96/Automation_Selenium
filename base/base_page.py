from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from config import DEFAULT_TIMEOUT
class BasePage:
    
    def __init__(self, driver, timeout = DEFAULT_TIMEOUT):
        self.driver = driver
        self.wait = WebDriverWait(driver, timeout)
    
    def find(self, locator):
        return self.wait.unlti(EC.presence_of_element_located(locator))
    
    def click(self, locator):
        self.find(locator).click()
    
    def type(self, locator, text):
        self.find(locator).send_keys(text)