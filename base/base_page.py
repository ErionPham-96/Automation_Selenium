from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from config import DEFAULT_TIMEOUT
class BasePage:
    
    def __init__(self, driver, timeout = DEFAULT_TIMEOUT):
        self.driver = driver
        self.wait = WebDriverWait(driver, timeout)
    
    def find(self, locator):
        # Find an element in the DOM
        return self.wait.until(EC.presence_of_element_located(locator))
    
     def click(self, locator):
        # Wait until the element is clickable in the DOM and UI then click it
        element = self.wait.until(EC.element_to_be_clickable(locator))
        element.click()
    
    def click(self, locator):
        self.find(locator).click()
    
    def type(self, locator, text):
        self.find(locator).send_keys(text)