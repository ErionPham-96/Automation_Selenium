from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from config.config import DEFAULT_TIMEOUT
from selenium.common.exceptions import TimeoutException


class BasePage:
    
    def __init__(self, driver, timeout = DEFAULT_TIMEOUT):
        self.driver = driver
        self.wait = WebDriverWait(driver, timeout)
    
    def find(self, locator):
        # Find an element in the DOM and UI
        try:
            element = self.wait.until(EC.presence_of_element_located(locator))
            return element
        except TimeoutException:
            raise Exception(f"Element with locator {locator} not found in the DOM.")
    
    def click(self, locator):
        # Wait until the element is clickable in the DOM and UI then click it
        try:    
            element = self.wait.until(EC.element_to_be_clickable(locator))
            element.click()
        except TimeoutException:
            raise Exception(f"Element with locator {locator} not clickable.")
    
    def get_text(self, locator):
        element = self.find(locator)
        return element.text
    
    def is_displayed(self, locator):
        # Check if the element is displayed in the DOM and UI
        try:
            self.find(locator) 
            return True
        except:
            return False
    
    def type(self, locator, text):
        # Clear the field first then type the text if text is not None
        element = self.find(locator)
        element.clear()
        if text is not None:
            element.send_keys(text)
            
    def scroll_into_view(self, element):
        self.driver.execute_script("arguments[0].scrollIntoView(true);", element)
    
    def scroll_and_click(self, locator):
        element = self.find(locator)
        self.scroll_into_view(element)
        clickable_element = self.wait.until(EC.element_to_be_clickable(locator))
        clickable_element.click()
    
    def is_selected(self, locator):
        element = self.find(locator)
        return element.is_selected()