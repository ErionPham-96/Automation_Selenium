from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from config.config import DEFAULT_TIMEOUT

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
    
    def type(self, locator, text):
        element = self.wait.until(EC.element_to_be_clickable(locator))
        element.send_keys(Keys.CONTROL, "a", Keys.BACKSPACE)
        if text is not None:
            element.send_keys(str(text))
        
    def scroll_into_view(self, element):
        self.driver.execute_script("arguments[0].scrollIntoView(true);", element)

    def scroll_and_click(self, locator):
        element = self.find(locator)
        self.scroll_into_view(element)
        element.click()
    
    def is_selected(self, locator):
        element = self.find(locator)
        return element.is_selected()
    